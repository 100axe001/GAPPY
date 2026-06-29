import os
import shutil
import datetime
import secrets
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession

from .database import get_db, Base, engine
from . import models, schemas, crud, auth, ai
from .security import encrypt_data, decrypt_data
from .integrations.registry import registry
from .integrations import service as int_service
from .integrations.routing import route_and_execute_query
from . import settings_service, chat as chat_engine
from .integrations.web_search import web_search, WebSearchError
from .integrations import email_adapter


app = FastAPI(title="LifeOS API", version="1.0.0")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure upload directory exists
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.on_event("startup")
async def startup():
    # Automatically create tables in local Postgres
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# -- Auth Routes --
@app.post("/api/auth/signup", response_model=schemas.UserResponse)
async def signup(user_in: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user_by_email(db, email=user_in.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    hashed_pwd = auth.get_password_hash(user_in.password)
    user = await crud.create_user(db, user_in, hashed_pwd)
    return user

@app.post("/api/auth/login", response_model=schemas.Token)
async def login(user_in: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    user = await crud.get_user_by_email(db, email=user_in.email)
    if not user or not auth.verify_password(user_in.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# -- Item CRUD Routes --
@app.get("/api/items", response_model=List[schemas.ItemResponse])
async def list_items(
    type: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return await crud.get_items(db, item_type=type)

@app.post("/api/items", response_model=schemas.ItemResponse)
async def create_item(
    item_in: schemas.ItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    # Create the item in DB
    item = await crud.create_item(db, item_in)
    
    # If the item is a note, run AI insight analysis & auto-linking
    if item.type == "note":
        existing_notes = await crud.get_items(db, item_type="note")
        # Filter out the newly created note from comparisons
        existing_notes = [n for n in existing_notes if n.id != item.id]
        
        ai_res = await ai.analyze_note_and_suggest_links(item, existing_notes)
        
        # Save trace and connections in metadata
        item_meta = dict(item.metadata_json or {})
        item_meta["ai_analysis"] = {
            "trace": ai_res.get("trace"),
            "suggested_tasks": ai_res.get("suggested_tasks", []),
            "suggested_connections": ai_res.get("connections", [])
        }
        item.metadata_json = item_meta
        await db.flush()
        
        # Automatically create suggested tasks and connections if configured
        # (For MVP, we auto-create them directly so the command center works automatically!)
        for t in ai_res.get("suggested_tasks", []):
            task_due = None
            if t.get("due_date"):
                try:
                    task_due = datetime.datetime.strptime(t["due_date"], "%Y-%m-%d")
                except ValueError:
                    pass
            db_task = await crud.create_item(db, schemas.ItemCreate(
                type="task",
                title=t["title"],
                content=t.get("content", ""),
                priority=t.get("priority", "medium"),
                status="todo",
                due_date=task_due,
                metadata_json={"source_note_id": item.id, "auto_generated": True}
            ))
            # Link task to the note
            await crud.create_connection(db, schemas.ConnectionCreate(
                source_id=item.id,
                target_id=db_task.id,
                connection_type="suggested_task"
            ))
            
        # (We store connection suggestions in metadata_json so the user can accept them with a single click!)
        pass
                
    return item

@app.get("/api/items/{item_id}", response_model=schemas.ItemResponse)
async def get_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    item = await crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/api/items/{item_id}", response_model=schemas.ItemResponse)
async def update_item(
    item_id: int,
    item_in: schemas.ItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    item = await crud.update_item(db, item_id, item_in)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/api/items/{item_id}")
async def delete_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    success = await crud.delete_item(db, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}

# -- Connections Routes --
@app.get("/api/connections", response_model=List[schemas.ConnectionDetailResponse])
async def list_connections(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return await crud.get_connections(db)

@app.post("/api/connections", response_model=schemas.ConnectionResponse)
async def create_connection(
    conn_in: schemas.ConnectionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return await crud.create_connection(db, conn_in)

@app.delete("/api/connections/{conn_id}")
async def delete_connection(
    conn_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    success = await crud.delete_connection(db, conn_id)
    if not success:
        raise HTTPException(status_code=404, detail="Connection not found")
    return {"detail": "Connection deleted"}

@app.get("/api/items/{item_id}/connections", response_model=List[schemas.ConnectionDetailResponse])
async def get_item_connections(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return await crud.get_connections_by_item_id(db, item_id)

# -- Learning Routes --
@app.post("/api/learning/upload", response_model=schemas.ItemResponse)
async def upload_material(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    # 1. Save locally
    filename = f"{int(datetime.datetime.utcnow().timestamp())}_{file.filename}"
    local_path = os.path.join(UPLOAD_DIR, filename)
    with open(local_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    # 2. Upload to Lemma in background
    sdk_res = await ai.upload_learning_file_to_lemma(filename, local_path)
    if "error" in sdk_res:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Lemma upload failed: {sdk_res['error']}"
        )
        
    # 3. Create Item representing this Study Material
    item_in = schemas.ItemCreate(
        type="study_material",
        title=file.filename,
        content=f"/learning/{filename}", # Lemma path alias
        status="todo",
        metadata_json={
            "local_path": local_path,
            "lemma_path": f"/learning/{filename}",
            "upload_response": sdk_res
        }
    )
    return await crud.create_item(db, item_in)

@app.post("/api/learning/study")
async def start_study_session(
    material_id: int = Form(...),
    self_reported_confusion: str = Form(""),
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    # Fetch material item
    material = await crud.get_item(db, material_id)
    if not material or material.type != "study_material":
        raise HTTPException(status_code=404, detail="Study material not found")
        
    lemma_path = material.metadata_json.get("lemma_path")
    if not lemma_path:
        raise HTTPException(status_code=400, detail="Material is missing Lemma index path")
        
    # Generate study plan & questions using Lemma SDK
    ai_res, search_results = await ai.generate_study_plan_and_questions(
        material_title=material.title,
        material_path=lemma_path,
        self_reported_confusion=self_reported_confusion
    )
    
    if "error" in ai_res:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Study plan generation failed: {ai_res['error']}"
        )
        
    # Store generated Weak Topics in DB
    created_topics = []
    for topic_data in ai_res.get("weak_topics", []):
        db_topic = await crud.create_item(db, schemas.ItemCreate(
            type="study_topic",
            title=topic_data["topic"],
            content=topic_data["reason"],
            status="weak",
            metadata_json={"source_material_id": material_id}
        ))
        created_topics.append(db_topic)
        # Link topic to source material
        await crud.create_connection(db, schemas.ConnectionCreate(
            source_id=material_id,
            target_id=db_topic.id,
            connection_type="weakness_of"
        ))
        
    # Store generated Revision Plan steps in DB
    created_revisions = []
    for plan_step in ai_res.get("revision_plan", []):
        due_date = None
        if plan_step.get("due_date"):
            try:
                due_date = datetime.datetime.strptime(plan_step["due_date"], "%Y-%m-%d")
            except ValueError:
                pass
        db_rev = await crud.create_item(db, schemas.ItemCreate(
            type="task",
            title=plan_step["title"],
            content=plan_step["content"],
            status="todo",
            priority=plan_step.get("priority", "medium"),
            due_date=due_date,
            metadata_json={"source_material_id": material_id, "is_study_revision": True}
        ))
        created_revisions.append(db_rev)
        # Link task to study material
        await crud.create_connection(db, schemas.ConnectionCreate(
            source_id=material_id,
            target_id=db_rev.id,
            connection_type="practice_of"
        ))
        
    # Save the practice questions in the study session response but don't commit them to DB items
    # (Or they can be answered on frontend dynamically)
    return {
        "practice_questions": ai_res.get("practice_questions", []),
        "search_results": search_results,
        "weak_topics_count": len(created_topics),
        "revision_steps_count": len(created_revisions)
    }

# -- NEW EXTENSION ENDPOINTS --

# 1. Life Ops
@app.get("/api/lifeops/weekly-review")
async def get_weekly_review(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    now = datetime.datetime.utcnow()
    # Fetch all tasks and deadlines
    tasks = await crud.get_items(db, limit=500, item_type="task")
    deadlines = await crud.get_items(db, limit=500, item_type="deadline")
    all_tasks = tasks + deadlines
    
    open_tasks = []
    slipped_tasks = []
    stale_followups = []
    
    three_days_ago = now - datetime.timedelta(days=3)
    
    for t in all_tasks:
        if t.status != "done":
            # Is it open task or slipped?
            if t.due_date and t.due_date < now:
                slipped_tasks.append(t)
            else:
                open_tasks.append(t)
                
            # Is it a follow-up?
            is_waiting = (t.status == "waiting" or (t.metadata_json and t.metadata_json.get("waiting_on")))
            if is_waiting and t.updated_at <= three_days_ago:
                stale_followups.append(t)
                
    ai_summary = await ai.generate_weekly_review_summary(open_tasks, slipped_tasks, stale_followups)
    return ai_summary

@app.post("/api/lifeops/commit-parse")
async def commit_parse(
    req: schemas.CommitmentInboxRequest,
    current_user: models.User = Depends(auth.get_current_user)
):
    return await ai.parse_commitment_inbox(req.text)

@app.get("/api/lifeops/stale-followups")
async def get_stale_followups_list(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    now = datetime.datetime.utcnow()
    three_days_ago = now - datetime.timedelta(days=3)
    
    tasks = await crud.get_items(db, limit=500, item_type="task")
    deadlines = await crud.get_items(db, limit=500, item_type="deadline")
    all_tasks = tasks + deadlines
    
    stale = []
    for t in all_tasks:
        if t.status != "done":
            is_waiting = (t.status == "waiting" or (t.metadata_json and t.metadata_json.get("waiting_on")))
            if is_waiting and t.updated_at <= three_days_ago:
                stale.append(t)
                
    return {
        "count": len(stale),
        "items": [
            {
                "id": t.id,
                "title": t.title,
                "status": t.status,
                "priority": t.priority,
                "due_date": t.due_date,
                "metadata_json": t.metadata_json,
                "updated_at": t.updated_at
            } for t in stale
        ]
    }

# 2. Second Brain
@app.get("/api/brain/insights")
async def get_brain_insights(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    notes = await crud.get_items(db, limit=500, item_type="note")
    # Filter notes from last 30 days
    thirty_days_ago = datetime.datetime.utcnow() - datetime.timedelta(days=30)
    recent_notes = [n for n in notes if n.created_at >= thirty_days_ago]
    insights = await ai.surface_brain_insights(recent_notes)
    return {"insights": insights}

@app.post("/api/brain/draft")
async def generate_draft(
    req: schemas.DraftGenerateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    notes = []
    for nid in req.note_ids:
        note = await crud.get_item(db, nid)
        if note and note.type == "note":
            notes.append(note)
    if not notes:
        raise HTTPException(status_code=400, detail="No valid notes selected")
    
    draft_content = await ai.generate_draft_from_notes(notes, req.format)
    return {"draft": draft_content}

# 3. Learning Companion
@app.get("/api/learning/reviews/due", response_model=List[schemas.StudyReviewResponse])
async def get_due_reviews(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return await crud.get_due_study_reviews(db, user_id=current_user.id)

@app.post("/api/learning/reviews/submit")
async def submit_review(
    submission: schemas.StudyReviewSubmit,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    res = await crud.update_study_review(db, submission.review_id, submission.score)
    if not res:
        raise HTTPException(status_code=404, detail="Study review not found")
    return {"detail": "Review updated", "interval_days": res.interval_days, "due_date": res.due_date}

@app.post("/api/learning/test-submit")
async def submit_practice_test(
    submission: schemas.PracticeTestSubmit,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    ai_res = await ai.score_test_and_map_topics(submission.answers)
    
    created_topics = []
    for topic_data in ai_res.get("topic_strength", []):
        status = topic_data.get("status", "weak")
        db_topic = await crud.create_item(db, schemas.ItemCreate(
            type="study_topic",
            title=topic_data["topic"],
            content=f"Strength Score: {topic_data.get('score')}",
            status=status,
            metadata_json={"source_material_id": submission.material_id, "score": topic_data.get("score")}
        ))
        created_topics.append(db_topic)
        await crud.create_connection(db, schemas.ConnectionCreate(
            source_id=submission.material_id,
            target_id=db_topic.id,
            connection_type="weakness_of" if status == "weak" else "strength_of"
        ))
        
    created_revisions = []
    for plan_step in ai_res.get("suggested_revisions", []):
        due_date = None
        if plan_step.get("due_date"):
            try:
                due_date = datetime.datetime.strptime(plan_step["due_date"], "%Y-%m-%d")
            except ValueError:
                pass
        db_rev = await crud.create_item(db, schemas.ItemCreate(
            type="task",
            title=plan_step["title"],
            content=plan_step["content"],
            status="todo",
            priority=plan_step.get("priority", "medium"),
            due_date=due_date,
            metadata_json={"source_material_id": submission.material_id, "is_study_revision": True}
        ))
        created_revisions.append(db_rev)
        await crud.create_connection(db, schemas.ConnectionCreate(
            source_id=submission.material_id,
            target_id=db_rev.id,
            connection_type="practice_of"
        ))
        
    return {
        "topic_strength": ai_res.get("topic_strength", []),
        "suggested_revisions_count": len(created_revisions)
    }

@app.post("/api/learning/debrief")
async def pomodoro_debrief(
    req: schemas.PomodoroDebriefRequest,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    ai_res = await ai.generate_study_debrief_insights(req.summary, req.confusion)
    
    debrief_note = await crud.create_item(db, schemas.ItemCreate(
        type="note",
        title=f"Study Session Debrief: {datetime.datetime.utcnow().strftime('%Y-%m-%d')}",
        content=f"Focus Summary: {req.summary}\nConfusion/Struggles: {req.confusion or 'None'}\n\nAI Insights:\n{ai_res.get('feedback', '')}\nSuggested Next Focus: {ai_res.get('suggested_next_focus', '')}",
        status="todo"
    ))
    
    for wt in ai_res.get("weak_topics", []):
        db_topic = await crud.create_item(db, schemas.ItemCreate(
            type="study_topic",
            title=wt["topic"],
            content=wt["reason"],
            status="weak",
            metadata_json={"source_debrief_id": debrief_note.id}
        ))
        await crud.create_connection(db, schemas.ConnectionCreate(
            source_id=debrief_note.id,
            target_id=db_topic.id,
            connection_type="weakness_of"
        ))
        
    return ai_res

@app.get("/api/learning/reviews/generate-quiz")
async def get_review_quiz(
    concept_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    concept = await crud.get_item(db, concept_id)
    if not concept:
        raise HTTPException(status_code=404, detail="Concept not found")
    questions = await ai.generate_spaced_repetition_quiz(concept.title, concept.content or "")
    return {"questions": questions}

# 4. Cross-Module
@app.get("/api/search", response_model=List[schemas.ItemResponse])
async def universal_search(
    q: str,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    items = await crud.get_items(db, limit=500)
    query_lower = q.lower()
    results = []
    for item in items:
        # Search title, content, status, priority, or tags
        title_match = query_lower in item.title.lower()
        content_match = (item.content and query_lower in item.content.lower())
        if title_match or content_match:
            results.append(item)
    return results

@app.get("/api/today")
async def get_today_view(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    now = datetime.datetime.utcnow()
    today_start = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_end = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    
    items = await crud.get_items(db, limit=500)
    
    overdue = []
    due_today = []
    stale_followups = []
    
    three_days_ago = now - datetime.timedelta(days=3)
    
    for item in items:
        if item.type in ("task", "deadline") and item.status != "done":
            if item.due_date:
                if item.due_date < today_start:
                    overdue.append(item)
                elif today_start <= item.due_date <= today_end:
                    due_today.append(item)
            
            is_waiting = (item.status == "waiting" or (item.metadata_json and item.metadata_json.get("waiting_on")))
            if is_waiting and item.updated_at <= three_days_ago:
                stale_followups.append(item)
                
    due_reviews = await crud.get_due_study_reviews(db, user_id=current_user.id)
    
    # AI insights card from notes
    notes = [n for n in items if n.type == "note" and n.created_at >= (now - datetime.timedelta(days=30))]
    insights = []
    if notes:
        insights = await ai.surface_brain_insights(notes)
        
    insight_card = insights[0] if insights else {
        "title": "Welcome to LifeOS",
        "description": "Log your daily notes and tasks. The AI will automatically analyze your second brain and surface key connections here.",
        "action": "expand"
    }
        
    return {
        "overdue_tasks": overdue,
        "due_today_tasks": due_today,
        "stale_followups": {
            "count": len(stale_followups),
            "items": stale_followups
        },
        "due_reviews": {
            "count": len(due_reviews),
            "items": due_reviews
        },
        "insight_card": insight_card
    }

# -- Integrations Routes --

@app.get("/api/integrations", response_model=List[schemas.UserIntegrationResponse])
async def list_integrations(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    user_ints = await int_service.get_all_user_integrations(db, current_user.id)
    user_ints_map = {ui.name: ui for ui in user_ints}
    
    # Query SDK connector status
    status_data = {"installed": [], "accounts": []}
    try:
        from .sdk_client import get_lemma_pod
        pod = get_lemma_pod()
        status_data = pod.connectors.status()
    except Exception as e:
        import logging
        logging.getLogger("lifeos.main").warning(f"Failed to retrieve SDK connector status: {e}")
        
    def is_app_connected(app_name: str) -> tuple[bool, str]:
        norm_app = app_name.replace("_", "").replace("-", "").lower()
        if norm_app == "googlecalendar":
            norm_app = "googlecalendar"
        for acc in status_data.get("accounts", []):
            norm_acc = acc.get("connector_id", "").replace("_", "").replace("-", "").lower()
            if norm_app == norm_acc:
                return True, acc.get("email") or "Connected Account"
        return False, ""

    response = []
    for adapter in registry.list_adapters():
        is_conn, conn_email = is_app_connected(adapter.name)
        if is_conn:
            response.append(schemas.UserIntegrationResponse(
                name=adapter.name,
                is_connected=True,
                scopes=adapter.scopes,
                metadata_json={"email": conn_email},
                health_status="healthy",
                error_message=None,
                last_sync_at=None
            ))
        else:
            ui = user_ints_map.get(adapter.name)
            if ui:
                response.append(schemas.UserIntegrationResponse(
                    name=ui.name,
                    is_connected=ui.is_connected,
                    scopes=ui.scopes,
                    metadata_json=ui.metadata_json or {},
                    health_status=ui.health_status,
                    error_message=ui.error_message,
                    last_sync_at=ui.last_sync_at
                ))
            else:
                response.append(schemas.UserIntegrationResponse(
                    name=adapter.name,
                    is_connected=False,
                    scopes=[],
                    metadata_json={},
                    health_status="healthy",
                    error_message=None,
                    last_sync_at=None
                ))
    return response

@app.get("/api/integrations/{name}/auth-url")
async def get_integration_auth_url(
    name: str,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    normalized_name = name.replace("-", "_")
    adapter = registry.get_adapter(normalized_name)
    if not adapter:
        raise HTTPException(status_code=404, detail="Integration not found")
        
    # Check if this adapter can generate dynamic connect URL using Lemma SDK Connectors
    # google_calendar is native, other native connectors can follow this
    if normalized_name in ("google_calendar", "gmail", "slack", "google_tasks"):
        try:
            auth_url = adapter.get_auth_url("", "")
            return {"auth_url": auth_url}
        except Exception as e:
            import logging
            logging.getLogger("lifeos.main").error(f"Failed generating Lemma connect URL: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail=f"Lemma connector failed: {str(e)}")
            
    # For mock integrations, fall back to our mock callback auth url flow
    redirect_uri = os.getenv("GOOGLE_REDIRECT_URI") or "http://localhost:8081/api/integrations/oauth/callback"
    csrf_nonce = secrets.token_hex(16)
    state_payload = f"{current_user.id}:{csrf_nonce}:{normalized_name}"
    state_encrypted = encrypt_data(state_payload)
    auth_url = adapter.get_auth_url(redirect_uri, state_encrypted)
    return {"auth_url": auth_url}

@app.get("/api/integrations/oauth/callback", response_class=HTMLResponse)
async def oauth_callback(
    code: str,
    state: str,
    db: AsyncSession = Depends(get_db)
):
    try:
        decrypted = decrypt_data(state)
        parts = decrypted.split(":")
        if len(parts) < 2:
            raise ValueError("Invalid state payload format.")
        user_id = int(parts[0])
        name = parts[2] if len(parts) > 2 else "google_calendar"
    except Exception as e:
        return HTMLResponse(
            status_code=400,
            content=f"<html><body><h3>Security Error</h3><p>OAuth state validation failed: {e}</p></body></html>"
        )
        
    adapter = registry.get_adapter(name)
    if not adapter:
        return HTMLResponse(status_code=404, content=f"<html><body><h3>Integration '{name}' not found</h3></body></html>")
        
    redirect_uri = os.getenv("GOOGLE_REDIRECT_URI") or "http://localhost:8081/api/integrations/oauth/callback"
    
    try:
        token_data = await adapter.exchange_code(redirect_uri, code)
        await int_service.save_user_credentials(
            db,
            user_id=user_id,
            name=name,
            token_data=token_data,
            scopes=adapter.scopes
        )
        
        return HTMLResponse(
            content=f"""
            <html>
              <head>
                <title>Connection Successful</title>
                <style>
                  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; text-align: center; padding-top: 15vh; background-color: #F7F4EF; color: #2C2825; }}
                  .card {{ background-color: #FFFDF9; border: 1px solid #E3DDD6; border-radius: 8px; max-width: 400px; margin: 0 auto; padding: 2rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }}
                  h3 {{ font-family: Georgia, serif; color: #8FAF8F; font-size: 1.5rem; margin-bottom: 1rem; }}
                  p {{ color: #8C7F74; font-size: 0.95rem; margin-bottom: 2rem; }}
                </style>
              </head>
              <body>
                <div class="card">
                  <h3>{adapter.display_name} Connected!</h3>
                  <p>Your workspace is now securely linked. You can close this tab and return to LifeOS.</p>
                  <script>
                    if (window.opener && typeof window.opener.onOAuthSuccess === 'function') {{
                      window.opener.onOAuthSuccess('{adapter.display_name}');
                    }}
                    setTimeout(function() {{ window.close(); }}, 2500);
                  </script>
                </div>
              </body>
            </html>
            """
        )
    except Exception as err:
        import logging
        logging.getLogger("lifeos.main").error(f"OAuth callback code exchange failed: {err}", exc_info=True)
        return HTMLResponse(
            status_code=500,
            content=f"<html><body><h3>OAuth Connection Failed</h3><p>Error: {err}</p></body></html>"
        )

@app.delete("/api/integrations/{name}")
async def disconnect_integration(
    name: str,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    normalized_name = name.replace("-", "_")
    
    sdk_disconnected = False
    try:
        from .sdk_client import get_lemma_pod
        pod = get_lemma_pod()
        norm_app = normalized_name.replace("_", "").replace("-", "").lower()
        acc_list = pod.connectors.accounts.list()
        for acc in acc_list.items:
            norm_acc = acc.connector_id.replace("_", "").replace("-", "").lower()
            if norm_app == norm_acc:
                pod.connectors.accounts.delete(str(acc.id))
                sdk_disconnected = True
                break
    except Exception as e:
        import logging
        logging.getLogger("lifeos.main").warning(f"Failed to disconnect from SDK: {e}")
        
    db_disconnected = await int_service.disconnect_user_integration(db, current_user.id, normalized_name)
    if not sdk_disconnected and not db_disconnected:
        raise HTTPException(status_code=404, detail="Integration not connected")
    return {"detail": f"Disconnected {name} successfully."}

@app.post("/api/integrations/{name}/test")
async def test_integration_connection(
    name: str,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    normalized_name = name.replace("-", "_")
    adapter = registry.get_adapter(normalized_name)
    if adapter and normalized_name in ("google_calendar", "gmail", "slack", "google_tasks"):
        success = await adapter.test_connection({})
        if not success:
            return {
                "status": "unhealthy",
                "error_message": "Authentication failed. Reconnection required."
            }
        return {"status": "healthy"}
        
    success = await int_service.test_integration_health(db, current_user.id, normalized_name)
    if not success:
        ui = await int_service.get_user_integration(db, current_user.id, normalized_name)
        error_msg = ui.error_message if ui else "Authentication failed. Reconnection required."
        return {
            "status": "unhealthy",
            "error_message": error_msg
        }
    return {"status": "healthy"}

# -- AI Assistant Query Endpoint --

@app.post("/api/assistant/query", response_model=schemas.AssistantQueryResponse)
async def assistant_query(
    req: schemas.AssistantQueryRequest,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    res = await route_and_execute_query(db, user_id=current_user.id, query=req.query)
    return res

# -- Chat / Conversations --

@app.get("/api/chat/conversations", response_model=List[schemas.ConversationResponse])
async def list_conversations(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return await crud.list_conversations(db, current_user.id)

@app.post("/api/chat/conversations", response_model=schemas.ConversationResponse)
async def create_conversation(
    conv_in: schemas.ConversationCreate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return await crud.create_conversation(db, current_user.id, title=conv_in.title, tag=conv_in.tag)

@app.patch("/api/chat/conversations/{conv_id}", response_model=schemas.ConversationResponse)
async def update_conversation(
    conv_id: int,
    conv_in: schemas.ConversationUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    conv = await crud.update_conversation(db, conv_id, current_user.id,
                                          title=conv_in.title, tag=conv_in.tag)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conv

@app.delete("/api/chat/conversations/{conv_id}")
async def delete_conversation(
    conv_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    ok = await crud.delete_conversation(db, conv_id, current_user.id)
    if not ok:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return {"detail": "Conversation deleted"}

@app.get("/api/chat/conversations/{conv_id}/messages", response_model=List[schemas.MessageResponse])
async def get_conversation_messages(
    conv_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    conv = await crud.get_conversation(db, conv_id, current_user.id)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return await crud.get_messages(db, conv_id)

@app.post("/api/chat/conversations/{conv_id}/send", response_model=schemas.ChatSendResponse)
async def send_chat_message(
    conv_id: int,
    req: schemas.ChatSendRequest,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    conv = await crud.get_conversation(db, conv_id, current_user.id)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversation not found")
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Empty message")

    settings = await settings_service.get_resolved_settings(db, current_user.id)
    user_row, assistant_row, tools_used = await chat_engine.send_message(
        db, current_user.id, conv, req.message, settings
    )
    return schemas.ChatSendResponse(
        conversation_id=conv.id,
        user_message=user_row,
        assistant_message=assistant_row,
        tools_used=tools_used
    )

# -- Settings --

@app.get("/api/settings", response_model=schemas.SettingsResponse)
async def get_settings(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    values = await settings_service.get_masked_settings(db, current_user.id)
    return schemas.SettingsResponse(values=values)

@app.put("/api/settings", response_model=schemas.SettingsResponse)
async def update_settings(
    req: schemas.SettingsUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    values = await settings_service.update_settings(db, current_user.id, req.values)
    return schemas.SettingsResponse(values=values)

@app.post("/api/settings/test-email")
async def settings_test_email(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    settings = await settings_service.get_resolved_settings(db, current_user.id)
    ok = await email_adapter.test_email(settings)
    return {"status": "healthy" if ok else "unhealthy"}

# -- Web Search --

@app.post("/api/web-search", response_model=schemas.WebSearchResponse)
async def run_web_search(
    req: schemas.WebSearchRequest,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    settings = await settings_service.get_resolved_settings(db, current_user.id)
    try:
        res = await web_search(req.query, settings, max_results=req.max_results or 6)
    except WebSearchError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Web search failed: {e}")
    return schemas.WebSearchResponse(
        query=req.query,
        provider=res.get("provider", "unknown"),
        answer=res.get("answer"),
        results=[schemas.WebSearchResult(**r) for r in res.get("results", [])]
    )

# Mount static files at root
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")


