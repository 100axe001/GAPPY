# LifeOS Pod

The Lemma pod that powers LifeOS. Everything here is plain files — import it into any Lemma
org with `lemma pods import ./pod/lifeos`.

## What's inside

| Primitive | Name | What it does |
|---|---|---|
| **Table** | `items` | Tasks, notes, deadlines, study material (unified `type` column). |
| **Table** | `connections` | The Second-Brain graph (related notes, suggested tasks, recurrences). |
| **Table** | `study_reviews` | Spaced-repetition schedule (1→3→7→14→30 days). |
| **Agent** | `note-linker` | On a new note: finds related notes + suggests follow-up tasks. |
| **Agent** | `commitment-parser` | Natural language → structured task (title, due date, priority, category). |
| **Agent** | `study-coach` | Study material → weak topics, revision plan, MCQ practice. |
| **Agent** | `weekly-reviewer` | Open/slipped/stale tasks → a weekly review. |
| **Agent** | `brain-insights` | Recent notes → 3–5 synthesised insights. |
| **Agent** | `email-drafter` | A short brief → a ready-to-send email draft. |
| **Agent** | `chat-assistant` | The Chat tab: POD + web search + connector tools. |
| **Function** | `apply_task` | Writes an approved task into `items`. |
| **Function** | `schedule_review` | Deterministic spaced-repetition scheduler. |
| **Function** | `send_gmail` | Sends an approved email via the Gmail connector. |
| **Workflow** | `commitment-intake` | FORM → **agent** → **human approval** → function writes the task. |
| **Workflow** | `email-draft-send` | **agent** drafts → **human approval** → connector sends. |
| **Schedule** | `morning-briefing` | Daily cron → runs `brain-insights` for the Today view. |

Agents have `output_schema`s and least-privilege `permissions.grants` (each names the exact
tables/connectors it may touch — nothing else).

## Notes

- The column is `owner_id`, not `user_id` — `user_id` is a Lemma-reserved system column.
- A workflow that needs input **starts with a FORM entry node**; `create_run` submits no start
  payload. The app auto-submits the entry form, then the human approves the second form.
- Connector **auth-configs** and **file contents** don't travel in bundles — configure them
  separately (see the repo README + `app/provision.py`).

## Setup / verify

```bash
python app/provision.py            # find-or-create the pod, import this bundle
lemma pods describe lifeos         # inspect what landed
lemma agents chat commitment-parser "call the dentist next Tuesday"   # smoke test
lemma pods export ./exported lifeos   # round-trips back to files
```
