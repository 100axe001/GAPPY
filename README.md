# LifeOS — Personal AI Command Centre

LifeOS is a full-stack personal AI command centre — a unified task/deadline tracker, an **AI Second Brain** that links thoughts and extracts actions, an **AI Learning Companion** that builds study material and schedules spaced revisions, a **Chat** assistant with real tools, and a **Today View** that surfaces your day.

**It is a real Lemma pod, not a wrapper.** LifeOS is built directly on the **[Lemma platform](https://github.com/lemma-work/lemma-platform)** primitives:

- **Pod datastore** — your tasks, notes, and review schedule live as rows in the `lifeos` pod's `items` / `connections` / `study_reviews` tables (not a private database).
- **Purpose-built agents** — `note-linker`, `commitment-parser`, `study-coach`, `weekly-reviewer`, `brain-insights`, `email-drafter`, and a tool-using `chat-assistant`, each with its own output schema and least-privilege grants.
- **Workflows with human approval** — `commitment-intake` (agent → **you approve** → task) and `email-draft-send` (agent drafts → **you approve** → Gmail sends). This is the Lemma "agent works, structured output lands, a human decides" shape.
- **Functions** for deterministic logic, a **schedule** for the daily briefing, and the live **connector catalog** (Gmail, Calendar, Drive, Slack, Jira, …) for real integrations.

The whole pod is a directory of files under [`pod/lifeos/`](pod/lifeos/) — inspect it, export it, or import it into any Lemma org.

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

- **Docker** running
- **Lemma local stack** installed and running (the `lemma-stack` tool + `lemma` CLI), authenticated with `lemma auth login`
- **Python 3.11+** on your host machine

### Step 0 — Point Lemma at a model, connectors, and provision the pod *(one-time)*

Lemma agents need a model provider, and the connector catalog must be imported once:

```bash
# 1. Model backend (agents can't run without this)
lemma-stack config set LEMMA_DEFAULT_MODEL_TYPE openai_compat
lemma-stack config set LEMMA_OPENAI_API_KEY sk-...
# 2. (optional) extra connectors via Composio — native Gmail/Calendar/Slack/… work without it
lemma-stack config set COMPOSIO_API_KEY <composio-api-key>
lemma-stack restart

# 3. Import the native connector catalog (Gmail, Calendar, Drive, Slack, Jira, …)
docker exec lemma-local-backend python scripts/import_connector_catalog.py

# 4. Create the pod and import the LifeOS bundle
python app/provision.py            # prints LEMMA_ORG_ID / LEMMA_POD_ID
```

`docker-compose.yml` already defaults `LEMMA_ORG_ID` / `LEMMA_POD_ID`; override them via env if provisioning printed different ids.

> **Connecting an integration** (OAuth) needs credentials for that app — either a Composio API key, or Google OAuth client credentials for the native Google connectors. Without them the catalog still shows live and the connect button reports honestly what's missing.

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

Seed sample data (runs against the live app, so notes trigger the `note-linker` agent):

```bash
python app/seed.py
```

Login credentials:

| Field    | Value              |
|----------|--------------------|
| Email    | `demo@lifeos.dev`  |
| Password | `password`         |

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

### Chat (AI Assistant with Tools)
A clean, standard chat experience with a conversation sidebar (rename + tag any chat) on the left and the message thread on the right. The assistant is backed by a configurable LLM and can **use your integrations as tools**:

- **Regex intent recognition** inspects each message and activates only the relevant tools for that turn — integrations are never all-on at once. Calendar wording surfaces the Google Calendar tools, "search the web…" surfaces Web Search, "email/inbox" surfaces the IMAP/SMTP tools, "remind me…" surfaces task creation, and "what did I tell you…" surfaces Second Brain recall.
- The LLM runs a tool loop: it calls a tool, reads the result, then answers. Tools used in a reply are shown as chips on the message.
- **Automatic memory (Second Brain):** after each exchange the assistant decides on its own whether anything durable (a preference, fact, project, or commitment) is worth keeping, and silently saves it as a note. Saved memories appear beneath the reply and become recall context for future chats.

### Settings
Configure everything from one encrypted panel (secrets are stored encrypted and never shown back):
- **AI Model** — choose Lemma (local, no key), Anthropic (Claude), or OpenAI, with an optional model override.
- **Web Search** — pick Tavily (API key) or a self-hosted SearXNG (instance URL).
- **Email** — Gmail/IMAP/SMTP via a Google **App Password** (test the connection with one click).
- **Memory** — toggle automatic Second Brain saving.

### Web Search
A dedicated Web Search pane lives in the Search tab (Tavily or SearXNG), and the same capability is available to the chat assistant as a tool.

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
