from __future__ import annotations

from app.modules.agent_surfaces.domain.models import (
    SurfaceQuestion,
    SurfaceQuestionOption,
    SurfaceQuestionRenderPlan,
)
from app.modules.agent_surfaces.platforms.slack.service import _question_blocks
from app.modules.agent_surfaces.platforms.slack.parser import SlackMessageParser
from app.modules.agent_surfaces.platforms.teams.adapter import _teams_question_card
from app.modules.agent_surfaces.platforms.teams.parser import (
    TEAMS_FORM_CALLBACK_KEY,
    TeamsMessageParser,
)
from app.modules.agent_surfaces.api.controllers.webhook_controller import (
    _decode_webhook_payload,
)


def _plan() -> SurfaceQuestionRenderPlan:
    return SurfaceQuestionRenderPlan(
        title="A few quick questions",
        callback_id="conv-1|tool-1",
        questions=[
            SurfaceQuestion(
                header="country",
                question="Which country?",
                options=[
                    SurfaceQuestionOption(label="US", recommended=True),
                    SurfaceQuestionOption(label="CA"),
                ],
            ),
            SurfaceQuestion(
                header="tags",
                question="Which tags?",
                multi_select=True,
                options=[
                    SurfaceQuestionOption(label="a"),
                    SurfaceQuestionOption(label="b"),
                ],
            ),
        ],
    )


# ── Slack render ────────────────────────────────────────────────────────────


def test_slack_question_blocks_keys_by_header_and_carries_callback():
    blocks = _question_blocks(_plan())
    selects = {
        b["block_id"]: b
        for b in blocks
        if b.get("type") == "input"
        and b["element"]["type"] in ("static_select", "multi_static_select")
    }
    assert selects["country"]["element"]["type"] == "static_select"
    assert selects["tags"]["element"]["type"] == "multi_static_select"
    # option values are the labels; recommended is annotated
    country_opts = selects["country"]["element"]["options"]
    assert {o["value"] for o in country_opts} == {"US", "CA"}
    assert any("recommended" in o["text"]["text"] for o in country_opts)
    # an optional "Other" free-text input is added per question
    other_ids = {
        b["block_id"] for b in blocks if b.get("type") == "input"
    } & {"country__other", "tags__other"}
    assert other_ids == {"country__other", "tags__other"}
    submit = [b for b in blocks if b.get("type") == "actions"][0]["elements"][0]
    assert submit["action_id"] == "lemma_form_submit"
    assert submit["value"] == "conv-1|tool-1"


# ── Teams render ──────────────────────────────────────────────────────────────


def test_teams_question_card_keys_by_header_and_carries_callback():
    card = _teams_question_card(_plan())
    choice_sets = {
        el["id"]: el for el in card["body"] if el.get("type") == "Input.ChoiceSet"
    }
    assert choice_sets["country"]["choices"][0]["value"] == "US"
    assert choice_sets["tags"]["isMultiSelect"] is True
    # an "Other" text input is added per question
    text_ids = {el["id"] for el in card["body"] if el.get("type") == "Input.Text"}
    assert text_ids == {"country__other", "tags__other"}
    submit = card["actions"][0]
    assert submit["type"] == "Action.Submit"
    assert submit["data"][TEAMS_FORM_CALLBACK_KEY] == "conv-1|tool-1"


# ── Slack interaction parse ───────────────────────────────────────────────────


def test_slack_parse_interaction_extracts_values():
    payload = {
        "type": "block_actions",
        "user": {"id": "U1"},
        "team": {"id": "T1"},
        "channel": {"id": "C1"},
        "container": {"message_ts": "123.45"},
        "message": {"ts": "123.45", "thread_ts": "100.0"},
        "actions": [
            {
                "action_id": "lemma_form_submit",
                "value": "conv-1|tool-1",
                "action_ts": "124.0",
            }
        ],
        "state": {
            "values": {
                "email": {"email": {"type": "plain_text_input", "value": "a@b.com"}},
                "country": {
                    "country": {
                        "type": "static_select",
                        "selected_option": {"value": "US"},
                    }
                },
                "tags": {
                    "tags": {
                        "type": "multi_static_select",
                        "selected_options": [{"value": "x"}, {"value": "y"}],
                    }
                },
            }
        },
    }
    interaction = SlackMessageParser().parse_interaction(payload)
    assert interaction is not None
    assert interaction.callback_id == "conv-1|tool-1"
    assert interaction.values == {
        "email": "a@b.com",
        "country": "US",
        "tags": ["x", "y"],
    }
    assert interaction.external_user_id == "U1"
    assert interaction.reply_target == {"channel": "C1", "thread_ts": "100.0"}
    # A normal message event is not an interaction.
    assert SlackMessageParser().parse_interaction({"type": "event_callback"}) is None


# ── Teams interaction parse ───────────────────────────────────────────────────


def test_teams_parse_interaction_extracts_values():
    payload = {
        "type": "message",
        "id": "act-9",
        "from": {"id": "29:u"},
        "conversation": {"id": "19:conv"},
        "channelData": {"tenant": {"id": "tid"}},
        "serviceUrl": "https://svc/",
        "replyToId": "act-1",
        "value": {
            TEAMS_FORM_CALLBACK_KEY: "conv-1|tool-2",
            "name": "Bob",
            "subscribe": "true",
        },
    }
    interaction = TeamsMessageParser().parse_interaction(payload)
    assert interaction is not None
    assert interaction.callback_id == "conv-1|tool-2"
    assert interaction.values == {"name": "Bob", "subscribe": "true"}
    assert interaction.external_user_id == "29:u"
    assert interaction.dedup_id == "act-9"
    assert interaction.reply_target["conversation_id"] == "19:conv"
    assert interaction.reply_target["reply_to_id"] == "act-1"
    # A plain message (no value dict) is not an interaction.
    assert TeamsMessageParser().parse_interaction({"type": "message"}) is None


# ── Webhook decode + body formatting ─────────────────────────────────────────


def test_decode_webhook_payload_handles_form_encoded_and_json():
    import json
    import urllib.parse

    inner = {"type": "block_actions", "actions": []}
    form_body = urllib.parse.urlencode({"payload": json.dumps(inner)}).encode("utf-8")
    decoded = _decode_webhook_payload(
        form_body, {"content-type": "application/x-www-form-urlencoded"}
    )
    assert decoded == inner

    json_body = json.dumps({"type": "event_callback"}).encode("utf-8")
    assert _decode_webhook_payload(json_body, {"content-type": "application/json"}) == {
        "type": "event_callback"
    }
    assert _decode_webhook_payload(b"", {}) == {}
