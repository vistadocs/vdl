#!/usr/bin/env bash
# Install the corpus git hooks. Idempotent.
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
ln -sf ../../.ci/pre-push "$ROOT/.git/hooks/pre-push"
chmod +x "$ROOT/.ci/pre-push" "$ROOT/.git/hooks/pre-push" 2>/dev/null || true
echo "Installed pre-push hook → .git/hooks/pre-push"
