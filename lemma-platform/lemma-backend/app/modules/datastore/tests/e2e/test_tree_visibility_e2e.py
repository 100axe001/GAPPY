"""E2E: directory-tree nodes carry `visibility` (so bundle export can tell
pod-shared from personal entries without a per-file fetch)."""

from __future__ import annotations

import pytest

from app.modules.datastore.tests.e2e.harness import DatastoreApi

pytestmark = pytest.mark.e2e


def _by_path(tree_payload: dict) -> dict[str, dict]:
    nodes: dict[str, dict] = {}

    def walk(node: dict) -> None:
        nodes[node["path"]] = node
        for child in node.get("children") or []:
            walk(child)

    walk(tree_payload["tree"])
    return nodes


class TestTreeVisibility:
    @pytest.mark.asyncio
    async def test_tree_nodes_carry_visibility(self, pod_api: DatastoreApi):
        await pod_api.create_folder("/shared-docs")  # POD by default
        await pod_api.upload_file(
            "a.md", b"x", directory_path="/shared-docs", search_enabled=False
        )
        await pod_api.create_folder("/me/notes")  # PERSONAL

        nodes = _by_path(await pod_api.tree(root_path="/", files_per_directory=10))

        assert nodes["/shared-docs"]["visibility"] == "POD"
        assert nodes["/shared-docs/a.md"]["visibility"] == "POD"
        # The synthetic /me root is personal.
        assert nodes["/me"]["visibility"] == "PERSONAL"
