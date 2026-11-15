#!/bin/bash
# Master Daily Runner with Auto-Detector for Termux (Android) / Linux
# Usage:
#   ./run_day.sh         (AUTO MODE: auto-detects what is uploaded and runs next batch)
#   ./run_day.sh status  (CHECKS STATUS: shows upload detector table)
#   ./run_day.sh 1       (RUNS Day 1 explicitly)
#   ./run_day.sh 2       (RUNS Day 2 explicitly)
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

chmod +x auto_submit.sh

if [ "$1" == "status" ] || [ "$1" == "--status" ]; then
    bash auto_submit.sh --status
elif [ -n "$1" ]; then
    bash auto_submit.sh "$1"
else
    bash auto_submit.sh auto
fi
