import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from . import models, schemas

# -- User Helpers --
async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(models.User).where(models.User.email == email))
    return result.scalars().first()

async def create_user(db: AsyncSession, user_in: schemas.UserCreate, hashed_password: str):
    db_user = models.User(email=user_in.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.flush()
    return db_user

# -- Item Helpers --
async def get_item(db: AsyncSession, item_id: int):
    result = await db.execute(select(models.Item).where(models.Item.id == item_id))
    return result.scalars().first()

async def get_items(db: AsyncSession, skip: int = 0, limit: int = 100, item_type: str = None):
    query = select(models.Item)
    if item_type:
        query = query.where(models.Item.type == item_type)
    query = query.order_by(models.Item.created_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def create_item(db: AsyncSession, item_in: schemas.ItemCreate):
    due_date = item_in.due_date
    if due_date and due_date.tzinfo is not None:
        due_date = due_date.replace(tzinfo=None)
        
    db_item = models.Item(
        type=item_in.type,
        title=item_in.title,
        content=item_in.content,
        status=item_in.status,
        priority=item_in.priority,
        due_date=due_date,
        metadata_json=item_in.metadata_json or {}
    )
    db.add(db_item)
    await db.flush()
    return db_item

async def update_item(db: AsyncSession, item_id: int, item_in: schemas.ItemUpdate):
    db_item = await get_item(db, item_id)
    if not db_item:
        return None
    
    update_data = item_in.model_dump(exclude_unset=True)
    if "due_date" in update_data and update_data["due_date"] is not None:
        if update_data["due_date"].tzinfo is not None:
            update_data["due_date"] = update_data["due_date"].replace(tzinfo=None)
            
    # Check if task is being marked as done and has recurrence rules
    was_done = db_item.status == "done"
    new_status = update_data.get("status")
    
    for key, value in update_data.items():
        setattr(db_item, key, value)
    
    await db.flush()
    
    # Trigger recurring task engine if task is newly completed
    if new_status == "done" and not was_done and db_item.metadata_json:
        meta = db_item.metadata_json
        if meta.get("is_recurring") is True:
            interval = meta.get("recurrence_interval", "daily")
            custom_days = meta.get("recurrence_custom_days")
            
            # Calculate next due date
            base_date = db_item.due_date or datetime.datetime.utcnow()
            if interval == "daily":
                next_due = base_date + datetime.timedelta(days=1)
            elif interval == "weekly":
                next_due = base_date + datetime.timedelta(weeks=1)
            elif interval == "monthly":
                next_due = base_date + datetime.timedelta(days=30)
            elif interval == "custom" and custom_days:
                next_due = base_date + datetime.timedelta(days=int(custom_days))
            else:
                next_due = base_date + datetime.timedelta(days=1)
                
            # Create next instance task
            next_task = models.Item(
                type=db_item.type,
                title=db_item.title,
                content=db_item.content,
                status="todo",
                priority=db_item.priority,
                due_date=next_due,
                metadata_json=db_item.metadata_json # Copy recurrence settings verbatim
            )
            db.add(next_task)
            await db.flush()
            
            # Link next instance to completed instance for history
            conn = models.Connection(
                source_id=db_item.id,
                target_id=next_task.id,
                connection_type="recurrence_next"
            )
            db.add(conn)
            await db.flush()
            
    return db_item

async def delete_item(db: AsyncSession, item_id: int):
    db_item = await get_item(db, item_id)
    if db_item:
        await db.delete(db_item)
        await db.flush()
        return True
    return False

# -- Connection Helpers --
async def create_connection(db: AsyncSession, conn_in: schemas.ConnectionCreate):
    db_conn = models.Connection(
        source_id=conn_in.source_id,
        target_id=conn_in.target_id,
        connection_type=conn_in.connection_type
    )
    db.add(db_conn)
    await db.flush()
    return db_conn

async def get_connections(db: AsyncSession, skip: int = 0, limit: int = 100):
    # Fetch connections with their related items for detailed response
    query = select(models.Connection).order_by(models.Connection.created_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    conns = result.scalars().all()
    
    detailed_conns = []
    for c in conns:
        # Load source and target titles manually if lazy loading isn't triggered
        source = await get_item(db, c.source_id)
        target = await get_item(db, c.target_id)
        if source and target:
            detailed_conns.append({
                "id": c.id,
                "source_id": c.source_id,
                "target_id": c.target_id,
                "connection_type": c.connection_type,
                "created_at": c.created_at,
                "source_title": source.title,
                "source_type": source.type,
                "target_title": target.title,
                "target_type": target.type
            })
    return detailed_conns

async def get_connections_by_item_id(db: AsyncSession, item_id: int):
    query = select(models.Connection).where(
        (models.Connection.source_id == item_id) | (models.Connection.target_id == item_id)
    )
    result = await db.execute(query)
    conns = result.scalars().all()
    
    detailed_conns = []
    for c in conns:
        source = await get_item(db, c.source_id)
        target = await get_item(db, c.target_id)
        if source and target:
            detailed_conns.append({
                "id": c.id,
                "source_id": c.source_id,
                "target_id": c.target_id,
                "connection_type": c.connection_type,
                "created_at": c.created_at,
                "source_title": source.title,
                "source_type": source.type,
                "target_title": target.title,
                "target_type": target.type
            })
    return detailed_conns

async def delete_connection(db: AsyncSession, connection_id: int):
    result = await db.execute(select(models.Connection).where(models.Connection.id == connection_id))
    db_conn = result.scalars().first()
    if db_conn:
        await db.delete(db_conn)
        await db.flush()
        return True
    return False

# -- StudyReview Helpers (Spaced Repetition) --
async def get_study_review_by_concept(db: AsyncSession, concept_id: int, user_id: int):
    result = await db.execute(
        select(models.StudyReview).where(
            models.StudyReview.concept_id == concept_id,
            models.StudyReview.user_id == user_id
        )
    )
    return result.scalars().first()

async def create_study_review(db: AsyncSession, concept_id: int, user_id: int):
    existing = await get_study_review_by_concept(db, concept_id, user_id)
    if existing:
        return existing
        
    db_review = models.StudyReview(
        user_id=user_id,
        concept_id=concept_id,
        interval_days=1,
        due_date=datetime.datetime.utcnow() + datetime.timedelta(days=1),
        status="learning"
    )
    db.add(db_review)
    await db.flush()
    return db_review

async def get_due_study_reviews(db: AsyncSession, user_id: int):
    now = datetime.datetime.utcnow()
    result = await db.execute(
        select(models.StudyReview).where(
            models.StudyReview.user_id == user_id,
            models.StudyReview.due_date <= now
        )
    )
    reviews = result.scalars().all()
    
    enriched = []
    for r in reviews:
        concept = await get_item(db, r.concept_id)
        if concept:
            r_dict = {
                "id": r.id,
                "user_id": r.user_id,
                "concept_id": r.concept_id,
                "interval_days": r.interval_days,
                "due_date": r.due_date,
                "last_reviewed_at": r.last_reviewed_at,
                "status": r.status,
                "created_at": r.created_at,
                "concept_title": concept.title,
                "concept_content": concept.content
            }
            enriched.append(r_dict)
    return enriched

async def update_study_review(db: AsyncSession, review_id: int, score: int):
    result = await db.execute(select(models.StudyReview).where(models.StudyReview.id == review_id))
    r = result.scalars().first()
    if not r:
        return None
        
    if score >= 2:
        intervals = {1: 3, 3: 7, 7: 14, 14: 30, 30: 30}
        r.interval_days = intervals.get(r.interval_days, 1)
        if r.interval_days == 30:
            r.status = "learned"
    else:
        r.interval_days = 1
        r.status = "learning"
        
    r.last_reviewed_at = datetime.datetime.utcnow()
    r.due_date = datetime.datetime.utcnow() + datetime.timedelta(days=r.interval_days)
    
    await db.flush()
    return r

