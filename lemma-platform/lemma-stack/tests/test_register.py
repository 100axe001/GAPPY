from __future__ import annotations

import json

from lemma_stack import register


def test_register_creates_cli_config(tmp_path, monkeypatch):
    cli_config = tmp_path / "config.json"
    monkeypatch.setenv("LEMMA_CONFIG_FILE", str(cli_config))

    register.register_local_server(
        base_url="http://localhost:8711/",
        auth_url="http://localhost:3711/auth",
        make_active=True,
    )

    config = json.loads(cli_config.read_text())
    server = config["servers"]["local"]
    assert server["base_url"] == "http://localhost:8711"  # trailing slash stripped
    assert server["auth_url"] == "http://localhost:3711/auth"
    assert server["defaults"] == {}
    assert config["active_server"] == "local"


def test_register_preserves_existing_servers_and_tokens(tmp_path, monkeypatch):
    cli_config = tmp_path / "config.json"
    # shape produced by lemma-cli's upsert_server()
    cli_config.write_text(
        json.dumps(
            {
                "active_server": "cloud",
                "servers": {
                    "cloud": {
                        "base_url": "https://api.lemma.work",
                        "auth_url": "https://lemma.work/auth",
                        "token": "tok-cloud",
                        "defaults": {"org_id": "o-1"},
                    },
                    "local": {
                        "base_url": "http://localhost:9999",
                        "token": "tok-local",
                        "defaults": {"pod_id": "p-1"},
                    },
                },
            }
        )
    )
    monkeypatch.setenv("LEMMA_CONFIG_FILE", str(cli_config))

    register.register_local_server(
        base_url="http://localhost:8711",
        auth_url="http://localhost:3711/auth",
    )

    config = json.loads(cli_config.read_text())
    # active server untouched (already set), cloud untouched, local token/defaults kept
    assert config["active_server"] == "cloud"
    assert config["servers"]["cloud"]["token"] == "tok-cloud"
    local = config["servers"]["local"]
    assert local["base_url"] == "http://localhost:8711"
    assert local["token"] == "tok-local"
    assert local["defaults"] == {"pod_id": "p-1"}
