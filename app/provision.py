#!/usr/bin/env python3
"""
Provision the LifeOS Lemma pod.

Idempotent: creates the `lifeos` pod (if missing) and imports the bundle in pod/lifeos
(tables, agents, functions, workflows, schedules). Prints the LEMMA_ORG_ID / LEMMA_POD_ID
to wire into the app (docker-compose reads them, defaults are already baked in).

Prerequisites (one-time, on the Lemma stack):
    lemma-stack config set LEMMA_DEFAULT_MODEL_TYPE openai_compat
    lemma-stack config set LEMMA_OPENAI_API_KEY sk-...
    lemma-stack config set COMPOSIO_API_KEY <composio-api-key>   # optional, for extra connectors
    lemma-stack restart
    # then import the native connector catalog inside the backend container:
    docker exec lemma-local-backend python scripts/import_connector_catalog.py

Usage:
    python app/provision.py            # create + import
    python app/provision.py --org <ORG_ID>
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

POD_NAME = "lifeos"
BUNDLE = Path(__file__).resolve().parent.parent / "pod" / "lifeos"
DEFAULT_ORG = "019f0d47-91d9-7314-9376-8a2a47900bea"


def lemma(*args, org=None):
    env_args = ["--org", org] if org else []
    cmd = ["lemma", *args]
    return subprocess.run(cmd, capture_output=True, text=True,
                          env={**_env(org)})


def _env(org):
    import os
    e = dict(os.environ)
    if org:
        e["LEMMA_ORG_ID"] = org
    return e


def _pods(org):
    r = subprocess.run(["lemma", "pods", "list", "--json"], capture_output=True, text=True,
                       env=_env(org))
    try:
        data = json.loads(r.stdout)
        return data if isinstance(data, list) else data.get("items", [])
    except Exception:
        return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--org", default=DEFAULT_ORG)
    args = ap.parse_args()
    org = args.org

    pods = {p.get("name"): p.get("id") for p in _pods(org)}
    pod_id = pods.get(POD_NAME)

    if not pod_id:
        print(f"Creating pod '{POD_NAME}'...")
        subprocess.run(["lemma", "pods", "create", POD_NAME, "--org", org], check=True, env=_env(org))
        pods = {p.get("name"): p.get("id") for p in _pods(org)}
        pod_id = pods.get(POD_NAME)
    else:
        print(f"Pod '{POD_NAME}' already exists: {pod_id}")

    if not pod_id:
        print("ERROR: could not resolve pod id after create", file=sys.stderr)
        sys.exit(1)

    print(f"Importing bundle {BUNDLE} ...")
    r = subprocess.run(["lemma", "pods", "import", str(BUNDLE), "--pod", pod_id],
                       env=_env(org))
    if r.returncode != 0:
        sys.exit(r.returncode)

    print("\nProvisioned. Wire these into the app (docker-compose already defaults to them):")
    print(f"  LEMMA_ORG_ID={org}")
    print(f"  LEMMA_POD_ID={pod_id}")


if __name__ == "__main__":
    main()
