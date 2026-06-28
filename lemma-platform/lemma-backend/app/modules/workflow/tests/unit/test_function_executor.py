"""FunctionExecutor node outcome: JOB functions suspend on a FUNCTION wait;
API functions (and any inline result) advance without waiting."""
from __future__ import annotations

from types import SimpleNamespace
from uuid import uuid4

import pytest

from app.modules.workflow.domain.wait import WorkflowRunWaitType
from app.modules.workflow.execution.executors.function import FunctionExecutor
from app.modules.workflow.execution.outcome import Advance, Suspend

pytestmark = pytest.mark.asyncio


def _node():
    return SimpleNamespace(
        config=SimpleNamespace(function_name="echo", input_mapping={})
    )


def _step(result):
    async def _execute_function(name, inputs, pod_id, user_id, ctx=None):
        return result

    return SimpleNamespace(
        context=SimpleNamespace(resolve_inputs=lambda mapping: {"a": 1}),
        function=SimpleNamespace(execute_function=_execute_function),
        pod_id=uuid4(),
        user_id=uuid4(),
        authz_ctx=None,
    )


async def test_job_function_suspends_with_function_wait():
    run_id = uuid4()
    outcome = await FunctionExecutor().execute(
        _node(),
        _step({"run_id": str(run_id), "status": "RUNNING", "function_type": "JOB"}),
    )
    assert isinstance(outcome, Suspend)
    assert outcome.wait.wait_type == WorkflowRunWaitType.FUNCTION
    assert outcome.wait.external_ref == str(run_id)


async def test_api_function_advances_inline():
    outcome = await FunctionExecutor().execute(_node(), _step({"done": True}))
    assert isinstance(outcome, Advance)
    assert outcome.output == {"done": True}


async def test_non_job_pending_result_raises():
    with pytest.raises(RuntimeError, match="Only JOB functions can suspend"):
        await FunctionExecutor().execute(
            _node(),
            _step(
                {"run_id": str(uuid4()), "status": "RUNNING", "function_type": "API"}
            ),
        )


async def test_non_dict_result_wrapped_in_advance():
    outcome = await FunctionExecutor().execute(_node(), _step("plain-string"))
    assert isinstance(outcome, Advance)
    assert outcome.output == {"result": "plain-string"}
