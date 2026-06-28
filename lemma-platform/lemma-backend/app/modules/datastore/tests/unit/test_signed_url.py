from __future__ import annotations

from app.modules.datastore.services.files.signed_url import _clamp


def test_clamp_uses_default_when_none():
    assert _clamp(None, default=50, ceiling=100) == 50


def test_clamp_caps_at_ceiling():
    assert _clamp(999, default=50, ceiling=100) == 100


def test_clamp_floors_at_one():
    assert _clamp(0, default=50, ceiling=100) == 1
    assert _clamp(-5, default=50, ceiling=100) == 1


def test_clamp_passes_through_value_in_range():
    assert _clamp(30, default=50, ceiling=100) == 30
