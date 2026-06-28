from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lemma_connectors.core.results import BinaryContentResult
from lemma_connectors.google_drive.generated.tool_types import DriveFilesExportToolOutput
from lemma_connectors.jira.generated.tool_types import GetAttachmentContentToolOutput


def test_binary_content_result_encodes_bytes_for_json_transport():
    result = BinaryContentResult.from_bytes(
        b"hello",
        media_type="text/plain",
        file_name="hello.txt",
    )

    assert result.type == "binary_content"
    assert result.media_type == "text/plain"
    assert result.file_name == "hello.txt"
    assert result.size_bytes == 5
    assert result.content_base64 == "aGVsbG8="


def test_generated_binary_tool_outputs_use_binary_content_model():
    export = DriveFilesExportToolOutput.model_validate(
        {
            "type": "binary_content",
            "content_base64": "aGVsbG8=",
            "media_type": "text/plain",
            "size_bytes": 5,
        }
    )
    attachment = GetAttachmentContentToolOutput.model_validate(
        {
            "type": "binary_content",
            "content_base64": "aGVsbG8=",
            "media_type": "text/plain",
            "size_bytes": 5,
        }
    )

    assert export.content_base64 == "aGVsbG8="
    assert attachment.media_type == "text/plain"
