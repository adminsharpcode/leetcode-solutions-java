#!/bin/bash
# =================================================================
# Day 1 LeetCode Submissions (6 Sequential Java Contributions)
# Compatible with Termux (Android) and standard Linux/macOS bash
# =================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================"
echo "🚀 Executing Day 1 Submissions (6 Problems in Java)"
echo "================================================================"

if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0018_4Sum.java
echo "[*] Processing [1/6]: LC0018 4Sum..."
if [ -f "./LC0018_4Sum.java" ] && git ls-files --error-unmatch "./LC0018_4Sum.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0018_4Sum.java"; then
    echo "    [✓] LC0018_4Sum.java is already committed in git repository."
else
    cp "staging/day1/LC0018_4Sum.java" "./LC0018_4Sum.java"
    git add "LC0018_4Sum.java"
    git commit -m "feat(leetcode): solve LC0018 4Sum in Java"
    echo "    [+] Committed [1/6]: LC0018 4Sum"
    sleep 2
fi

# [2/6] LC0027_RemoveElement.java
echo "[*] Processing [2/6]: LC0027 Remove Element..."
if [ -f "./LC0027_RemoveElement.java" ] && git ls-files --error-unmatch "./LC0027_RemoveElement.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0027_RemoveElement.java"; then
    echo "    [✓] LC0027_RemoveElement.java is already committed in git repository."
else
    cp "staging/day1/LC0027_RemoveElement.java" "./LC0027_RemoveElement.java"
    git add "LC0027_RemoveElement.java"
    git commit -m "feat(leetcode): solve LC0027 Remove Element in Java"
    echo "    [+] Committed [2/6]: LC0027 Remove Element"
    sleep 2
fi

# [3/6] LC0080_RemoveDuplicatesFromSortedArrayII.java
echo "[*] Processing [3/6]: LC0080 Remove Duplicates from Sorted Array II..."
if [ -f "./LC0080_RemoveDuplicatesFromSortedArrayII.java" ] && git ls-files --error-unmatch "./LC0080_RemoveDuplicatesFromSortedArrayII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0080_RemoveDuplicatesFromSortedArrayII.java"; then
    echo "    [✓] LC0080_RemoveDuplicatesFromSortedArrayII.java is already committed in git repository."
else
    cp "staging/day1/LC0080_RemoveDuplicatesFromSortedArrayII.java" "./LC0080_RemoveDuplicatesFromSortedArrayII.java"
    git add "LC0080_RemoveDuplicatesFromSortedArrayII.java"
    git commit -m "feat(leetcode): solve LC0080 Remove Duplicates from Sorted Array II in Java"
    echo "    [+] Committed [3/6]: LC0080 Remove Duplicates from Sorted Array II"
    sleep 2
fi

# [4/6] LC0088_MergeSortedArray.java
echo "[*] Processing [4/6]: LC0088 Merge Sorted Array..."
if [ -f "./LC0088_MergeSortedArray.java" ] && git ls-files --error-unmatch "./LC0088_MergeSortedArray.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0088_MergeSortedArray.java"; then
    echo "    [✓] LC0088_MergeSortedArray.java is already committed in git repository."
else
    cp "staging/day1/LC0088_MergeSortedArray.java" "./LC0088_MergeSortedArray.java"
    git add "LC0088_MergeSortedArray.java"
    git commit -m "feat(leetcode): solve LC0088 Merge Sorted Array in Java"
    echo "    [+] Committed [4/6]: LC0088 Merge Sorted Array"
    sleep 2
fi

# [5/6] LC0209_MinimumSizeSubarraySum.java
echo "[*] Processing [5/6]: LC0209 Minimum Size Subarray Sum..."
if [ -f "./LC0209_MinimumSizeSubarraySum.java" ] && git ls-files --error-unmatch "./LC0209_MinimumSizeSubarraySum.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0209_MinimumSizeSubarraySum.java"; then
    echo "    [✓] LC0209_MinimumSizeSubarraySum.java is already committed in git repository."
else
    cp "staging/day1/LC0209_MinimumSizeSubarraySum.java" "./LC0209_MinimumSizeSubarraySum.java"
    git add "LC0209_MinimumSizeSubarraySum.java"
    git commit -m "feat(leetcode): solve LC0209 Minimum Size Subarray Sum in Java"
    echo "    [+] Committed [5/6]: LC0209 Minimum Size Subarray Sum"
    sleep 2
fi

# [6/6] LC0283_MoveZeroes.java
echo "[*] Processing [6/6]: LC0283 Move Zeroes..."
if [ -f "./LC0283_MoveZeroes.java" ] && git ls-files --error-unmatch "./LC0283_MoveZeroes.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0283_MoveZeroes.java"; then
    echo "    [✓] LC0283_MoveZeroes.java is already committed in git repository."
else
    cp "staging/day1/LC0283_MoveZeroes.java" "./LC0283_MoveZeroes.java"
    git add "LC0283_MoveZeroes.java"
    git commit -m "feat(leetcode): solve LC0283 Move Zeroes in Java"
    echo "    [+] Committed [6/6]: LC0283 Move Zeroes"
    sleep 2
fi

echo "================================================================"
echo "[*] Day 1 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 1 complete! 6 contributions pushed to GitHub."
echo "================================================================"
