from __future__ import annotations

import sys
from pathlib import Path


def _ensure_local_lemma_connectors_on_path() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    lemma_src = repo_root / "lemma-connectors" / "src"
    lemma_src_str = str(lemma_src)
    if lemma_src.exists() and lemma_src_str not in sys.path:
        sys.path.insert(0, lemma_src_str)


_ensure_local_lemma_connectors_on_path()
