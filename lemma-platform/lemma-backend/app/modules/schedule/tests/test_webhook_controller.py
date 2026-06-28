from app.modules.schedule.api.controllers.webhook_controller import (
    _normalize_composio_payload,
    router,
)


def test_direct_schedule_webhook_route_is_removed():
    """The unauthenticated, unverified POST /webhooks/schedules/{id} endpoint was
    deleted (security_authz-02). Only the composio-verified /webhooks/{source}
    routes remain."""
    paths = {route.path for route in router.routes}
    assert "/webhooks/schedules/{schedule_id}" not in paths
    assert "/webhooks/{source}" in paths


def test_normalize_composio_payload_maps_sdk_result_to_internal_shape():
    verification_result = {
        "version": "V3",
        "payload": {
            "id": "ti_123",
            "uuid": "ti_123",
            "user_id": "user_123",
            "toolkit_slug": "GOOGLECALENDAR",
            "trigger_slug": "GOOGLECALENDAR_GOOGLE_CALENDAR_EVENT_SYNC_TRIGGER",
            "metadata": {
                "id": "ti_123",
                "uuid": "ti_123",
                "toolkit_slug": "GOOGLECALENDAR",
                "trigger_slug": "GOOGLECALENDAR_GOOGLE_CALENDAR_EVENT_SYNC_TRIGGER",
                "trigger_data": None,
                "trigger_config": {},
                "connected_account": {
                    "id": "ca_123",
                    "uuid": "ca_123",
                    "auth_config_id": "ac_123",
                    "auth_config_uuid": "ac_123",
                    "user_id": "user_123",
                    "status": "ACTIVE",
                },
            },
            "payload": {
                "event_id": "evt_123",
            },
        },
        "raw_payload": {
            "id": "msg_123",
            "timestamp": "2026-03-22T06:50:57.477Z",
            "type": "composio.trigger.message",
            "metadata": {
                "log_id": "log_123",
            },
            "data": {
                "event_id": "evt_123",
            },
        },
    }

    normalized = _normalize_composio_payload(verification_result)

    assert normalized["type"] == "GOOGLECALENDAR_GOOGLE_CALENDAR_EVENT_SYNC_TRIGGER"
    assert normalized["webhook_type"] == "composio.trigger.message"
    assert normalized["data"] == {"event_id": "evt_123"}
    assert normalized["metadata"]["trigger_id"] == "ti_123"
    assert normalized["metadata"]["connected_account_id"] == "ca_123"
    assert normalized["metadata"]["version"] == "V3"


def test_normalize_composio_payload_falls_back_to_raw_data_payload():
    verification_result = {
        "version": "V3",
        "payload": {
            "id": "ti_123",
            "uuid": "ti_123",
            "user_id": "user_123",
            "toolkit_slug": "GOOGLECALENDAR",
            "trigger_slug": "GOOGLECALENDAR_GOOGLE_CALENDAR_EVENT_SYNC_TRIGGER",
            "metadata": {
                "connected_account": {
                    "id": "ca_123",
                    "auth_config_id": "ac_123",
                },
            },
            "payload": None,
        },
        "raw_payload": {
            "type": "composio.trigger.message",
            "data": {
                "event_id": "evt_123",
            },
        },
    }

    normalized = _normalize_composio_payload(verification_result)

    assert normalized["data"] == {"event_id": "evt_123"}
    assert normalized["metadata"]["trigger_id"] == "ti_123"
