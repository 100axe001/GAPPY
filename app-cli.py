#!/usr/bin/env python3
import os
import sys
import json
import webbrowser
import urllib.request
import urllib.parse
from pathlib import Path

CONFIG_DIR = Path.home() / ".lifeos"
CONFIG_FILE = CONFIG_DIR / "cli_config.json"
DEFAULT_API_URL = "http://localhost:8081"

def load_config() -> dict:
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {"api_url": DEFAULT_API_URL, "token": None}

def save_config(config: dict):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def request_api(endpoint: str, method: str = "GET", data: dict = None, token: str = None, api_url: str = DEFAULT_API_URL) -> dict:
    url = f"{api_url}{endpoint}"
    req_headers = {"Accept": "application/json"}
    if token:
        req_headers["Authorization"] = f"Bearer {token}"
        
    req_data = None
    if data:
        req_headers["Content-Type"] = "application/json"
        req_data = json.dumps(data).encode("utf-8")
        
    req = urllib.request.Request(url, data=req_data, headers=req_headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            resp_body = resp.read().decode("utf-8")
            if resp_body:
                return json.loads(resp_body)
            return {}
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        try:
            err_json = json.loads(err_msg)
            detail = err_json.get("detail", err_msg)
        except Exception:
            detail = err_msg
        print(f"Error ({e.code}): {detail}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Failed to connect to LifeOS backend at {api_url}: {e.reason}")
        print("Please check if the FastAPI server / Docker stack is running.")
        sys.exit(1)

def do_login(email: str = None, password: str = None):
    config = load_config()
    if not email:
        email = input("Email: ").strip()
    if not password:
        import getpass
        password = getpass.getpass("Password: ")
        
    resp = request_api(
        "/api/auth/login",
        method="POST",
        data={"email": email, "password": password},
        api_url=config["api_url"]
    )
    
    config["token"] = resp.get("access_token")
    save_config(config)
    print("Login successful! Token saved locally.")

def require_token(config: dict) -> str:
    token = config.get("token")
    if not token:
        print("Not logged in. Please run './app login' first.")
        sys.exit(1)
    return token

def do_integrations_list():
    config = load_config()
    token = require_token(config)
    resp = request_api("/api/integrations", token=token, api_url=config["api_url"])
    
    print("\nAvailable Integrations:\n")
    print(f"{'Name':<20} | {'Status':<12} | {'Health':<8} | {'Connected Email'}")
    print("-" * 70)
    for item in resp:
        name = item.get("name", "")
        connected = "Connected" if item.get("is_connected") else "Disconnected"
        health = item.get("health_status", "healthy")
        email = item.get("metadata_json", {}).get("email", "N/A")
        print(f"{name:<20} | {connected:<12} | {health:<8} | {email}")
    print()

def do_integrations_connect(name: str):
    # Normalize google-calendar CLI arg to google_calendar backend parameter
    normalized_name = name.replace("-", "_")
    
    config = load_config()
    token = require_token(config)
    
    resp = request_api(f"/api/integrations/{normalized_name}/auth-url", token=token, api_url=config["api_url"])
    auth_url = resp.get("auth_url")
    if not auth_url:
        print("Could not retrieve connection auth URL from backend.")
        sys.exit(1)
        
    print(f"Opening OAuth URL in browser to connect {name}...")
    print(f"URL: {auth_url}")
    webbrowser.open(auth_url)
    print("\nComplete the connection in your browser. Once completed, verify connection using:")
    print(f"  ./app integrations status\n")

def do_integrations_disconnect(name: str):
    normalized_name = name.replace("-", "_")
    config = load_config()
    token = require_token(config)
    request_api(f"/api/integrations/{normalized_name}", method="DELETE", token=token, api_url=config["api_url"])
    print(f"Successfully disconnected {name}.")

def do_integrations_status():
    do_integrations_list()

def do_integrations_test(name: str):
    normalized_name = name.replace("-", "_")
    config = load_config()
    token = require_token(config)
    
    print(f"Testing connection health for {name}...")
    resp = request_api(f"/api/integrations/{normalized_name}/test", method="POST", token=token, api_url=config["api_url"])
    status = resp.get("status", "unknown")
    if status == "healthy":
        print(f"Connection to {name} is Healthy!")
    else:
        err = resp.get("error_message", "Unknown error")
        print(f"Connection to {name} is Unhealthy.")
        print(f"Error details: {err}")

def do_query(prompt: str):
    config = load_config()
    token = require_token(config)
    
    print("AI Assistant thinking...")
    resp = request_api(
        "/api/assistant/query",
        method="POST",
        data={"query": prompt},
        token=token,
        api_url=config["api_url"]
    )
    
    print("\nAssistant Response:\n")
    print(resp.get("response_message", "No response received."))
    print()

def main():
    if len(sys.argv) < 2:
        print("Usage: ./app <command> [args]")
        print("\nCommands:")
        print("  login                         Log in to LifeOS host")
        print("  integrations list             List connection status of integrations")
        print("  integrations connect <name>    Connect an integration (e.g. google-calendar)")
        print("  integrations disconnect <name> Disconnect an integration")
        print("  integrations status           Show status of all integrations")
        print("  integrations test <name>      Test connectivity of an integration")
        print("  query \"<prompt>\"              Send natural language command to AI Assistant")
        sys.exit(0)

    cmd = sys.argv[1]
    
    if cmd == "login":
        email = sys.argv[2] if len(sys.argv) > 2 else None
        password = sys.argv[3] if len(sys.argv) > 3 else None
        do_login(email, password)
    elif cmd == "query":
        if len(sys.argv) < 3:
            print("Please specify a prompt query: ./app query \"What's on my calendar today?\"")
            sys.exit(1)
        do_query(sys.argv[2])
    elif cmd == "integrations":
        if len(sys.argv) < 3:
            print("Usage: ./app integrations [list|connect|disconnect|status|test] [name]")
            sys.exit(1)
        subcmd = sys.argv[2]
        if subcmd in ("list", "status"):
            do_integrations_list()
        elif subcmd in ("connect", "disconnect", "test"):
            if len(sys.argv) < 4:
                print(f"Please specify integration name: ./app integrations {subcmd} google-calendar")
                sys.exit(1)
            name = sys.argv[3]
            if subcmd == "connect":
                do_integrations_connect(name)
            elif subcmd == "disconnect":
                do_integrations_disconnect(name)
            elif subcmd == "test":
                do_integrations_test(name)
        else:
            print(f"Unknown integrations subcommand: {subcmd}")
            sys.exit(1)
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
