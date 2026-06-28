from __future__ import annotations

import pytest

from lemma_stack.paths import LocalPaths


@pytest.fixture
def paths(tmp_path) -> LocalPaths:
    p = LocalPaths(root=tmp_path / "local")
    p.ensure()
    return p
