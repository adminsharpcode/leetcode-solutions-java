#!/bin/bash
# =================================================================
# Day 2 LeetCode Submissions (6 Sequential Java Contributions)
# Compatible with Termux (Android) and standard Linux/macOS bash
# =================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================"
echo "🚀 Executing Day 2 Submissions (6 Problems in Java)"
echo "================================================================"

if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0085_MaximalRectangle.java
echo "[*] Processing [1/6]: LC0085 Maximal Rectangle..."
if [ -f "./LC0085_MaximalRectangle.java" ] && git ls-files --error-unmatch "./LC0085_MaximalRectangle.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0085_MaximalRectangle.java"; then
    echo "    [✓] LC0085_MaximalRectangle.java is already committed in git repository."
else
    cp "staging/day2/LC0085_MaximalRectangle.java" "./LC0085_MaximalRectangle.java"
    git add "LC0085_MaximalRectangle.java"
    git commit -m "feat(leetcode): solve LC0085 Maximal Rectangle in Java"
    echo "    [+] Committed [1/6]: LC0085 Maximal Rectangle"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [2/6] LC0316_RemoveDuplicateLetters.java
echo "[*] Processing [2/6]: LC0316 Remove Duplicate Letters..."
if [ -f "./LC0316_RemoveDuplicateLetters.java" ] && git ls-files --error-unmatch "./LC0316_RemoveDuplicateLetters.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0316_RemoveDuplicateLetters.java"; then
    echo "    [✓] LC0316_RemoveDuplicateLetters.java is already committed in git repository."
else
    cp "staging/day2/LC0316_RemoveDuplicateLetters.java" "./LC0316_RemoveDuplicateLetters.java"
    git add "LC0316_RemoveDuplicateLetters.java"
    git commit -m "feat(leetcode): solve LC0316 Remove Duplicate Letters in Java"
    echo "    [+] Committed [2/6]: LC0316 Remove Duplicate Letters"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [3/6] LC0394_DecodeString.java
echo "[*] Processing [3/6]: LC0394 Decode String..."
if [ -f "./LC0394_DecodeString.java" ] && git ls-files --error-unmatch "./LC0394_DecodeString.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0394_DecodeString.java"; then
    echo "    [✓] LC0394_DecodeString.java is already committed in git repository."
else
    cp "staging/day2/LC0394_DecodeString.java" "./LC0394_DecodeString.java"
    git add "LC0394_DecodeString.java"
    git commit -m "feat(leetcode): solve LC0394 Decode String in Java"
    echo "    [+] Committed [3/6]: LC0394 Decode String"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [4/6] LC0496_NextGreaterElementI.java
echo "[*] Processing [4/6]: LC0496 Next Greater Element I..."
if [ -f "./LC0496_NextGreaterElementI.java" ] && git ls-files --error-unmatch "./LC0496_NextGreaterElementI.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0496_NextGreaterElementI.java"; then
    echo "    [✓] LC0496_NextGreaterElementI.java is already committed in git repository."
else
    cp "staging/day2/LC0496_NextGreaterElementI.java" "./LC0496_NextGreaterElementI.java"
    git add "LC0496_NextGreaterElementI.java"
    git commit -m "feat(leetcode): solve LC0496 Next Greater Element I in Java"
    echo "    [+] Committed [4/6]: LC0496 Next Greater Element I"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [5/6] LC0503_NextGreaterElementII.java
echo "[*] Processing [5/6]: LC0503 Next Greater Element II..."
if [ -f "./LC0503_NextGreaterElementII.java" ] && git ls-files --error-unmatch "./LC0503_NextGreaterElementII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0503_NextGreaterElementII.java"; then
    echo "    [✓] LC0503_NextGreaterElementII.java is already committed in git repository."
else
    cp "staging/day2/LC0503_NextGreaterElementII.java" "./LC0503_NextGreaterElementII.java"
    git add "LC0503_NextGreaterElementII.java"
    git commit -m "feat(leetcode): solve LC0503 Next Greater Element II in Java"
    echo "    [+] Committed [5/6]: LC0503 Next Greater Element II"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [6/6] LC0739_DailyTemperatures.java
echo "[*] Processing [6/6]: LC0739 Daily Temperatures..."
if [ -f "./LC0739_DailyTemperatures.java" ] && git ls-files --error-unmatch "./LC0739_DailyTemperatures.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0739_DailyTemperatures.java"; then
    echo "    [✓] LC0739_DailyTemperatures.java is already committed in git repository."
else
    cp "staging/day2/LC0739_DailyTemperatures.java" "./LC0739_DailyTemperatures.java"
    git add "LC0739_DailyTemperatures.java"
    git commit -m "feat(leetcode): solve LC0739 Daily Temperatures in Java"
    echo "    [+] Committed [6/6]: LC0739 Daily Temperatures"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

echo "================================================================"
echo "[*] Day 2 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 2 complete! 6 contributions pushed to GitHub."
echo "================================================================"
