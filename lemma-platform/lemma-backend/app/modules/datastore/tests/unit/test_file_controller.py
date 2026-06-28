from __future__ import annotations

from app.modules.datastore.api.controllers.file_controller import (
    build_content_disposition,
)


def test_build_content_disposition_supports_unicode_filename() -> None:
    filename = "Screenshot 2026-04-06 at 1.01.14\u202fPM.png"

    header = build_content_disposition("inline", filename)

    assert header == (
        'inline; filename="Screenshot 2026-04-06 at 1.01.14 PM.png"; '
        "filename*=UTF-8''Screenshot%202026-04-06%20at%201.01.14%E2%80%AFPM.png"
    )
    header.encode("latin-1")
