"""E2E tests for the document-only file-indexing allow-list (P6).

These lock down the early indexing policy: only prose/document formats are ever
indexed. Tabular/data files (csv, json, xlsx) and images (png) land as
NOT_REQUIRED immediately and never surface in search, while .txt/.md become
COMPLETED once indexed. Disabling search on an indexed file synchronously
removes its chunks so it stops appearing in search.
"""

from __future__ import annotations

from uuid import UUID, uuid4

import pytest

from app.modules.datastore.tests.e2e.harness import (
    PAPERS,
    DatastoreApi,
    load_paper,
)

pytestmark = pytest.mark.e2e


async def _index(index_datastore_file, file_entity: dict) -> None:
    await index_datastore_file(UUID(file_entity["pod_id"]), UUID(file_entity["id"]))


def _file_ids(search_result: dict) -> set[str]:
    return {item["file_id"] for item in search_result.get("items", [])}


class TestIndexingAllowList:
    @pytest.mark.asyncio
    async def test_data_and_image_files_are_not_indexed(
        self,
        pod_api: DatastoreApi,
    ):
        """Casey uploads csv/json/xlsx/png; each is NOT_REQUIRED and unsearchable."""
        api = pod_api

        token = f"ZZData{uuid4().hex[:8]}"
        body = f"{token} tabular and binary payload".encode()
        cases = [
            ("data.csv", "text/csv"),
            ("config.json", "application/json"),
            (
                "budget.xlsx",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            ),
            ("diagram.png", "image/png"),
        ]

        uploaded = []
        for filename, content_type in cases:
            created = await api.upload_file(
                filename,
                body,
                content_type=content_type,
                search_enabled=True,
            )
            # Status is correct immediately at write time — no indexing pass.
            assert created["status"] == "NOT_REQUIRED", created
            uploaded.append(created)

        # Confirm the persisted status stays NOT_REQUIRED.
        for created in uploaded:
            fetched = await api.get_file(created["path"])
            assert fetched["status"] == "NOT_REQUIRED", fetched

        results = await api.search_files(token)
        found = _file_ids(results)
        assert all(created["id"] not in found for created in uploaded), found

    @pytest.mark.asyncio
    async def test_document_files_are_indexed_and_searchable(
        self,
        pod_api: DatastoreApi,
        index_datastore_file,
    ):
        """Casey uploads txt/md plus a real PDF paper; all reach COMPLETED and are searchable."""
        api = pod_api

        token = f"ZZDoc{uuid4().hex[:8]}"
        cases = [
            ("notes.txt", "text/plain"),
            ("readme.md", "text/markdown"),
        ]

        uploaded = []
        for filename, content_type in cases:
            created = await api.upload_file(
                filename,
                f"{token} indexable prose content for {filename}".encode(),
                content_type=content_type,
                search_enabled=True,
            )
            assert created["status"] == "PENDING", created
            await _index(index_datastore_file, created)
            uploaded.append(created)

        # A genuine arXiv PDF also reaches COMPLETED and is searchable by the
        # text Kreuzberg extracts from it (queried via its own needle, since the
        # random token above is not present in the real paper).
        seq2seq_paper = PAPERS["seq2seq"]
        pdf = await api.upload_file(
            seq2seq_paper.filename,
            load_paper("seq2seq"),
            content_type="application/pdf",
            search_enabled=True,
        )
        assert pdf["status"] == "PENDING", pdf
        await _index(index_datastore_file, pdf)

        for created in (*uploaded, pdf):
            fetched = await api.get_file(created["path"])
            assert fetched["status"] == "COMPLETED", fetched

        results = await api.search_files(token)
        found = _file_ids(results)
        for created in uploaded:
            assert created["id"] in found, (created, found)

        pdf_results = await api.search_files(seq2seq_paper.needle)
        assert pdf["id"] in _file_ids(pdf_results), pdf_results

    @pytest.mark.asyncio
    async def test_disabling_search_removes_indexed_chunks(
        self,
        pod_api: DatastoreApi,
        index_datastore_file,
    ):
        """Disabling search on an indexed .txt makes it NOT_REQUIRED and unsearchable."""
        api = pod_api

        token = f"ZZDisable{uuid4().hex[:8]}"
        created = await api.upload_file(
            "secret.txt",
            f"{token} originally searchable body".encode(),
            content_type="text/plain",
            search_enabled=True,
        )
        assert created["status"] == "PENDING"
        await _index(index_datastore_file, created)

        # Indexed and searchable before disabling.
        before = await api.search_files(token)
        assert created["id"] in _file_ids(before), before

        # Disable search → synchronous chunk + converted-artifact cleanup.
        updated = await api.update_file(created["path"], search_enabled=False)
        assert updated["search_enabled"] is False
        assert updated["status"] == "NOT_REQUIRED", updated

        fetched = await api.get_file(created["path"])
        assert fetched["status"] == "NOT_REQUIRED", fetched

        after = await api.search_files(token)
        assert created["id"] not in _file_ids(after), after
