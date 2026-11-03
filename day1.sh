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

# Ensure we have git configured
if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

# Pull latest commits cleanly
echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0016_3SumClosest.java
echo "[*] Committing [1/6]: LC0016 3Sum Closest..."
cp "staging/day1/LC0016_3SumClosest.java" "./LC0016_3SumClosest.java"
git add "LC0016_3SumClosest.java"
git commit -m "feat(leetcode): solve LC0016 3Sum Closest in Java"
sleep 2

# [2/6] LC0026_RemoveDuplicatesFromSortedArray.java
echo "[*] Committing [2/6]: LC0026 Remove Duplicates from Sorted Array..."
cp "staging/day1/LC0026_RemoveDuplicatesFromSortedArray.java" "./LC0026_RemoveDuplicatesFromSortedArray.java"
git add "LC0026_RemoveDuplicatesFromSortedArray.java"
git commit -m "feat(leetcode): solve LC0026 Remove Duplicates from Sorted Array in Java"
sleep 2

# [3/6] LC0075_SortColors.java
echo "[*] Committing [3/6]: LC0075 Sort Colors..."
cp "staging/day1/LC0075_SortColors.java" "./LC0075_SortColors.java"
git add "LC0075_SortColors.java"
git commit -m "feat(leetcode): solve LC0075 Sort Colors in Java"
sleep 2

# [4/6] LC0128_LongestConsecutiveSequence.java
echo "[*] Committing [4/6]: LC0128 Longest Consecutive Sequence..."
cp "staging/day1/LC0128_LongestConsecutiveSequence.java" "./LC0128_LongestConsecutiveSequence.java"
git add "LC0128_LongestConsecutiveSequence.java"
git commit -m "feat(leetcode): solve LC0128 Longest Consecutive Sequence in Java"
sleep 2

# [5/6] LC0167_TwoSumIIInputArrayIsSorted.java
echo "[*] Committing [5/6]: LC0167 Two Sum II - Input Array Is Sorted..."
cp "staging/day1/LC0167_TwoSumIIInputArrayIsSorted.java" "./LC0167_TwoSumIIInputArrayIsSorted.java"
git add "LC0167_TwoSumIIInputArrayIsSorted.java"
git commit -m "feat(leetcode): solve LC0167 Two Sum II - Input Array Is Sorted in Java"
sleep 2

# [6/6] LC0189_RotateArray.java
echo "[*] Committing [6/6]: LC0189 Rotate Array..."
cp "staging/day1/LC0189_RotateArray.java" "./LC0189_RotateArray.java"
git add "LC0189_RotateArray.java"
git commit -m "feat(leetcode): solve LC0189 Rotate Array in Java"
sleep 2

echo "[*] Pushing all 6 commits to GitHub..."
git push origin main

echo ""
echo "================================================================"
echo "✅ Day 1 COMPLETE: 6 new Java solutions pushed to GitHub!"
echo "================================================================"
