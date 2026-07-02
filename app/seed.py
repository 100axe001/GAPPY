"""
Seed LifeOS with demo data by driving the running app's API.

Because LifeOS is now Lemma-native (tasks/notes live in the pod datastore), seeding goes
through the real endpoints — so notes trigger the note-linker agent and the study PDF is
processed by the study pipeline, exactly as in normal use.

Run the app first (docker compose up -d), then:
    python app/seed.py
"""
import os
import datetime
import httpx
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

BASE = os.getenv("LIFEOS_URL", "http://localhost:8081")
EMAIL = os.getenv("SEED_EMAIL", "demo@lifeos.dev")
PASSWORD = os.getenv("SEED_PASSWORD", "password")


def generate_pdf(path: str):
    c = canvas.Canvas(path, pagesize=letter)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, 750, "Introduction to Machine Learning (Study Guide)")
    c.setFont("Helvetica", 10)
    y = 700
    paragraphs = [
        "Topic 1: Supervised Learning",
        "Supervised learning maps inputs to outputs from labeled training examples. The algorithm "
        "analyzes labeled data and produces an inferred function for mapping new examples.",
        "Topic 2: Unsupervised Learning",
        "Unsupervised learning finds patterns in unlabeled data, building a compact internal "
        "representation without guidance.",
        "Topic 3: Overfitting and Underfitting",
        "Overfitting occurs when a model fits training data too well, capturing noise and failing "
        "to generalize. Underfitting occurs when a model is too simple to capture the trend. "
        "Study the bias-variance trade-off, which underlies both.",
    ]
    for p in paragraphs:
        bold = p.startswith("Topic")
        c.setFont("Helvetica-Bold" if bold else "Helvetica", 12 if bold else 10)
        for i in range(0, len(p), 90):
            c.drawString(100, y, p[i:i + 90]); y -= 15
        y -= 6
        if y < 80:
            c.showPage(); y = 750
    c.save()
    print(f"Generated study PDF: {path}")


def main():
    with httpx.Client(base_url=BASE, timeout=90) as cl:
        cl.post("/api/auth/signup", json={"email": EMAIL, "password": PASSWORD})
        tok = cl.post("/api/auth/login", json={"email": EMAIL, "password": PASSWORD}).json()["access_token"]
        h = {"Authorization": f"Bearer {tok}"}

        now = datetime.datetime.utcnow()
        tasks = [
            ("Prepare presentation slides for board meeting", "high", 2),
            ("Review contract terms with the law firm", "medium", 4),
            ("Renew annual gym membership", "low", -2),
            ("Verify shipping details for order #1042", "high", 1),
        ]
        for title, prio, days in tasks:
            cl.post("/api/items", headers=h, json={
                "type": "task", "title": title, "priority": prio, "status": "todo",
                "due_date": (now + datetime.timedelta(days=days)).isoformat(),
            })
        print(f"Seeded {len(tasks)} tasks.")

        notes = [
            ("Idea for AI-generated reports",
             "Build an agent that runs nightly, scans our data, and emails a PDF summary or updates the dashboard."),
            ("Feedback on candidate Maya",
             "Maya had strong coding credentials and resolved the case study quickly. Recommend her for the Lead Developer role — need to call her."),
        ]
        for title, content in notes:
            print(f"Creating note '{title}' (runs note-linker agent)…")
            cl.post("/api/items", headers=h, json={"type": "note", "title": title, "content": content})
        print(f"Seeded {len(notes)} notes.")

        os.makedirs("uploads", exist_ok=True)
        pdf_path = os.path.join("uploads", "machine_learning_intro.pdf")
        generate_pdf(pdf_path)
        with open(pdf_path, "rb") as f:
            r = cl.post("/api/learning/upload", headers=h,
                        files={"file": ("machine_learning_intro.pdf", f, "application/pdf")})
        print("Uploaded study material:", "ok" if r.status_code == 200 else r.text[:200])
        print("Seeding complete. Log in at", BASE, "with", EMAIL, "/", PASSWORD)


if __name__ == "__main__":
    main()
