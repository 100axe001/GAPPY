"""
AI helpers — every call runs a purpose-built Lemma agent from the `lifeos` pod
(note-linker, commitment-parser, study-coach, weekly-reviewer, brain-insights,
email-drafter, chat-assistant), replacing the single generic "hello" agent the
original code assumed. Blocking SDK calls are run off the event loop.

Agent output is normalised back into the shapes the endpoints/frontend already expect,
so the rest of the app is untouched.
"""
import json
import re
import asyncio
import datetime
from typing import List, Dict, Any, Tuple

from .sdk_client import get_lemma_pod, run_sync


def extract_json(text: str) -> Dict[str, Any]:
    """Robustly extract a JSON object from text (handles ```json fences and prose)."""
    if not text:
        raise ValueError("empty text")
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL | re.IGNORECASE)
    if match:
        try:
            return json.loads(match.group(1).strip())
        except Exception:
            pass
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1:
        try:
            return json.loads(text[start:end + 1].strip())
        except Exception:
            pass
    raise ValueError(f"Could not extract JSON from text: {text[:200]}")


def _agent_reply_text(pod, conv_id: str) -> str:
    messages = pod.conversations.messages(conv_id).to_dict()["items"]
    for msg in reversed(messages):
        if msg.get("role") == "assistant" and msg.get("text"):
            return msg["text"]
    raise RuntimeError("No assistant response text found")


async def run_agent_text(agent_name: str, prompt: str, timeout_s: int = 60) -> str:
    """Run an agent and return its final assistant text."""
    pod = get_lemma_pod()
    conv = await run_sync(pod.agents.run, agent_name, prompt)
    conv_id = str(conv.id)
    for _ in range(timeout_s * 2):
        detail = await run_sync(pod.conversations.get, conv_id)
        if getattr(detail, "status", None) in ("COMPLETED", "FAILED", "STOPPED"):
            break
        await asyncio.sleep(0.5)
    return await run_sync(_agent_reply_text, pod, conv_id)


def _unwrap_output(data: Dict[str, Any]) -> Dict[str, Any]:
    """Agents with an output_schema return a {tool_name, args:{output:...}} envelope."""
    if not isinstance(data, dict):
        return {}
    if isinstance(data.get("args"), dict) and isinstance(data["args"].get("output"), dict):
        return data["args"]["output"]
    if isinstance(data.get("output"), dict):
        return data["output"]
    return data


async def run_agent_structured(agent_name: str, prompt: str) -> Dict[str, Any]:
    """Run a structured (output_schema) agent and return its parsed output object."""
    text = await run_agent_text(agent_name, prompt)
    return _unwrap_output(extract_json(text))


# ------------------------------------------------------------ Second Brain

async def analyze_note_and_suggest_links(new_note, existing_notes: List) -> Dict[str, Any]:
    notes_list_str = ""
    for note in existing_notes:
        snippet = (note.content[:150] + "...") if note.content else ""
        notes_list_str += f"- [ID: {note.id}] Title: {note.title} (Snippet: {snippet})\n"

    prompt = f"""A new note was just saved.
Title: {new_note.title}
Content: {new_note.content or 'No content provided.'}

Existing notes:
{notes_list_str or 'No existing notes.'}

Find related existing notes (use their exact ID) and suggest any follow-up tasks."""

    try:
        parsed = await run_agent_structured("note-linker", prompt)
        parsed.setdefault("connections", [])
        parsed.setdefault("suggested_tasks", [])
        parsed["trace"] = {
            "agent": "note-linker",
            "prompt_summary": f"Linked note '{new_note.title}' against {len(existing_notes)} notes.",
        }
        return parsed
    except Exception as e:
        return {"connections": [], "suggested_tasks": [], "error": str(e), "trace": {"error": str(e)}}


async def surface_brain_insights(notes: List) -> List[Dict[str, Any]]:
    notes_str = "\n".join([f"- [ID: {n.id}] {n.title}: {(n.content or '')[:200]}" for n in notes])
    prompt = f"""Review these notes from the past 30 days and surface the key patterns:
{notes_str or 'No notes recorded.'}"""
    try:
        out = await run_agent_structured("brain-insights", prompt)
        insights = out.get("insights", [])
        # Normalise to the {title, description, action, source_note_ids} shape the UI expects.
        return [{
            "title": i.get("title", "Insight"),
            "description": i.get("detail") or i.get("description", ""),
            "action": i.get("action", "expand"),
            "source_note_ids": i.get("source_note_ids", []),
        } for i in insights]
    except Exception:
        return []


async def generate_draft_from_notes(notes: List, format_type: str) -> str:
    notes_str = "\n---\n".join([f"Note: {n.title}\nContent:\n{n.content}" for n in notes])
    prompt = f"""Combine the following notes into a polished {format_type}. Write the {format_type}
directly with no preamble like "Here is your draft".

NOTES:
{notes_str}"""
    try:
        return await run_agent_text("chat-assistant", prompt)
    except Exception as e:
        return f"Failed to generate draft: {str(e)}"


# --------------------------------------------------------------- Life Ops

async def parse_commitment_inbox(text: str) -> Dict[str, Any]:
    today = datetime.date.today().strftime("%Y-%m-%d")
    prompt = f"Today is {today}. Parse this commitment into a task: \"{text}\""
    try:
        out = await run_agent_structured("commitment-parser", prompt)
        return {
            "title": out.get("title", text),
            "content": out.get("content", ""),
            "due_date": out.get("due_date") or None,
            "priority": out.get("priority", "medium"),
            "category": out.get("category", "personal"),
        }
    except Exception as e:
        return {"title": text, "due_date": None, "priority": "medium",
                "category": "personal", "error": str(e)}


async def generate_weekly_review_summary(open_tasks: List, slipped_tasks: List,
                                         stale_followups: List) -> Dict[str, Any]:
    def fmt(tasks, label):
        return "\n".join([f"- [ID: {t.id}] {t.title} ({label})" for t in tasks]) or "None"
    digest = f"""OPEN TASKS:
{fmt(open_tasks, 'open')}

SLIPPED / OVERDUE:
{fmt(slipped_tasks, 'overdue')}

STALE FOLLOW-UPS:
{fmt(stale_followups, 'waiting')}"""
    try:
        out = await run_agent_structured("weekly-reviewer", digest)
        return {
            "summary": out.get("summary_markdown") or out.get("summary", ""),
            "closed_loops": out.get("closed_loops", []),
            "slipped": out.get("slipped", []),
            "needs_attention": out.get("needs_attention", []),
            "attention_item_ids": [],
        }
    except Exception as e:
        return {"summary": f"Failed to generate summary: {str(e)}", "attention_item_ids": []}


# --------------------------------------------------- Learning Companion

def _extract_text(local_path: str) -> str:
    """Best-effort text extraction for study material (txt / pdf)."""
    lower = local_path.lower()
    if lower.endswith((".txt", ".md")):
        try:
            with open(local_path, "r", errors="replace") as f:
                return f.read()
        except Exception:
            return ""
    if lower.endswith(".pdf"):
        try:
            from pypdf import PdfReader
            reader = PdfReader(local_path)
            return "\n".join((page.extract_text() or "") for page in reader.pages)
        except Exception:
            return ""
    try:
        with open(local_path, "r", errors="replace") as f:
            return f.read()
    except Exception:
        return ""


async def upload_learning_file_to_lemma(filename: str, local_path: str) -> Dict[str, Any]:
    """Extract text from the uploaded study file (local; the SDK build here has no file RAG)."""
    text = await run_sync(_extract_text, local_path)
    if not text.strip():
        return {"error": "Could not extract any text from this file."}
    return {"chars": len(text), "extracted_text": text[:20000]}


async def generate_study_plan_and_questions(
    material_title: str, material_context: str, self_reported_confusion: str = ""
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    context = (material_context or "")[:6000]
    prompt = f"""Study material: {material_title}
Confusion: {self_reported_confusion or 'None specified.'}

Relevant content:
{context}"""
    try:
        out = await run_agent_structured("study-coach", prompt)
        # Adapt the study-coach schema to the shapes the endpoint stores.
        weak = [{"topic": t, "reason": ""} if isinstance(t, str)
                else {"topic": t.get("topic", ""), "reason": t.get("reason", "")}
                for t in out.get("weak_topics", [])]
        revision = [{
            "title": rp.get("topic", "Revise"),
            "content": rp.get("action", ""),
            "due_date": None,
            "priority": "medium",
        } for rp in out.get("revision_plan", [])]
        questions = []
        for q in out.get("practice_questions", []):
            opts = q.get("options", [])
            ai = q.get("answer_index", 0)
            questions.append({
                "question": q.get("question", ""),
                "options": opts,
                "correct_answer": opts[ai] if isinstance(ai, int) and 0 <= ai < len(opts) else (opts[0] if opts else ""),
                "explanation": q.get("explanation", ""),
                "topic": q.get("topic", ""),
            })
        return {"weak_topics": weak, "revision_plan": revision, "practice_questions": questions}, []
    except Exception as e:
        return {"weak_topics": [], "revision_plan": [], "practice_questions": [], "error": str(e)}, []


async def score_test_and_map_topics(test_results: List[Dict[str, Any]]) -> Dict[str, Any]:
    results_str = ""
    for idx, r in enumerate(test_results):
        results_str += (f"\nQ{idx+1}: {r.get('question')}\nSelected: {r.get('selected')}\n"
                        f"Correct: {r.get('correct')}\nTopic: {r.get('topic', 'unknown')}\n")
    prompt = f"""Grade this practice test and return ONLY JSON with this schema:
{{"topic_strength":[{{"topic":"<name>","score":"<c>/<n>","status":"weak"|"strong"}}],
"suggested_revisions":[{{"title":"<t>","content":"<c>","priority":"high"|"medium"|"low","due_date":"YYYY-MM-DD"}}]}}

RESULTS:{results_str}"""
    try:
        return _unwrap_output(extract_json(await run_agent_text("chat-assistant", prompt)))
    except Exception as e:
        return {"topic_strength": [], "suggested_revisions": [], "error": str(e)}


async def generate_spaced_repetition_quiz(concept_title: str, concept_content: str) -> List[Dict[str, Any]]:
    prompt = f"""Write a 3-question multiple-choice quiz on "{concept_title}".
Context: {concept_content or 'None'}
Return ONLY JSON: {{"questions":[{{"question":"..","options":["..",".."],"correct_answer":"..","explanation":".."}}]}}"""
    try:
        data = _unwrap_output(extract_json(await run_agent_text("chat-assistant", prompt)))
        return data.get("questions", [])
    except Exception:
        return []


async def generate_study_debrief_insights(summary: str, confusion: str) -> Dict[str, Any]:
    prompt = f"""A focus session just finished.
Covered: {summary}
Struggles: {confusion or 'None reported.'}
Return ONLY JSON: {{"feedback":"..","weak_topics":[{{"topic":"..","reason":".."}}],"suggested_next_focus":".."}}"""
    try:
        return _unwrap_output(extract_json(await run_agent_text("chat-assistant", prompt)))
    except Exception as e:
        return {"feedback": "Great focus session! Keep going.", "weak_topics": [],
                "suggested_next_focus": "Continue current topic.", "error": str(e)}
