from __future__ import annotations

from uuid import uuid4

import pytest

from app.core.authorization.delegation import (
    CLAIM_ACTOR_ID,
    CLAIM_ACTOR_NAME,
    CLAIM_ACTOR_TYPE,
    CLAIM_INVOKED_BY_USER_ID,
    CLAIM_POD_ID,
    CLAIM_SCOPE,
    CLAIM_SESSION_ID,
    DelegationClaimsError,
    WorkloadPrincipalType,
    parse_delegation_claims,
)


def _valid_payload() -> dict:
    return {
        CLAIM_ACTOR_TYPE: WorkloadPrincipalType.FUNCTION.value,
        CLAIM_ACTOR_ID: str(uuid4()),
        CLAIM_ACTOR_NAME: "reconciler",
        CLAIM_POD_ID: str(uuid4()),
        CLAIM_SESSION_ID: "session-123",
        CLAIM_SCOPE: ["datastore.read"],
        CLAIM_INVOKED_BY_USER_ID: str(uuid4()),
    }


def test_parse_valid_delegation_claims():
    payload = _valid_payload()

    parsed = parse_delegation_claims(payload)

    assert parsed is not None
    assert parsed.actor_type == WorkloadPrincipalType.FUNCTION
    assert parsed.actor_name == "reconciler"
    assert parsed.session_id == "session-123"
    assert parsed.scope == ["datastore.read"]


def test_parse_claims_missing_required_fields():
    payload = _valid_payload()
    payload.pop(CLAIM_POD_ID)

    with pytest.raises(DelegationClaimsError, match="Missing delegated claim"):
        parse_delegation_claims(payload)


def test_parse_claims_invalid_uuid():
    payload = _valid_payload()
    payload[CLAIM_ACTOR_ID] = "not-a-uuid"

    with pytest.raises(DelegationClaimsError, match="Invalid UUID"):
        parse_delegation_claims(payload)


def test_parse_claims_unknown_actor_type():
    payload = _valid_payload()
    payload[CLAIM_ACTOR_TYPE] = "worker"

    with pytest.raises(DelegationClaimsError, match="Unsupported delegated actor type"):
        parse_delegation_claims(payload)
