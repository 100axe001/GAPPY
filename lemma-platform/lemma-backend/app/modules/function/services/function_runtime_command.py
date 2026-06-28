from __future__ import annotations

from app.core.helpers.slug import slugify
from app.modules.function.domain.entities import FunctionEntity


def function_workspace_cwd(function: FunctionEntity) -> str:
    return f"/workspace/pods/{function.pod_id}/functions/{slugify(function.name)}"
