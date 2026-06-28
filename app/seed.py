import os
import asyncio
import datetime
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from backend.database import Base
from backend.models import User, Item, Connection
from backend.auth import get_password_hash
from backend.sdk_client import get_lemma_pod

DB_URL = "postgresql+asyncpg://postgres:postgres@localhost:5433/lifeos"

def generate_pdf(path: str):
    """Generates a valid study PDF for the learning companion module using ReportLab."""
    c = canvas.Canvas(path, pagesize=letter)
    
    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, 750, "Introduction to Machine Learning (Study Guide)")
    
    # Subtitle
    c.setFont("Helvetica-Oblique", 12)
    c.drawString(100, 730, "A Comprehensive Overview for LifeOS Learning companion")
    
    # Text content
    c.setFont("Helvetica", 10)
    y = 690
    
    paragraphs = [
        "Topic 1: Supervised Learning concepts",
        "Supervised learning is the machine learning task of learning a function that maps an input to an output based on example input-output pairs. It infers a function from labeled training data consisting of a set of training examples. A supervised learning algorithm analyzes the training data and produces an inferred function, which can be used for mapping new examples.",
        "",
        "Topic 2: Unsupervised Learning concepts",
        "Unsupervised learning is a type of algorithm that learns patterns from untagged data. The hope is that through mimicry, which is an important mode of learning in people, the machine is forced to build a compact internal representation of its world. In contrast to supervised learning, unsupervised learning algorithms are left to find structures and patterns in data without any guidance.",
        "",
        "Topic 3: Overfitting and Underfitting",
        "Overfitting is a concept in machine learning that occurs when a statistical model fits its training data too well. The training algorithm adjusts the weights to minimize the loss for the training set, but it captures noise and anomalies rather than the underlying data distribution. Consequently, the model performs poorly on unseen validation data.",
        "Underfitting occurs when a machine learning model cannot capture the underlying trend of the data. It is often the result of an excessively simple model (e.g. fitting a linear model to a non-linear dataset). Underfit models show low accuracy on both training and test data.",
        "",
        "Practice review point:",
        "Make sure to study the trade-off between Bias and Variance, which directly relates to overfitting and underfitting."
    ]
    
    for p in paragraphs:
        if not p:
            y -= 15
            continue
        
        if p.startswith("Topic") or p.startswith("Practice"):
            c.setFont("Helvetica-Bold", 12)
            c.drawString(100, y, p)
            y -= 20
        else:
            c.setFont("Helvetica", 10)
            # Simple text wrap
            words = p.split(" ")
            line = ""
            for word in words:
                if len(line + word) > 85:
                    c.drawString(100, y, line)
                    y -= 15
                    line = word + " "
                else:
                    line += word + " "
            if line:
                c.drawString(100, y, line)
                y -= 15
        
        # Guard against page overflow
        if y < 80:
            c.showPage()
            c.setFont("Helvetica", 10)
            y = 750
            
    c.save()
    print(f"Generated sample study PDF: {path}")

async def seed_data():
    print("Connecting to database at:", DB_URL)
    engine = create_async_engine(DB_URL, echo=False)
    AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    
    # 1. Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    async with AsyncSessionLocal() as db:
        # 2. Check if default user exists
        email = "srivastavaaarush25@gmail.com"
        user = await db.run_sync(lambda s: s.query(User).filter_by(email=email).first())
        if not user:
            hashed_pw = get_password_hash("password")
            user = User(email=email, hashed_password=hashed_pw)
            db.add(user)
            await db.flush()
            print(f"Created default user: {email} with password: 'password'")
        else:
            print(f"User {email} already exists.")
            
        # 3. Clear existing items
        await db.run_sync(lambda s: s.query(Connection).delete())
        await db.run_sync(lambda s: s.query(Item).delete())
        await db.flush()
        
        # 4. Insert 5 Tasks
        tasks_data = [
            {
                "type": "task",
                "title": "Verify shipping details for order #1042",
                "content": "Verify address details and shipping method for the international order before processing.",
                "status": "todo",
                "priority": "high",
                "due_date": datetime.datetime.utcnow() + datetime.timedelta(days=1)
            },
            {
                "type": "task",
                "title": "Review contract terms with law firm",
                "content": "Read through clauses 4 and 7 about intellectual property ownership and confidentiality.",
                "status": "in_progress",
                "priority": "medium",
                "due_date": datetime.datetime.utcnow() + datetime.timedelta(days=4)
            },
            {
                "type": "task",
                "title": "Call candidate Maya for interview feedback",
                "content": "Call Maya at 2:00 PM to offer the position and discuss compensation details.",
                "status": "done",
                "priority": "low",
                "due_date": datetime.datetime.utcnow() - datetime.timedelta(days=1)
            },
            {
                "type": "task",
                "title": "Prepare presentation slides for board meeting",
                "content": "Gather Q2 financial metrics and project roadmap slides for the quarterly update.",
                "status": "todo",
                "priority": "high",
                "due_date": datetime.datetime.utcnow() + datetime.timedelta(days=2)
            },
            {
                "type": "task",
                "title": "Renew annual gym membership",
                "content": "Gym subscription renewal is due. Need to process before the discount code expires.",
                "status": "todo",
                "priority": "low",
                "due_date": datetime.datetime.utcnow() - datetime.timedelta(days=2)
            }
        ]
        
        created_tasks = []
        for t in tasks_data:
            item = Item(**t)
            db.add(item)
            created_tasks.append(item)
            
        # 5. Insert 3 Notes
        notes_data = [
            {
                "type": "note",
                "title": "Idea for AI-generated reports",
                "content": "We can build an agent that runs every night, scans our databases, and creates a report. It should email this as a PDF or update the LifeOS dashboard.",
                "status": "todo",
                "metadata_json": {}
            },
            {
                "type": "note",
                "title": "Feedback on candidate Maya",
                "content": "Maya had strong coding credentials and resolved the architectural case study quickly. She is highly recommended for the Lead Developer role.",
                "status": "todo",
                "metadata_json": {}
            },
            {
                "type": "note",
                "title": "Notes on Gym subscription",
                "content": "The gym membership is about to expire. Renewing before the end of the month gives a 10% loyalty discount.",
                "status": "todo",
                "metadata_json": {}
            }
        ]
        
        created_notes = []
        for n in notes_data:
            item = Item(**n)
            db.add(item)
            created_notes.append(item)
            
        await db.flush()
        print(f"Seeded {len(created_tasks)} tasks and {len(created_notes)} notes.")
        
        # Link "Feedback on candidate Maya" (Note ID) to "Call candidate Maya for interview feedback" (Task ID)
        maya_note = next(n for n in created_notes if "Maya" in n.title)
        maya_task = next(t for t in created_tasks if "Maya" in t.title)
        conn1 = Connection(source_id=maya_note.id, target_id=maya_task.id, connection_type="relates_to")
        db.add(conn1)
        
        # Link "Notes on Gym subscription" (Note ID) to "Renew annual gym membership" (Task ID)
        gym_note = next(n for n in created_notes if "Gym" in n.title)
        gym_task = next(t for t in created_tasks if "gym" in t.title.lower())
        conn2 = Connection(source_id=gym_note.id, target_id=gym_task.id, connection_type="relates_to")
        db.add(conn2)
        
        # 6. Generate & Upload study PDF to Lemma
        os.makedirs("uploads", exist_ok=True)
        pdf_filename = "machine_learning_intro.pdf"
        pdf_path = os.path.join("uploads", pdf_filename)
        generate_pdf(pdf_path)
        
        print("Uploading PDF to Lemma files system...")
        try:
            pod = get_lemma_pod()
            # Ensure folder
            try:
                pod.files.create_folder("/learning", description="Learning module uploads")
            except Exception:
                pass
                
            res = pod.files.upload(
                local_path=pdf_path,
                path=f"/learning/{pdf_filename}",
                search_enabled=True
            )
            
            # Save Study Material Item in DB
            db_pdf_item = Item(
                type="study_material",
                title="Introduction to Machine Learning",
                content=f"/learning/{pdf_filename}",
                status="todo",
                metadata_json={
                    "local_path": pdf_path,
                    "lemma_path": f"/learning/{pdf_filename}",
                    "upload_response": res.to_dict()
                }
            )
            db.add(db_pdf_item)
            await db.flush()
            print("Successfully uploaded PDF to Lemma and created DB reference!")
        except Exception as e:
            print("WARNING: Could not upload PDF to Lemma (is the Lemma API reachable?):", e)
            print("Mocking DB entry for study material...")
            db_pdf_item = Item(
                type="study_material",
                title="Introduction to Machine Learning",
                content=f"/learning/{pdf_filename}",
                status="todo",
                metadata_json={
                    "local_path": pdf_path,
                    "lemma_path": f"/learning/{pdf_filename}",
                    "upload_response": {"status": "MOCKED"}
                }
            )
            db.add(db_pdf_item)
            await db.flush()
            
        await db.commit()
        print("Seeding completed successfully!")
        
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(seed_data())
