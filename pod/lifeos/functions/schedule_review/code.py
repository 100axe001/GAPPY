#input_type_name: ScheduleReviewInput
#output_type_name: ScheduleReviewResult
#function_name: schedule_review

from datetime import datetime, timedelta, timezone
from typing import Optional
from pydantic import BaseModel
from lemma_sdk import FunctionContext, Pod

# Spaced-repetition ladder (days). Correct answers climb it; misses reset to the bottom.
LADDER = [1, 3, 7, 14, 30]


def _next_interval(current: int, remembered: bool) -> int:
    if not remembered:
        return LADDER[0]
    for step in LADDER:
        if step > current:
            return step
    return LADDER[-1]


class ScheduleReviewInput(BaseModel):
    concept_id: str
    user_id: str
    concept_title: Optional[str] = ""
    remembered: bool = True


class ScheduleReviewResult(BaseModel):
    review_id: str
    interval_days: int
    due_date: str
    status: str


async def schedule_review(ctx: FunctionContext, data: ScheduleReviewInput) -> ScheduleReviewResult:
    """Upsert the spaced-repetition schedule for one study concept."""
    pod = Pod.from_env()

    existing = pod.records.list(
        "study_reviews",
        limit=1,
        filter=[
            {"field": "concept_id", "op": "eq", "value": data.concept_id},
            {"field": "owner_id", "op": "eq", "value": data.user_id},
        ],
    ).to_dict()["items"]

    prev_interval = existing[0].get("interval_days", 0) if existing else 0
    interval = _next_interval(prev_interval, data.remembered)
    now = datetime.now(timezone.utc)
    due = now + timedelta(days=interval)
    status = "learned" if interval >= LADDER[-1] else "learning"

    payload = {
        "concept_id": data.concept_id,
        "concept_title": data.concept_title or "",
        "interval_days": interval,
        "due_date": due.isoformat(),
        "last_reviewed_at": now.isoformat(),
        "status": status,
        "owner_id": data.user_id,
    }

    if existing:
        rec = pod.table("study_reviews").update(str(existing[0]["id"]), payload)
    else:
        rec = pod.table("study_reviews").create(payload)

    return ScheduleReviewResult(
        review_id=str(rec["id"]),
        interval_days=interval,
        due_date=due.isoformat(),
        status=status,
    )
