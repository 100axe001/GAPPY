from __future__ import annotations

import json
from uuid import uuid4

import httpx
import pytest

from agentbox_client.apps.function_executor import (
    FunctionExecuteRequest,
    FunctionExecutorClient,
)


@pytest.mark.asyncio
async def test_function_executor_client_posts_through_manager_app_proxy():
    calls: list[httpx.Request] = []
    run_id = uuid4()
    pod_id = uuid4()

    async def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(
            200,
            json={
                "status": "completed",
                "output_data": {"ok": True},
                "error": None,
                "logs": [],
                "code_hash": "abc",
                "duration_ms": 10,
            },
        )

    client = FunctionExecutorClient(
        manager_base_url="https://manager.test",
        manager_api_key="manager-key",
        lemma_token="lemma-token",
    )
    await client.client.aclose()
    client.client = httpx.AsyncClient(
        base_url="https://manager.test",
        transport=httpx.MockTransport(handler),
        headers={
            "X-API-Key": "manager-key",
            "Authorization": "Bearer lemma-token",
            "Accept": "application/json",
        },
    )

    try:
        response = await client.execute(
            sandbox_id="sandbox-1",
            pod_id=pod_id,
            function_name="hello",
            request=FunctionExecuteRequest(
                run_id=run_id,
                input_data={"name": "Ada"},
            ),
        )
    finally:
        await client.close()

    assert response.status == "completed"
    assert calls[0].url.path == (
        f"/sandboxes/sandbox-1/apps/function_executor/"
        f"pods/{pod_id}/functions/hello/execute"
    )
    assert calls[0].headers["x-api-key"] == "manager-key"
    assert calls[0].headers["authorization"] == "Bearer lemma-token"
    assert "env_vars" not in json.loads(calls[0].content)
