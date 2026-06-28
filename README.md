# LifeOS — Personal AI Command Centre

LifeOS is a full-stack personal AI-powered command centre designed to help you close every open loop in your life. It features a unified task/deadline tracker, an **AI Second Brain** that links thoughts and extracts actions, an **AI Learning Companion** that automates study materials and schedules revisions, and a **Today View** that surfaces your most important work every morning.

Built as an extension layer on top of the **[Lemma SDK](https://github.com/lemma-work/lemma-platform)** — all semantic search, RAG, and LLM calls are routed through your locally running Lemma container stack.

---

## Folder Structure

```text
/shiptohire
├── lemma-platform/    # Lemma SDK (do not modify)
├── app/               # LifeOS Application Layer
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── backend/       # FastAPI Backend (models, CRUD, AI helpers)
│   ├── frontend/      # Vanilla JS + CSS web UI
│   └── seed.py        # Seeds the DB with sample data & uploads PDF
├── docker-compose.yml # Orchestrates LifeOS app + Postgres
├── .gitignore
└── README.md
```

---

## Running Locally

### Prerequisites

- **Docker Desktop** installed and running
- **Lemma local stack** already running (provides the AI/LLM backend on port `8000`)
- **Python 3.11+** on your host machine

---

### Step 1 — Create a virtual environment

```bash
cd /path/to/shiptohire

python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

pip install -r app/requirements.txt
```

---

### Step 2 — Start the database

```bash
docker compose up -d lifeos-db
```

Wait ~5 seconds for Postgres to finish booting.

---

### Step 3 — Seed the database *(first time only)*

Generates a sample Machine Learning study PDF, uploads it to Lemma, and creates 5 tasks and 3 notes in the database:

```bash
python app/seed.py
```

---

### Step 4 — Build & start the application

```bash
docker compose up -d
```

> **After any code change**, rebuild before restarting so the container picks up your edits:
> ```bash
> docker compose build lifeos-app && docker compose up -d lifeos-app
> ```

---

### Step 5 — Open the app

**http://localhost:8081**

Pre-seeded login credentials:

| Field    | Value                          |
|----------|--------------------------------|
| Email    | `srivastavaaarush25@gmail.com` |
| Password | `password`                     |

---

## Ports at a Glance

| Service             | Port   |
|---------------------|--------|
| LifeOS web app      | `8081` |
| LifeOS Postgres     | `5433` |
| Lemma backend (SDK) | `8000` |

> **Docker network note:** `docker-compose.yml` uses an external network called `lemma-local-net`. This network is created automatically when you start the Lemma stack. If you see a network error, create it manually:
> ```bash
> docker network create lemma-local-net
> ```

---

## Feature Walkthrough

### Today View (landing page)
The default screen aggregates your day: overdue tasks, items due today, spaced-repetition review queue, stale follow-ups, and an AI brain insight. The greeting updates based on the time of day.

### Life Ops
- **Commitment Inbox** — drop any natural language commitment ("call dentist next Thursday", "submit assignment by Friday") and AI parses it into a structured task with deadline, priority, and category. Press Enter to trigger parsing.
- **Task Board** — tasks grouped as To Do / In Progress / Completed, with colour-coded left borders for priority (red = high, amber = medium, green = low).
- **Follow-up Tracker** — mark any task as "waiting on someone" from its detail view; stale follow-ups surface on the Today page.
- **Weekly Review** — click the ✦ Weekly Review button to get an AI summary of closed loops, slipped items, and what needs attention. Reschedule, snooze, or delete items directly from the modal.

### Second Brain
Save notes, links, and raw ideas. After saving, the AI:
- Finds semantically related notes and creates connections
- Suggests follow-up tasks
- Logs an **AI Origin Trace** explaining its reasoning

Use the split-pane editor (left = note list, right = full editor). Select text to reveal the floating Bold / Italic / Link toolbar. Check multiple notes in the list then use **Draft Generator** to compile them into an essay, plan, email, or summary.

### Learning Companion
- **Upload Study Material** — PDF or `.txt` files are indexed via Lemma RAG.
- **Active Study Room** — select a resource, optionally describe what you're confused about, and click **Generate Practice** for AI-generated multiple-choice questions.
- **Spaced Repetition Queue** — after completing a practice quiz, weak topics are scheduled for review using a spaced repetition algorithm. Due reviews appear on the Today page.
- **Pomodoro Timer** — 25-minute focus timer with a post-session AI debrief that recommends your next study focus.

### Search
Full-text search across all tasks, notes, and study materials.

---

## Security Notes

- Never commit `.env` files — they are git-ignored at the root level.
- The `slack.json` OpenAPI spec (a large generated file containing Slack's own sample tokens) is also git-ignored.
- Store all API keys as environment variables; see `docker-compose.yml` for the expected variable names.
