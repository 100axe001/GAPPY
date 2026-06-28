"""Runtime detection, selection, and podman installation.

First-run flow: detect docker/podman; if neither is usable, offer to install
podman (the recommended default). The choice persists in config.toml
[runtime].provider.
"""

from __future__ import annotations

import platform
import shutil
import subprocess
import time

import typer

from lemma_stack.output import AdminError, info, non_interactive, ok
from lemma_stack.runtime import machine
from lemma_stack.runtime.base import Runtime


def _cli_present(cli: str) -> bool:
    return shutil.which(cli) is not None


def _daemon_up(cli: str) -> bool:
    proc = subprocess.run([cli, "info"], capture_output=True, text=True, check=False)
    return proc.returncode == 0


def detect() -> dict[str, dict[str, bool]]:
    return {
        cli: {"installed": _cli_present(cli), "running": _cli_present(cli) and _daemon_up(cli)}
        for cli in ("podman", "docker")
    }


def install_podman() -> None:
    system = platform.system()
    if system == "Darwin":
        if not _cli_present("brew"):
            raise AdminError(
                "Homebrew is required to install podman on macOS. "
                "Install it from https://brew.sh and re-run, or install podman manually."
            )
        info("Installing podman via Homebrew…")
        subprocess.run(["brew", "install", "podman"], check=True)
    elif system == "Linux":
        for manager, args in (
            ("apt-get", ["sudo", "apt-get", "install", "-y", "podman"]),
            ("dnf", ["sudo", "dnf", "install", "-y", "podman"]),
            ("pacman", ["sudo", "pacman", "-Sy", "--needed", "--noconfirm", "podman"]),
        ):
            if _cli_present(manager):
                info(f"Installing podman via {manager}…")
                subprocess.run(args, check=True)
                break
        else:
            raise AdminError(
                "no supported package manager found; install podman manually "
                "(https://podman.io/docs/installation) and re-run"
            )
    else:
        raise AdminError(f"unsupported OS for automatic podman install: {system}")
    if not _cli_present("podman"):
        raise AdminError("podman install finished but the CLI is not on PATH; open a new shell")
    ok("podman installed")


def select_runtime(requested: str, *, assume_yes: bool) -> str:
    """Resolve 'auto'/'docker'/'podman' to a usable provider, installing podman if needed."""
    state = detect()

    if requested in {"docker", "podman"}:
        if not state[requested]["installed"]:
            if requested == "podman":
                install_podman()
            else:
                raise AdminError("docker CLI not found; install Docker or use --runtime podman")
        return requested

    if state["podman"]["installed"]:
        return "podman"
    if state["docker"]["installed"]:
        if non_interactive() or assume_yes:
            return "docker"
        if typer.confirm(
            "Docker found. Use Docker? (No installs Podman, the recommended runtime)",
            default=True,
        ):
            return "docker"
        install_podman()
        return "podman"

    # neither installed
    if non_interactive() or assume_yes:
        install_podman()
        return "podman"
    choice = typer.prompt(
        "No container runtime found. Install Podman (recommended)? [install/abort]",
        default="install",
    )
    if choice.strip().lower() not in {"install", "i", "yes", "y"}:
        raise AdminError("a container runtime is required; install docker or podman and re-run")
    install_podman()
    return "podman"


def _start_docker_desktop(runtime: Runtime, timeout_s: int = 90) -> bool:
    """macOS: launch Docker Desktop in the background and wait for the daemon."""
    if platform.system() != "Darwin":
        return False
    proc = subprocess.run(
        ["open", "-g", "-a", "Docker"], capture_output=True, text=True, check=False
    )
    if proc.returncode != 0:
        return False
    info("Starting Docker Desktop…")
    deadline = time.monotonic() + timeout_s
    while time.monotonic() < deadline:
        if runtime.available():
            return True
        time.sleep(2)
    return False


def ensure_ready(provider: str) -> Runtime:
    """Make the chosen runtime usable: start podman machine/socket or Docker Desktop."""
    runtime = Runtime(provider)
    if provider == "podman":
        machine.ensure_podman_ready(runtime)
    elif not runtime.available():
        _start_docker_desktop(runtime)
    if not runtime.available():
        hint = (
            "start Docker Desktop (or the docker service)"
            if provider == "docker"
            else "check `podman machine list` / `systemctl --user status podman.socket`"
        )
        raise AdminError(f"{provider} is installed but not responding; {hint}")
    return runtime
