"""Offline golden-path test: the scaffold -> author -> validate portion of the
first-run flow that needs no backend. The full live chain (import -> run function
-> call agent -> app load -> workflow+form) requires an ephemeral backend and is
tracked separately.
"""

from pathlib import Path

from lemma_cli.cli_app.pod_bundle import loads_jsonc
from lemma_cli.cli_app.scaffold import init_pod, init_resource, validate_workflow


def test_golden_offline_firstrun_path(tmp_path: Path):
    # 1. Scaffold a complete starter pod (pod.json + table + function + agent).
    pod_dir = tmp_path / "demo"
    init_pod(pod_dir, "Demo Ops")
    assert (pod_dir / "pod.json").is_file()
    assert (pod_dir / "tables").is_dir()
    assert (pod_dir / "agents").is_dir()

    # 2. Author one of every other resource kind into the bundle.
    init_resource("workflow", "review", root=pod_dir)
    init_resource("function", "score_lead", root=pod_dir)
    init_resource("table", "leads", root=pod_dir)

    # 3. Every resource JSON in the bundle parses (no malformed scaffold output).
    json_files = list(pod_dir.rglob("*.json"))
    assert json_files, "scaffold produced no JSON"
    for path in json_files:
        loads_jsonc(path.read_text(encoding="utf-8"))  # raises on malformed JSONC

    # 4. Every scaffolded workflow validates clean (incl. the start.* namespace guard).
    workflow_files = list((pod_dir / "workflows").rglob("*.json"))
    assert workflow_files, "no workflow scaffolded"
    for path in workflow_files:
        issues = validate_workflow(loads_jsonc(path.read_text(encoding="utf-8")))
        assert issues == [], (path.name, issues)
