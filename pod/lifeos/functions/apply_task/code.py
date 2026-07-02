#input_type_name: ApplyTaskInput
#output_type_name: ApplyTaskResult
#function_name: apply_task

from typing import Optional
from pydantic import BaseModel
from lemma_sdk import FunctionContext, Pod


class ApplyTaskInput(BaseModel):
    title: str
    content: Optional[str] = ""
    due_date: Optional[str] = ""
    priority: Optional[str] = "medium"
    category: Optional[str] = ""
    user_id: str


class ApplyTaskResult(BaseModel):
    item_id: str
    created: bool


async def apply_task(ctx: FunctionContext, data: ApplyTaskInput) -> ApplyTaskResult:
    """Create a task item from an approved commitment."""
    pod = Pod.from_env()

    record = {
        "type": "task",
        "title": data.title,
        "content": data.content or "",
        "status": "todo",
        "priority": (data.priority or "medium").lower(),
        "category": data.category or "",
        "owner_id": data.user_id,
        "source": "workflow",
    }
    if data.due_date:
        record["due_date"] = data.due_date

    created = pod.table("items").create(record)
    return ApplyTaskResult(item_id=str(created["id"]), created=True)
