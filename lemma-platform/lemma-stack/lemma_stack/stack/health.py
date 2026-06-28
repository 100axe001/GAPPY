"""Health gates used by the start sequence."""

from __future__ import annotations

import time
import urllib.error
import urllib.request

from lemma_stack.output import AdminError
from lemma_stack.runtime.base import Runtime


def wait_container_healthy(runtime: Runtime, name: str, *, timeout: float = 180.0) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        status = runtime.container_health(name)
        if status == "healthy":
            return
        if not runtime.container_running(name):
            raise AdminError(f"{name} exited while waiting for it to become healthy")
        time.sleep(2)
    raise AdminError(f"{name} did not become healthy within {int(timeout)}s")


def wait_http(url: str, *, timeout: float = 180.0) -> None:
    deadline = time.monotonic() + timeout
    last_error: Exception | None = None
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                if 200 <= response.status < 500:
                    return
        except urllib.error.HTTPError as exc:
            # the server answered; auth/404-style responses still mean "up"
            if exc.code < 500:
                return
            last_error = exc
        except OSError as exc:
            last_error = exc
        time.sleep(2)
    detail = f" (last error: {last_error})" if last_error else ""
    raise AdminError(f"{url} did not respond within {int(timeout)}s{detail}")
