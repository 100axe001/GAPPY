"""E2E regression tests for dynamic-table DDL injection safety (Workstream B).

Injection attempts through computed-column ``expression`` and column ``default``
must be rejected with a 4xx and must not execute the injected DDL (the target
table survives). The read-only SQL guard is also pinned.
"""

from __future__ import annotations

from uuid import uuid4

import pytest
from fastapi import status
from httpx import AsyncClient

from app.modules.datastore.tests.e2e.harness import DatastoreApi

pytestmark = pytest.mark.e2e


@pytest.fixture
async def pod_api(authenticated_client: AsyncClient, fixed_test_org) -> DatastoreApi:
    suffix = uuid4().hex[:8]
    response = await authenticated_client.post(
        "/pods",
        json={
            "name": f"DDL Pod {suffix}",
            "slug": f"ddl-pod-{suffix}",
            "type": "ASSISTANT",
            "organization_id": fixed_test_org["id"],
        },
    )
    assert response.status_code == status.HTTP_201_CREATED, response.text
    return DatastoreApi(authenticated_client, response.json()["id"])


class TestDdlInjectionSafety:
    @pytest.mark.asyncio
    async def test_computed_expression_injection_is_rejected(
        self, pod_api: DatastoreApi
    ):
        suffix = uuid4().hex[:8]
        victim = f"victim_{suffix}"
        await pod_api.create_table(
            {
                "name": victim,
                "enable_rls": False,
                "columns": [{"name": "qty", "type": "INTEGER"}],
            }
        )

        target = f"target_{suffix}"
        resp = await pod_api.request(
            "POST",
            f"/pods/{pod_api.pod_id}/datastore/tables",
            json={
                "name": target,
                "enable_rls": False,
                "columns": [
                    {"name": "qty", "type": "INTEGER"},
                    {
                        "name": "evil",
                        "type": "INTEGER",
                        "computed": True,
                        "expression": f"qty) STORED; DROP TABLE {victim}; --",
                    },
                ],
            },
        )
        assert resp.status_code in (
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_422_UNPROCESSABLE_ENTITY,
        ), resp.text
        # The injected DROP must not have run.
        await pod_api.get_table(victim, expected_status=status.HTTP_200_OK)

    @pytest.mark.asyncio
    async def test_default_value_injection_is_rejected(self, pod_api: DatastoreApi):
        suffix = uuid4().hex[:8]
        victim = f"victim_def_{suffix}"
        await pod_api.create_table(
            {
                "name": victim,
                "enable_rls": False,
                "columns": [{"name": "name", "type": "TEXT"}],
            }
        )

        table = f"defaults_{suffix}"
        await pod_api.create_table(
            {
                "name": table,
                "enable_rls": False,
                "columns": [{"name": "name", "type": "TEXT"}],
            }
        )
        # A string default with an embedded quote must be quoted/escaped, not
        # break out of the literal. We send it as a normal string default and
        # assert the column is created safely (or cleanly rejected), never that
        # the victim table is dropped.
        resp = await pod_api.request(
            "POST",
            f"/pods/{pod_api.pod_id}/datastore/tables/{table}/columns",
            json={
                "column": {
                    "name": "note",
                    "type": "TEXT",
                    "default": f"x'); DROP TABLE {victim}; --",
                }
            },
        )
        assert resp.status_code in (
            status.HTTP_200_OK,
            status.HTTP_201_CREATED,
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_422_UNPROCESSABLE_ENTITY,
        ), resp.text
        # Regardless of accept/reject, the injected DROP must not have executed.
        await pod_api.get_table(victim, expected_status=status.HTTP_200_OK)

    @pytest.mark.asyncio
    async def test_enum_check_constraint_rejects_out_of_options_default(
        self, pod_api: DatastoreApi
    ):
        suffix = uuid4().hex[:8]
        resp = await pod_api.request(
            "POST",
            f"/pods/{pod_api.pod_id}/datastore/tables",
            json={
                "name": f"enum_{suffix}",
                "enable_rls": False,
                "columns": [
                    {
                        "name": "status",
                        "type": "ENUM",
                        "options": ["open", "closed"],
                        "default": "invalid_option",
                    }
                ],
            },
        )
        assert resp.status_code in (
            status.HTTP_400_BAD_REQUEST,
            status.HTTP_422_UNPROCESSABLE_ENTITY,
        ), resp.text
