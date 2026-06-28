import os
import json
from pathlib import Path
from lemma_sdk import Pod

def get_lemma_pod() -> Pod:
    # 1. Check if environment variables are set explicitly
    pod_id = os.getenv("LEMMA_POD_ID")
    org_id = os.getenv("LEMMA_ORG_ID")
    token = os.getenv("LEMMA_TOKEN")
    base_url = os.getenv("LEMMA_BASE_URL")
    
    # 2. If environment variables are missing, fallback to parsing ~/.lemma/config.json
    if not (pod_id and org_id and token):
        config_paths = [
            Path("/root/.lemma/config.json"),
            Path.home() / ".lemma" / "config.json"
        ]
        
        config = {}
        for path in config_paths:
            if path.exists():
                try:
                    with open(path, "r") as f:
                        config = json.load(f)
                    break
                except Exception:
                    pass
        
        if config:
            active_server = config.get("active_server", "local")
            server_config = config.get("servers", {}).get(active_server, {})
            auth_config = server_config.get("auth", {})
            defaults = server_config.get("defaults", {})
            
            if not token:
                token = auth_config.get("access_token") or server_config.get("token")
            if not pod_id:
                pod_id = defaults.get("pod_id")
            if not org_id:
                org_id = defaults.get("org_id")
            if not base_url:
                base_url = auth_config.get("base_url") or server_config.get("base_url")

    # 3. Handle Docker DNS mapping
    # If running inside docker, the container backend is reachable at http://lemma-local-backend:8000
    # instead of http://127-0-0-1.sslip.io:8711
    is_docker = os.path.exists("/.dockerenv")
    if is_docker and (not base_url or "127-0-0-1.sslip.io" in base_url or "localhost" in base_url):
        base_url = "http://lemma-local-backend:8000"

    # Make sure we have the required fields
    if not pod_id:
        raise ValueError("LEMMA_POD_ID not found in environment or config.json")
    if not token:
        raise ValueError("LEMMA_TOKEN not found in environment or config.json")

    # Disable SSL verification for local self-signed setups
    os.environ["LEMMA_SSL_NO_VERIFY"] = "1"
    
    return Pod(
        pod_id=pod_id,
        org_id=org_id,
        token=token,
        base_url=base_url,
        verify_ssl=False
    )
