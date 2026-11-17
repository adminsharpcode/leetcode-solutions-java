#!/bin/bash
# =================================================================
# Day 4 LeetCode Submissions (6 Sequential Java Contributions)
# Compatible with Termux (Android) and standard Linux/macOS bash
# =================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================"
echo "🚀 Executing Day 4 Submissions (6 Problems in Java)"
echo "================================================================"

if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0057_InsertInterval.java
echo "[*] Processing [1/6]: LC0057 Insert Interval..."
if [ -f "./LC0057_InsertInterval.java" ] && git ls-files --error-unmatch "./LC0057_InsertInterval.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0057_InsertInterval.java"; then
    echo "    [✓] LC0057_InsertInterval.java is already committed in git repository."
else
    cp "staging/day4/LC0057_InsertInterval.java" "./LC0057_InsertInterval.java"
    git add "LC0057_InsertInterval.java"
    git commit -m "feat(leetcode): solve LC0057 Insert Interval in Java"
    echo "    [+] Committed [1/6]: LC0057 Insert Interval"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [2/6] LC0081_SearchInRotatedSortedArrayII.java
echo "[*] Processing [2/6]: LC0081 Search in Rotated Sorted Array II..."
if [ -f "./LC0081_SearchInRotatedSortedArrayII.java" ] && git ls-files --error-unmatch "./LC0081_SearchInRotatedSortedArrayII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0081_SearchInRotatedSortedArrayII.java"; then
    echo "    [✓] LC0081_SearchInRotatedSortedArrayII.java is already committed in git repository."
else
    cp "staging/day4/LC0081_SearchInRotatedSortedArrayII.java" "./LC0081_SearchInRotatedSortedArrayII.java"
    git add "LC0081_SearchInRotatedSortedArrayII.java"
    git commit -m "feat(leetcode): solve LC0081 Search in Rotated Sorted Array II in Java"
    echo "    [+] Committed [2/6]: LC0081 Search in Rotated Sorted Array II"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [3/6] LC0162_FindPeakElement.java
echo "[*] Processing [3/6]: LC0162 Find Peak Element..."
if [ -f "./LC0162_FindPeakElement.java" ] && git ls-files --error-unmatch "./LC0162_FindPeakElement.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0162_FindPeakElement.java"; then
    echo "    [✓] LC0162_FindPeakElement.java is already committed in git repository."
else
    cp "staging/day4/LC0162_FindPeakElement.java" "./LC0162_FindPeakElement.java"
    git add "LC0162_FindPeakElement.java"
    git commit -m "feat(leetcode): solve LC0162 Find Peak Element in Java"
    echo "    [+] Committed [3/6]: LC0162 Find Peak Element"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [4/6] LC0278_FirstBadVersion.java
echo "[*] Processing [4/6]: LC0278 First Bad Version..."
if [ -f "./LC0278_FirstBadVersion.java" ] && git ls-files --error-unmatch "./LC0278_FirstBadVersion.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0278_FirstBadVersion.java"; then
    echo "    [✓] LC0278_FirstBadVersion.java is already committed in git repository."
else
    cp "staging/day4/LC0278_FirstBadVersion.java" "./LC0278_FirstBadVersion.java"
    git add "LC0278_FirstBadVersion.java"
    git commit -m "feat(leetcode): solve LC0278 First Bad Version in Java"
    echo "    [+] Committed [4/6]: LC0278 First Bad Version"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [5/6] LC0704_BinarySearch.java
echo "[*] Processing [5/6]: LC0704 Binary Search..."
if [ -f "./LC0704_BinarySearch.java" ] && git ls-files --error-unmatch "./LC0704_BinarySearch.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0704_BinarySearch.java"; then
    echo "    [✓] LC0704_BinarySearch.java is already committed in git repository."
else
    cp "staging/day4/LC0704_BinarySearch.java" "./LC0704_BinarySearch.java"
    git add "LC0704_BinarySearch.java"
    git commit -m "feat(leetcode): solve LC0704 Binary Search in Java"
    echo "    [+] Committed [5/6]: LC0704 Binary Search"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [6/6] LC0875_KokoEatingBananas.java
echo "[*] Processing [6/6]: LC0875 Koko Eating Bananas..."
if [ -f "./LC0875_KokoEatingBananas.java" ] && git ls-files --error-unmatch "./LC0875_KokoEatingBananas.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0875_KokoEatingBananas.java"; then
    echo "    [✓] LC0875_KokoEatingBananas.java is already committed in git repository."
else
    cp "staging/day4/LC0875_KokoEatingBananas.java" "./LC0875_KokoEatingBananas.java"
    git add "LC0875_KokoEatingBananas.java"
    git commit -m "feat(leetcode): solve LC0875 Koko Eating Bananas in Java"
    echo "    [+] Committed [6/6]: LC0875 Koko Eating Bananas"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

echo "================================================================"
echo "[*] Day 4 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 4 complete! 6 contributions pushed to GitHub."
echo "================================================================"
