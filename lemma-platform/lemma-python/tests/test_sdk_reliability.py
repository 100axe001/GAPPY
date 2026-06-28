from __future__ import annotations

from lemma_sdk.errors import (
    LemmaAPIError,
    LemmaAuthError,
    LemmaConflictError,
    LemmaConnectionError,
    LemmaNotFoundError,
    LemmaPermissionError,
    LemmaRateLimitError,
    LemmaServerError,
    LemmaTimeoutError,
    api_error,
)
from lemma_sdk.transport import _RETRYABLE_STATUS, _retry_after_seconds, _retry_delay


def test_api_error_maps_status_to_subclass():
    assert isinstance(api_error(401, "x"), LemmaAuthError)
    assert isinstance(api_error(403, "x"), LemmaPermissionError)
    assert isinstance(api_error(404, "x"), LemmaNotFoundError)
    assert isinstance(api_error(409, "x"), LemmaConflictError)
    assert isinstance(api_error(429, "x"), LemmaRateLimitError)
    assert isinstance(api_error(503, "x"), LemmaServerError)


def test_api_error_falls_back_to_base_for_unmapped_status():
    assert type(api_error(418, "x")) is LemmaAPIError


def test_every_subclass_is_still_lemma_api_error():
    # so existing `except LemmaAPIError` keeps catching everything
    assert isinstance(api_error(404, "x"), LemmaAPIError)


def test_rate_limit_carries_retry_after():
    err = api_error(429, "x", retry_after=2.5)
    assert isinstance(err, LemmaRateLimitError)
    assert err.retry_after == 2.5


def test_rate_limit_retry_after_is_a_real_dataclass_field():
    # retry_after participates in repr/eq (not a bare class attribute set after init)
    err = api_error(429, "x", retry_after=2.5)
    assert "retry_after=2.5" in repr(err)
    assert err != api_error(429, "x", retry_after=9.0)
    assert err == api_error(429, "x", retry_after=2.5)


def test_connection_error_hierarchy():
    assert issubclass(LemmaTimeoutError, LemmaConnectionError)


def test_retryable_status_set_is_conservative():
    assert _RETRYABLE_STATUS == frozenset({429, 502, 503, 504})
    assert 500 not in _RETRYABLE_STATUS


def test_retry_after_seconds_parsing():
    assert _retry_after_seconds("2") == 2.0
    assert _retry_after_seconds(None) is None
    assert _retry_after_seconds("not-a-date") is None


def test_retry_delay_backoff_and_cap():
    assert _retry_delay(0) == 0.5
    assert _retry_delay(10) == 6.0  # capped
    assert _retry_delay(0, "3") == 3.0  # honors Retry-After
    assert _retry_delay(0, "9999") == 30.0  # Retry-After capped at 30s
