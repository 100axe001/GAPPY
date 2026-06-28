#!/bin/bash
# Generate SSL certificates for local development
# Supports mkcert (recommended) or openssl fallback

set -e

CERTS_DIR="${1:-./certs}"
mkdir -p "$CERTS_DIR"

echo "Generating SSL certificates in $CERTS_DIR..."

# Domains we need certificates for
DOMAINS=(
    "api.localhost"
    "auth.localhost"
    "*.apps.localhost"
    "apps.localhost"
)

# Check if mkcert is available (preferred for local dev)
if command -v mkcert &> /dev/null; then
    echo "Using mkcert for certificate generation..."

    # Install the local CA if not already done
    mkcert -install 2>/dev/null || true

    # Generate wildcard certificate for all domains
    # Note: mkcert handles wildcards properly for local development
    mkcert -cert-file "$CERTS_DIR/apps.localhost.pem" \
           -key-file "$CERTS_DIR/apps.localhost-key.pem" \
           localhost 127.0.0.1 ::1 *.apps.localhost apps.localhost api.localhost auth.localhost

    # Create individual symlinks/copies for clarity
    cp "$CERTS_DIR/apps.localhost.pem" "$CERTS_DIR/api.localhost.pem"
    cp "$CERTS_DIR/apps.localhost-key.pem" "$CERTS_DIR/api.localhost-key.pem"
    cp "$CERTS_DIR/apps.localhost.pem" "$CERTS_DIR/auth.localhost.pem"
    cp "$CERTS_DIR/apps.localhost-key.pem" "$CERTS_DIR/auth.localhost-key.pem"
    cp "$CERTS_DIR/apps.localhost.pem" "$CERTS_DIR/localhost.pem"
    cp "$CERTS_DIR/apps.localhost-key.pem" "$CERTS_DIR/localhost-key.pem"

    echo "✓ Certificates generated with mkcert (trusted by system)"

# Fallback to openssl
elif command -v openssl &> /dev/null; then
    echo "Using openssl for certificate generation (you'll need to trust the CA)..."

    # Generate CA key and cert
    openssl genrsa -out "$CERTS_DIR/ca-key.pem" 2048 2>/dev/null
    openssl req -new -x509 -key "$CERTS_DIR/ca-key.pem" -out "$CERTS_DIR/ca.pem" -days 365 \
        -subj "/C=US/ST=Local/L=Local/O=LocalDev/CN=LocalDev CA" 2>/dev/null

    # Generate server key
    openssl genrsa -out "$CERTS_DIR/server-key.pem" 2048 2>/dev/null

    # Create CSR config with SANs
    cat > "$CERTS_DIR/server.cnf" <<EOF
[req]
distinguished_name = req_distinguished_name
x509_extensions = v3_req
prompt = no

[req_distinguished_name]
CN = localhost

[v3_req]
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
DNS.2 = *.localhost
DNS.3 = *.apps.localhost
DNS.4 = apps.localhost
DNS.5 = api.localhost
DNS.6 = auth.localhost
IP.1 = 127.0.0.1
IP.2 = ::1
EOF

    # Generate CSR
    openssl req -new -key "$CERTS_DIR/server-key.pem" -out "$CERTS_DIR/server.csr" -config "$CERTS_DIR/server.cnf" 2>/dev/null

    # Sign with CA
    openssl x509 -req -in "$CERTS_DIR/server.csr" -CA "$CERTS_DIR/ca.pem" -CAkey "$CERTS_DIR/ca-key.pem" \
        -CAcreateserial -out "$CERTS_DIR/server.pem" -days 365 -extensions v3_req -extfile "$CERTS_DIR/server.cnf" 2>/dev/null

    # Copy to expected filenames
    cp "$CERTS_DIR/server.pem" "$CERTS_DIR/apps.localhost.pem"
    cp "$CERTS_DIR/server-key.pem" "$CERTS_DIR/apps.localhost-key.pem"
    cp "$CERTS_DIR/server.pem" "$CERTS_DIR/api.localhost.pem"
    cp "$CERTS_DIR/server-key.pem" "$CERTS_DIR/api.localhost-key.pem"
    cp "$CERTS_DIR/server.pem" "$CERTS_DIR/auth.localhost.pem"
    cp "$CERTS_DIR/server-key.pem" "$CERTS_DIR/auth.localhost-key.pem"
    cp "$CERTS_DIR/server.pem" "$CERTS_DIR/localhost.pem"
    cp "$CERTS_DIR/server-key.pem" "$CERTS_DIR/localhost-key.pem"

    # Cleanup intermediate files
    rm -f "$CERTS_DIR/server.cnf" "$CERTS_DIR/server.csr" "$CERTS_DIR/ca-key.pem" "$CERTS_DIR/ca.srl"

    echo "✓ Certificates generated with openssl"
    echo ""
    echo "⚠️  IMPORTANT: Trust the CA certificate to avoid browser warnings:"
    echo "   $CERTS_DIR/ca.pem"
    echo ""
    echo "   On macOS: sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain $CERTS_DIR/ca.pem"

else
    echo "❌ Error: Neither mkcert nor openssl is installed."
    echo "   Install mkcert: brew install mkcert (recommended)"
    echo "   Or install openssl: brew install openssl"
    exit 1
fi

echo ""
echo "Generated certificates:"
ls -la "$CERTS_DIR/"*.pem 2>/dev/null || true
echo ""
echo "Done! Run 'docker compose up' to start the stack."
