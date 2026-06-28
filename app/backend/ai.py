import json
import re
import asyncio
import datetime
from typing import List, Dict, Any, Tuple
from .sdk_client import get_lemma_pod
from . import models


def extract_json(text: str) -> Dict[str, Any]:
    """Robustly extracts and parses JSON from text, even if wrapped in markdown code blocks."""
    # Find block code if present
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL | re.IGNORECASE)
    if match:
        try:
            return json.loads(match.group(1).strip())
        except Exception:
            pass
            
    # Try finding the first '{' and last '}'
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1:
        try:
            return json.loads(text[start:end+1].strip())
        except Exception:
            pass
            
    # Fallback to raising exception
    raise ValueError(f"Could not extract JSON from text: {text}")

async def run_agent_until_completed(pod, agent_name: str, prompt: str) -> str:
    """Runs a Lemma agent and polls until completed, returning the latest text response."""
    conv = pod.agents.run(agent_name, prompt)
    conv_id = str(conv.id)
    
    # Poll for completion
    for _ in range(60): # 30 seconds max timeout
        detail = pod.conversations.get(conv_id)
        if detail.status in ("COMPLETED", "FAILED", "STOPPED"):
            break
        await asyncio.sleep(0.5)
        
    messages = pod.conversations.messages(conv_id).to_dict()["items"]
    
    # Fetch the assistant's latest text response
    for msg in reversed(messages):
        if msg.get("role") == "assistant" and msg.get("text"):
            return msg["text"]
            
    raise RuntimeError("No response text found from the agent")

async def analyze_note_and_suggest_links(new_note: models.Item, existing_notes: List[models.Item]) -> Dict[str, Any]:
    """Uses the Lemma agent to analyze a new note, link related items, and suggest tasks."""
    pod = get_lemma_pod()
    
    notes_list_str = ""
    for note in existing_notes:
        snippet = note.content[:150] + "..." if note.content else ""
        notes_list_str += f"- [ID: {note.id}] Title: {note.title} (Snippet: {snippet})\n"
        
    prompt = f"""You are the Second Brain assistant for LifeOS. 
We have a new note:
Title: {new_note.title}
Content: {new_note.content or 'No content provided.'}

Here is a list of existing notes:
{notes_list_str or 'No existing notes.'}

Identify if the new note relates to any existing notes. If it does, specify the target ID and connection_type (must be 'relates_to').
Also, suggest if there are any action items/tasks that should be created from this note. Return them as a list of suggested tasks with a title, content, priority (high, medium, or low), and optional due_date (in YYYY-MM-DD format).

Return your output ONLY as a JSON block with the following schema:
{{
  "connections": [
    {{"target_id": <int>, "connection_type": "relates_to", "reason": "<reason explanation>"}}
  ],
  "suggested_tasks": [
    {{"title": "<task title>", "content": "<description>", "priority": "high"|"medium"|"low", "due_date": "YYYY-MM-DD"|null}}
  ]
}}
"""
    
    try:
        response_text = await run_agent_until_completed(pod, "hello", prompt)
        parsed_data = extract_json(response_text)
        # Append explanation trace metadata
        parsed_data["trace"] = {
            "agent": "hello",
            "prompt_summary": f"Analyzed relationship of note '{new_note.title}' with {len(existing_notes)} notes.",
            "raw_response": response_text
        }
        return parsed_data
    except Exception as e:
        return {
            "connections": [],
            "suggested_tasks": [],
            "error": str(e),
            "trace": {"error": str(e)}
        }

async def upload_learning_file_to_lemma(filename: str, local_path: str) -> Dict[str, Any]:
    """Uploads a PDF or text file to Lemma files system for indexing."""
    pod = get_lemma_pod()
    # Upload under `/learning` folder
    try:
        pod.files.create_folder("/learning", description="Learning module uploads")
    except Exception:
        # Folder might already exist, safe to ignore
        pass
        
    try:
        res = pod.files.upload(
            local_path=local_path,
            path=f"/learning/{filename}",
            search_enabled=True
        )
        return res.to_dict()
    except Exception as e:
        return {"error": str(e)}

async def generate_study_plan_and_questions(
    material_title: str, 
    material_path: str,
    self_reported_confusion: str = ""
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """Performs semantic search via Lemma for RAG, then generates weak topics, practice questions, and study plans."""
    pod = get_lemma_pod()
    
    # 1. RAG Search
    # Search document contents in Lemma to pull context
    search_query = self_reported_confusion or f"overview of {material_title}"
    search_results = []
    context_chunks = []
    
    try:
        search_res = pod.files.search(
            query=search_query,
            scope_path=material_path,
            search_method="HYBRID"
        ).to_dict()
        
        # Extract matches
        items = search_res.get("items", [])
        for item in items[:5]: # Take top 5 context chunks
            chunk_text = item.get("text", "")
            context_chunks.append(chunk_text)
            search_results.append({
                "path": item.get("path"),
                "snippet": chunk_text[:200] + "...",
                "score": item.get("score")
            })
    except Exception as e:
        # If search fails (e.g. index not completed yet), fallback to downloading raw converted markdown
        try:
            md_bytes = pod.files.download_markdown(material_path)
            fallback_text = md_bytes.decode("utf-8", errors="replace")[:4000]
            context_chunks.append(fallback_text)
            search_results.append({
                "path": material_path,
                "snippet": "Fallback full document text extraction (first 4000 chars)",
                "score": 1.0
            })
        except Exception as inner_e:
            context_chunks.append(f"Fallback: could not retrieve document content: {str(inner_e)}")
            
    context_str = "\n---\n".join(context_chunks)
    
    prompt = f"""You are the Learning Companion assistant for LifeOS.
Here is the context retrieved from the study material '{material_title}':
{context_str}

User reported confusion or focal point: {self_reported_confusion or 'None specified.'}

Please do the following:
1. Identify the weak/confusing topics based on the context and the user's reported confusion.
2. Generate a revision plan containing actionable steps (tasks) with priority and due dates (YYYY-MM-DD).
3. Generate exactly 5 practice multiple-choice questions testing these concepts.

Return your output ONLY as a JSON block with the following schema:
{{
  "weak_topics": [
    {{"topic": "<topic name>", "reason": "<explanation of weakness/difficulty>"}}
  ],
  "revision_plan": [
    {{"title": "<plan item title>", "content": "<description>", "due_date": "YYYY-MM-DD", "priority": "high"|"medium"|"low"}}
  ],
  "practice_questions": [
    {{
      "question": "<question text>",
      "options": ["<option A>", "<option B>", "<option C>", "<option D>"],
      "correct_answer": "<the correct option text, must match one option exactly>",
      "explanation": "<detailed explanation of why this option is correct>"
    }}
  ]
}}
"""

    try:
        response_text = await run_agent_until_completed(pod, "hello", prompt)
        parsed_data = extract_json(response_text)
        return parsed_data, search_results
    except Exception as e:
        return {
            "weak_topics": [],
            "revision_plan": [],
            "practice_questions": [],
            "error": str(e)
        }, search_results

# -- LIFE OPS EXTENSIONS --

async def generate_weekly_review_summary(open_tasks: List[models.Item], slipped_tasks: List[models.Item], stale_followups: List[models.Item]) -> Dict[str, Any]:
    pod = get_lemma_pod()
    
    open_str = "\n".join([f"- [ID: {t.id}] {t.title} (Priority: {t.priority or 'none'})" for t in open_tasks])
    slipped_str = "\n".join([f"- [ID: {t.id}] {t.title} (Was due: {t.due_date.strftime('%Y-%m-%d') if t.due_date else 'none'})" for t in slipped_tasks])
    stale_str = "\n".join([f"- [ID: {t.id}] {t.title} (Waiting since: {t.metadata_json.get('waiting_since', 'none')})" for t in stale_followups])

    prompt = f"""You are the LifeOS Executive Assistant. Please compile a weekly review summary based on these items:

OPEN ACTIVE TASKS:
{open_str or 'None'}

SLIPPED DEADLINES / OVERDUE:
{slipped_str or 'None'}

STALE FOLLOW-UPS (WAITING ON SOMEONE):
{stale_str or 'None'}

Generate a weekly review summary in plain-language markdown. 
First, summarize in 2-3 sentences what they accomplished, what slipped, and their focus.
Second, identify the specific IDs of items that require immediate attention.

Return your output ONLY as a JSON block with the following schema:
{{
  "summary": "<friendly markdown summary text here. Include bullet points if needed.>",
  "attention_item_ids": [<list of integers matching the IDs of items that need attention>]
}}
"""
    try:
        resp = await run_agent_until_completed(pod, "hello", prompt)
        return extract_json(resp)
    except Exception as e:
        return {
            "summary": f"Failed to generate summary: {str(e)}",
            "attention_item_ids": []
        }

async def parse_commitment_inbox(text: str) -> Dict[str, Any]:
    pod = get_lemma_pod()
    
    # We pass the current date for relative parsing
    current_date_str = datetime.date.today().strftime("%Y-%m-%d")
    
    prompt = f"""You are a natural language parser for LifeOS.
Today is {current_date_str}.
Please parse this raw user commitment: "{text}"

Extract the following:
1. Title: The clean action (e.g., "Call dentist", "Submit report").
2. Due Date: The parsed target date (in YYYY-MM-DD format) or null if no date is mentioned. Treat relative terms like "tomorrow", "next Friday" based on today's date ({current_date_str}).
3. Priority: "high", "medium", or "low".
4. Category: A single word tag (e.g., "personal", "work", "study", "health").

Return your output ONLY as a JSON block with the following schema:
{{
  "title": "<title>",
  "due_date": "YYYY-MM-DD"|null,
  "priority": "high"|"medium"|"low",
  "category": "<category>"
}}
"""
    try:
        resp = await run_agent_until_completed(pod, "hello", prompt)
        return extract_json(resp)
    except Exception as e:
        return {
            "title": text,
            "due_date": None,
            "priority": "medium",
            "category": "personal",
            "error": str(e)
        }

# -- SECOND BRAIN EXTENSIONS --

async def surface_brain_insights(notes: List[models.Item]) -> List[Dict[str, Any]]:
    pod = get_lemma_pod()
    
    notes_str = "\n".join([f"- [ID: {n.id}] {n.title}: {n.content[:200]}" for n in notes])
    
    prompt = f"""You are the Second Brain analyst for LifeOS.
Review these notes from the past 30 days:
{notes_str or 'No notes recorded.'}

Identify 3-5 key insights, patterns, contradictions, or forgotten ideas worth revisiting.
For each insight:
1. Title: A short catchy title (e.g. "Struggling with focus", "Gym habit slipping").
2. Description: 1-2 sentences summarizing the pattern or insight.
3. Action: A suggested action ("task" to turn into a task, "expand" to write a follow-up note, or "archive").
4. Source Note IDs: A list of integers containing the note IDs that contributed to this insight.

Return your output ONLY as a JSON block matching this schema:
{{
  "insights": [
    {{
      "title": "<title>",
      "description": "<description>",
      "action": "task"|"expand"|"archive",
      "source_note_ids": [<list of integers>]
    }}
  ]
}}
"""
    try:
        resp = await run_agent_until_completed(pod, "hello", prompt)
        data = extract_json(resp)
        return data.get("insights", [])
    except Exception:
        return []

async def generate_draft_from_notes(notes: List[models.Item], format_type: str) -> str:
    pod = get_lemma_pod()
    
    notes_str = "\n---\n".join([f"Note: {n.title}\nContent:\n{n.content}" for n in notes])
    
    prompt = f"""You are a content draft generator for LifeOS.
Combine the following notes to draft a coherent document of format: {format_type}.

NOTES TO COMBINE:
{notes_str}

Draft the content beautifully. Do not include introductory conversational text (like "Here is your draft:"). Start writing the draft directly.
"""
    try:
        return await run_agent_until_completed(pod, "hello", prompt)
    except Exception as e:
        return f"Failed to generate draft: {str(e)}"

# -- LEARNING COMPANION EXTENSIONS --

async def score_test_and_map_topics(test_results: List[Dict[str, Any]]) -> Dict[str, Any]:
    pod = get_lemma_pod()
    
    # Format results
    results_str = ""
    for idx, r in enumerate(test_results):
        results_str += f"""
Question {idx+1}: {r.get('question')}
Selected Answer: {r.get('selected')}
Correct Answer: {r.get('correct')}
Associated Topic: {r.get('topic', 'unknown')}
"""

    prompt = f"""You are the Learning Grader for LifeOS.
Review the following practice test results:
{results_str}

Perform the following:
1. Tag each question with its topic.
2. Build a topic strength map: Rank the topics from weakest to strongest.
3. Generate a list of recommended revision tasks (re-study plans) for the weakest topics.

Return your output ONLY as a JSON block matching this schema:
{{
  "topic_strength": [
    {{"topic": "<topic name>", "score": "<correct count>/<total questions on topic>", "status": "weak"|"strong"}}
  ],
  "suggested_revisions": [
    {{
      "title": "<revision task title>",
      "content": "<what to study and why based on test errors>",
      "priority": "high"|"medium"|"low",
      "due_date": "YYYY-MM-DD"
    }}
  ]
}}
"""
    try:
        resp = await run_agent_until_completed(pod, "hello", prompt)
        return extract_json(resp)
    except Exception as e:
        return {
            "topic_strength": [],
            "suggested_revisions": [],
            "error": str(e)
        }

async def generate_spaced_repetition_quiz(concept_title: str, concept_content: str) -> List[Dict[str, Any]]:
    pod = get_lemma_pod()
    
    prompt = f"""You are the Learning Suite Examiner for LifeOS.
Generate a quick 3-question Multiple Choice Quiz to test the user's recall on the concept:
Concept Name: {concept_title}
Explanation: {concept_content}

Return exactly 3 multiple choice questions.
Return your output ONLY as a JSON block matching this schema:
{{
  "questions": [
    {{
      "question": "<question text>",
      "options": ["<option A>", "<option B>", "<option C>", "<option D>"],
      "correct_answer": "<the correct option text, must match one option exactly>",
      "explanation": "<detailed explanation of why this option is correct>"
    }}
  ]
}}
"""
    try:
        resp = await run_agent_until_completed(pod, "hello", prompt)
        data = extract_json(resp)
        return data.get("questions", [])
    except Exception:
        return []

async def generate_study_debrief_insights(summary: str, confusion: str) -> Dict[str, Any]:
    pod = get_lemma_pod()
    
    prompt = f"""You are the Pomodoro debrief assistant for LifeOS.
The user completed a focus session.
Summary of what was covered: {summary}
Reported confusion / struggles: {confusion or 'None reported.'}

Generate a short debrief card containing:
1. A feedback sentence of encouragement.
2. A list of weak topics that arose during this session (each with a topic name and reason).
3. Suggested focus topic for the next session.

Return your output ONLY as a JSON block matching this schema:
{{
  "feedback": "<feedback string>",
  "weak_topics": [
    {{"topic": "<topic name>", "reason": "<reason>"}}
  ],
  "suggested_next_focus": "<suggested topic name>"
}}
"""
    try:
        resp = await run_agent_until_completed(pod, "hello", prompt)
        return extract_json(resp)
    except Exception as e:
        return {
            "feedback": "Great focus session! Keep studying.",
            "weak_topics": [],
            "suggested_next_focus": "Continue current topic.",
            "error": str(e)
        }

