#!/bin/bash
# Master Daily Runner for Termux (Android) / Linux
# Usage:
#   ./run_day.sh 1   (runs Day 1)
#   ./run_day.sh 2   (runs Day 2)
#   ...
#   ./run_day.sh     (prompts for Day 1-7)
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

DAY="$1"
if [ -z "$DAY" ]; then
    echo "=================================================="
    echo "⚡ LeetCode Daily Submissions Runner (Android/Termux) ⚡"
    echo "=================================================="
    echo "Which day would you like to submit? (1 - 7): "
    read -r DAY
fi

if [ ! -f "day${DAY}.sh" ]; then
    echo "[-] Error: Invalid day \"$DAY\". Please choose between 1 and 7."
    exit 1
fi

chmod +x "day${DAY}.sh"
bash "day${DAY}.sh"
