"""Unit test configuration for workspace module."""

from __future__ import annotations

import sys
from pathlib import Path


BACKEND_DIR = Path(__file__).resolve().parents[5]
REPO_DIR = BACKEND_DIR.parent
LEMMA_PYTHON_DIR = REPO_DIR / "lemma-python"
if str(LEMMA_PYTHON_DIR) not in sys.path:
    sys.path.insert(0, str(LEMMA_PYTHON_DIR))
