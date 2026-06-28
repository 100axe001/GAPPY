"""Filesystem layout of an installed local stack.

Everything the stack persists lives under one root (default ~/.lemma/local) so
backup, migration, and uninstall have a single directory to reason about.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_ROOT = Path.home() / ".lemma" / "local"

# Homebrew (Apple Silicon and Intel) plus the standard system dirs. A fresh
# Homebrew install or a GUI-spawned process often lacks these on PATH, so
# binaries we just installed (podman) or rely on (docker, gh) would be missed.
_PATH_EXTRAS = (
    "/opt/homebrew/bin",
    "/usr/local/bin",
    "/opt/podman/bin",  # official podman pkg / Podman Desktop
    "/usr/bin",
    "/bin",
    "/usr/sbin",
)


def enrich_path() -> None:
    """Append well-known tool locations to PATH for this process and children."""
    parts = [p for p in os.environ.get("PATH", "").split(os.pathsep) if p]
    for extra in _PATH_EXTRAS:
        if extra not in parts:
            parts.append(extra)
    os.environ["PATH"] = os.pathsep.join(parts)


def default_root() -> Path:
    override = os.environ.get("LEMMA_STACK_ROOT")
    return Path(override).expanduser() if override else DEFAULT_ROOT


@dataclass(frozen=True)
class LocalPaths:
    root: Path = field(default_factory=default_root)

    @property
    def config_file(self) -> Path:
        return self.root / "config.toml"

    @property
    def release_file(self) -> Path:
        return self.root / "release.json"

    @property
    def releases_dir(self) -> Path:
        return self.root / "releases"

    @property
    def data_dir(self) -> Path:
        return self.root / "data"

    @property
    def object_storage_dir(self) -> Path:
        return self.data_dir / "object-storage"

    @property
    def files_dir(self) -> Path:
        return self.data_dir / "files"

    @property
    def workspaces_dir(self) -> Path:
        return self.data_dir / "workspaces"

    @property
    def state_dir(self) -> Path:
        return self.root / "state"

    @property
    def run_dir(self) -> Path:
        return self.root / "run"

    @property
    def logs_dir(self) -> Path:
        return self.root / "logs"

    @property
    def backups_dir(self) -> Path:
        return self.root / "backups"

    @property
    def cache_dir(self) -> Path:
        return self.root / "cache"

    @property
    def postgres_init_dir(self) -> Path:
        return self.root / "postgres-init"

    @property
    def admin_log_file(self) -> Path:
        return self.logs_dir / "admin.log"

    def all_dirs(self) -> tuple[Path, ...]:
        return (
            self.root,
            self.releases_dir,
            self.data_dir,
            self.object_storage_dir,
            self.files_dir,
            self.workspaces_dir,
            self.state_dir,
            self.run_dir,
            self.logs_dir,
            self.backups_dir,
            self.cache_dir,
            self.postgres_init_dir,
        )

    def ensure(self) -> None:
        for path in self.all_dirs():
            path.mkdir(parents=True, exist_ok=True)
