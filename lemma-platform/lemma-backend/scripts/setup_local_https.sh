#!/bin/zsh

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
CERT_FILE="$ROOT_DIR/localhost+2.pem"
KEY_FILE="$ROOT_DIR/localhost+2-key.pem"

if ! command -v mkcert >/dev/null 2>&1; then
  echo "mkcert is required. Install it with: brew install mkcert"
  exit 1
fi

echo "Installing/trusting the local mkcert CA in macOS keychains..."
mkcert -install

echo "Generating localhost certificates for nginx..."
(
  cd "$ROOT_DIR"
  mkcert -cert-file "$CERT_FILE" -key-file "$KEY_FILE" localhost 127.0.0.1 ::1
)

echo
echo "Local HTTPS is ready."
echo "Next steps:"
echo "  1. Restart nginx: docker compose up -d --force-recreate nginx"
echo "  2. Open https://localhost"
