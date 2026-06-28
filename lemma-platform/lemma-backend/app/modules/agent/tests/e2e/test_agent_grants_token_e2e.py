"""E2E: agent delegation tokens honor datastore resource grants.

Agents carry resource grants exactly like functions (grantee_type="AGENT").
These tests mint a real agent delegation token and drive the datastore record
API with it, asserting the workload can reach granted tables and is denied on
ungranted ones — across both RLS and non-RLS tables.
"""

from __future__ import annotations

from uuid import UUID, uuid4

import pytest
from fastapi import status
from httpx import ASGITransport, AsyncClient

from app.modules.identity.infrastructure.supertokens_auth.helpers import (
    get_user_token,
)
from app.modules.identity.infrastructure.supertokens_auth.token_factory import (
    build_delegation_claims,
)

pytestmark = pytest.mark.e2e


async def _create_pod(authenticated_client, fixed_test_org) -> str:
    response = await authenticated_client.post(
        "/pods",
        json={
            "name": f"agent-grants-{uuid4().hex[:8]}",
            "description": "Agent grant token e2e",
            "organization_id": fixed_test_org["id"],
            "type": "HYBRID",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED, response.text
    return response.json()["id"]


async def _create_table(
    authenticated_client,
    pod_id: str,
    table_name: str,
    *,
    enable_rls: bool,
) -> dict:
    payload = {
        "name": table_name,
        "primary_key_column": "id",
        "enable_rls": enable_rls,
        "columns": [
            {"name": "id", "type": "UUID", "required": True, "auto": True},
            {"name": "title", "type": "TEXT", "required": True},
        ],
    }
    response = await authenticated_client.post(
        f"/pods/{pod_id}/datastore/tables",
        json=payload,
    )
    assert response.status_code == status.HTTP_201_CREATED, response.text
    return response.json()


async def _create_agent(authenticated_client, pod_id: str, name: str) -> dict:
    response = await authenticated_client.post(
        f"/pods/{pod_id}/agents",
        json={"name": name, "instruction": "Answer briefly."},
    )
    assert response.status_code == status.HTTP_201_CREATED, response.text
    return response.json()


async def _replace_agent_grants(
    authenticated_client,
    pod_id: str,
    agent_name: str,
    grants: list[dict],
) -> dict:
    response = await authenticated_client.put(
        f"/pods/{pod_id}/agents/{agent_name}/permissions",
        json={"grants": grants},
    )
    assert response.status_code == status.HTTP_200_OK, response.text
    return response.json()


def _mint_agent_client(
    test_app,
    *,
    user_id: str,
    agent_id: str,
    agent_name: str,
    pod_id: str,
):
    """Build an httpx client authenticated as the agent workload, mirroring how
    the backend mints delegation tokens for agents at runtime."""

    async def _build() -> AsyncClient:
        claims = build_delegation_claims(
            workload_type="agent",
            workload_id=UUID(agent_id),
            pod_id=UUID(pod_id),
            session_id=uuid4().hex,
            invoked_by_user_id=UUID(user_id),
            workload_name=agent_name,
        )
        token = await get_user_token(UUID(user_id), delegation_claims=claims)
        return AsyncClient(
            transport=ASGITransport(app=test_app),
            base_url="http://testserver",
            headers={"Authorization": f"Bearer {token}"},
        )

    return _build()


@pytest.mark.asyncio
@pytest.mark.parametrize("enable_rls", [True, False], ids=["rls", "no-rls"])
async def test_agent_token_respects_datastore_table_grants(
    test_app,
    authenticated_client,
    fixed_test_org,
    fixed_test_user,
    enable_rls,
):
    pod_id = await _create_pod(authenticated_client, fixed_test_org)
    suffix = uuid4().hex[:8]
    granted_table = f"granted_{suffix}"
    ungranted_table = f"ungranted_{suffix}"
    agent_name = f"grant_agent_{suffix}"

    await _create_table(
        authenticated_client, pod_id, granted_table, enable_rls=enable_rls
    )
    await _create_table(
        authenticated_client, pod_id, ungranted_table, enable_rls=enable_rls
    )
    agent = await _create_agent(authenticated_client, pod_id, agent_name)

    # Grant the agent data access to the granted table only. Note: record.write,
    # not table.update — data access is governed by record permissions.
    await _replace_agent_grants(
        authenticated_client,
        pod_id,
        agent_name,
        [
            {
                "resource_type": "agent",
                "resource_name": agent_name,
                "permission_ids": ["agent.read"],
            },
            {
                "resource_type": "datastore_table",
                "resource_name": granted_table,
                "permission_ids": [
                    "datastore.table.read",
                    "datastore.record.read",
                    "datastore.record.write",
                ],
            },
        ],
    )

    agent_client = await _mint_agent_client(
        test_app,
        user_id=fixed_test_user["id"],
        agent_id=agent["id"],
        agent_name=agent_name,
        pod_id=pod_id,
    )
    try:
        # Granted table: the agent token can write and read records.
        write = await agent_client.post(
            f"/pods/{pod_id}/datastore/tables/{granted_table}/records",
            json={"data": {"title": "from-agent"}},
            follow_redirects=True,
        )
        assert write.status_code == status.HTTP_201_CREATED, write.text

        read = await agent_client.get(
            f"/pods/{pod_id}/datastore/tables/{granted_table}/records",
        )
        assert read.status_code == status.HTTP_200_OK, read.text
        assert read.json()["total"] == 1
        assert read.json()["items"][0]["title"] == "from-agent"

        # Ungranted table: the agent token is denied with a real 403.
        denied_write = await agent_client.post(
            f"/pods/{pod_id}/datastore/tables/{ungranted_table}/records",
            json={"data": {"title": "should-fail"}},
            follow_redirects=True,
        )
        assert denied_write.status_code == status.HTTP_403_FORBIDDEN, denied_write.text
        assert denied_write.json()["code"] == "MISSING_WORKLOAD_RESOURCE_GRANT"

        denied_read = await agent_client.get(
            f"/pods/{pod_id}/datastore/tables/{ungranted_table}/records",
        )
        assert denied_read.status_code == status.HTTP_403_FORBIDDEN, denied_read.text
    finally:
        await agent_client.aclose()


@pytest.mark.asyncio
async def test_agent_token_requires_record_write_not_table_update(
    test_app,
    authenticated_client,
    fixed_test_org,
    fixed_test_user,
):
    """Schema permissions (table.read + table.update) do not authorize record
    writes for an agent workload; datastore.record.write does."""
    pod_id = await _create_pod(authenticated_client, fixed_test_org)
    suffix = uuid4().hex[:8]
    table_name = f"shared_{suffix}"
    agent_name = f"perm_agent_{suffix}"

    await _create_table(authenticated_client, pod_id, table_name, enable_rls=False)
    agent = await _create_agent(authenticated_client, pod_id, agent_name)

    await _replace_agent_grants(
        authenticated_client,
        pod_id,
        agent_name,
        [
            {
                "resource_type": "datastore_table",
                "resource_name": table_name,
                "permission_ids": [
                    "datastore.table.read",
                    "datastore.table.update",
                ],
            },
        ],
    )

    agent_client = await _mint_agent_client(
        test_app,
        user_id=fixed_test_user["id"],
        agent_id=agent["id"],
        agent_name=agent_name,
        pod_id=pod_id,
    )
    try:
        denied = await agent_client.post(
            f"/pods/{pod_id}/datastore/tables/{table_name}/records",
            json={"data": {"title": "schema-perms-only"}},
            follow_redirects=True,
        )
        assert denied.status_code == status.HTTP_403_FORBIDDEN, denied.text
        assert denied.json()["code"] == "MISSING_WORKLOAD_RESOURCE_GRANT"

        # Swap table.update for record.write -> the write now succeeds.
        await _replace_agent_grants(
            authenticated_client,
            pod_id,
            agent_name,
            [
                {
                    "resource_type": "datastore_table",
                    "resource_name": table_name,
                    "permission_ids": [
                        "datastore.table.read",
                        "datastore.record.write",
                    ],
                },
            ],
        )

        allowed = await agent_client.post(
            f"/pods/{pod_id}/datastore/tables/{table_name}/records",
            json={"data": {"title": "record-write-granted"}},
            follow_redirects=True,
        )
        assert allowed.status_code == status.HTTP_201_CREATED, allowed.text
    finally:
        await agent_client.aclose()
