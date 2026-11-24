#!/bin/bash
# Master Daily Runner with Auto-Detector for Termux (Android) / Linux
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if command -v chmod &> /dev/null; then
    chmod +x auto_submit.sh || true
fi

if [ "$1" == "status" ] || [ "$1" == "--status" ]; then
    sh auto_submit.sh --status
elif [ -n "$1" ]; then
    sh auto_submit.sh "$1"
else
    sh auto_submit.sh auto
fi
