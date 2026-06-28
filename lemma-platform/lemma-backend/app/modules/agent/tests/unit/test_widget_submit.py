from __future__ import annotations

from app.core.html_document import wrap_html_fragment
from app.modules.agent.api.controllers.widget_controller import (
    WidgetSubmitRequest,
    _widget_submit_content,
)


def test_submit_bridge_injected_for_embed_and_standalone():
    doc = wrap_html_fragment("<div>hi</div>", title="t", embed=True)
    assert "data-lemma-submit-bridge" in doc
    assert "window.lemma.submit" in doc
    assert "window.sendPrompt" in doc
    # Embedded path posts to the parent; standalone path POSTs to /submit.
    assert "lemma-widget-submit" in doc
    assert "/submit" in doc
    # Embedded gets the height bridge too.
    assert "lemma-widget-height" in doc


def test_submit_bridge_present_without_height_bridge_when_standalone():
    doc = wrap_html_fragment("<div>hi</div>", embed=False)
    assert "data-lemma-submit-bridge" in doc  # submit works standalone too
    assert "lemma-widget-height" not in doc  # no height bridge for a promoted app


def test_widget_submit_content_prefers_text():
    assert _widget_submit_content(WidgetSubmitRequest(text="  hello  ")) == "hello"


def test_widget_submit_content_renders_payload_when_no_text():
    out = _widget_submit_content(WidgetSubmitRequest(payload={"rating": 5, "note": "ok"}))
    assert "rating" in out and "5" in out and "ok" in out


def test_widget_submit_content_empty():
    assert _widget_submit_content(WidgetSubmitRequest()) == "Submitted the widget."
