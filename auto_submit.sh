#!/bin/bash
# =================================================================
# 🧠 Intelligent Auto-Detector & Daily Submissions Runner
# Automatically detects what has already been solved/pushed to GitHub
# and seamlessly runs the next pending batch without manual checking.
# Compatible with Termux (Android) and standard Linux/macOS bash.
# =================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================"
echo "⚡ LeetCode Auto-Detector & Submission Engine"
echo "================================================================"

# Verify git
if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

# Sync remote first
echo "[*] Fetching latest status from GitHub..."
git pull --rebase origin main 2>/dev/null || true

# Count total problems in root
TOTAL_ROOT=$(find . -maxdepth 1 -name "LC*.java" | wc -l | tr -d ' ')
echo "[*] Total Java solutions currently active in root: $TOTAL_ROOT"
echo "----------------------------------------------------------------"

# Scan staging/day1 through staging/day7
NEXT_DAY=""
ALL_DONE=true

for day in 1 2 3 4 5 6 7; do
    DAY_DIR="staging/day$day"
    if [ ! -d "$DAY_DIR" ]; then
        continue
    fi

    TOTAL_DAY=0
    DONE_DAY=0
    PENDING_FILES=()

    for f in "$DAY_DIR"/LC*.java; do
        [ -e "$f" ] || continue
        TOTAL_DAY=$((TOTAL_DAY + 1))
        BNAME=$(basename "$f")
        if [ -f "./$BNAME" ]; then
            DONE_DAY=$((DONE_DAY + 1))
        else
            PENDING_FILES+=("$BNAME")
        fi
    done

    if [ "$DONE_DAY" -eq "$TOTAL_DAY" ] && [ "$TOTAL_DAY" -gt 0 ]; then
        echo "  [✓] Day $day: Completed ($DONE_DAY/$TOTAL_DAY uploaded)"
    elif [ "$DONE_DAY" -gt 0 ] && [ "$DONE_DAY" -lt "$TOTAL_DAY" ]; then
        echo "  [⚡] Day $day: Partially complete ($DONE_DAY/$TOTAL_DAY uploaded, $((TOTAL_DAY - DONE_DAY)) pending)"
        if [ -z "$NEXT_DAY" ]; then
            NEXT_DAY="$day"
            ALL_DONE=false
        fi
    else
        echo "  [ ] Day $day: Queued (0/$TOTAL_DAY uploaded)"
        if [ -z "$NEXT_DAY" ]; then
            NEXT_DAY="$day"
            ALL_DONE=false
        fi
    fi
done

echo "----------------------------------------------------------------"

# Handle status check
if [ "$1" == "status" ] || [ "$1" == "--status" ] || [ "$1" == "-s" ]; then
    echo "[*] Status check complete."
    if [ "$ALL_DONE" = true ]; then
        echo "🎉 All 42 problems across Days 1-7 are fully submitted!"
    else
        echo "⚡ Next batch queued: DAY $NEXT_DAY. Run './auto_submit.sh' to execute."
    fi
    exit 0
fi

# If user provided a specific day parameter, respect it
if [ -n "$1" ] && [ "$1" != "auto" ] && [ "$1" != "--auto" ]; then
    TARGET_DAY="$1"
    echo "[!] User requested override: Day $TARGET_DAY"
else
    if [ "$ALL_DONE" = true ]; then
        echo "🎉 All 42 problems across Days 1-7 have already been submitted!"
        echo "[*] Nothing pending to upload. You're fully up-to-date!"
        exit 0
    fi
    TARGET_DAY="$NEXT_DAY"
    echo "⚡ Auto-detected next pending batch: DAY $TARGET_DAY"
fi

if [ ! -f "day${TARGET_DAY}.sh" ]; then
    echo "[-] Error: day${TARGET_DAY}.sh not found!"
    exit 1
fi

echo "[*] Launching execution for Day $TARGET_DAY..."
if command -v chmod &> /dev/null; then
    chmod +x "day${TARGET_DAY}.sh" || true
fi

sh "day${TARGET_DAY}.sh"
