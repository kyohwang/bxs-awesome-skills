#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-.}"
OUT="${2:-mcp-scan-report.json}"
VERSION="0.4.3"

# pinned install+run (no latest)
uvx "mcp-scan@${VERSION}" --skills "$TARGET" --json > "$OUT"
echo "MCP_SCAN_OK version=${VERSION} out=${OUT}"
