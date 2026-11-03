#!/bin/bash
# =================================================================
# Day 7 LeetCode Submissions (6 Sequential Java Contributions)
# Compatible with Termux (Android) and standard Linux/macOS bash
# =================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================"
echo "🚀 Executing Day 7 Submissions (6 Problems in Java)"
echo "================================================================"

# Ensure we have git configured
if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

# Pull latest commits cleanly
echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0072_EditDistance.java
echo "[*] Committing [1/6]: LC0072 Edit Distance..."
cp "staging/day7/LC0072_EditDistance.java" "./LC0072_EditDistance.java"
git add "LC0072_EditDistance.java"
git commit -m "feat(leetcode): solve LC0072 Edit Distance in Java"
sleep 2

# [2/6] LC0210_CourseScheduleII.java
echo "[*] Committing [2/6]: LC0210 Course Schedule II..."
cp "staging/day7/LC0210_CourseScheduleII.java" "./LC0210_CourseScheduleII.java"
git add "LC0210_CourseScheduleII.java"
git commit -m "feat(leetcode): solve LC0210 Course Schedule II in Java"
sleep 2

# [3/6] LC0322_CoinChange.java
echo "[*] Committing [3/6]: LC0322 Coin Change..."
cp "staging/day7/LC0322_CoinChange.java" "./LC0322_CoinChange.java"
git add "LC0322_CoinChange.java"
git commit -m "feat(leetcode): solve LC0322 Coin Change in Java"
sleep 2

# [4/6] LC0416_PartitionEqualSubsetSum.java
echo "[*] Committing [4/6]: LC0416 Partition Equal Subset Sum..."
cp "staging/day7/LC0416_PartitionEqualSubsetSum.java" "./LC0416_PartitionEqualSubsetSum.java"
git add "LC0416_PartitionEqualSubsetSum.java"
git commit -m "feat(leetcode): solve LC0416 Partition Equal Subset Sum in Java"
sleep 2

# [5/6] LC0424_LongestRepeatingCharacterReplacement.java
echo "[*] Committing [5/6]: LC0424 Longest Repeating Character Replacement..."
cp "staging/day7/LC0424_LongestRepeatingCharacterReplacement.java" "./LC0424_LongestRepeatingCharacterReplacement.java"
git add "LC0424_LongestRepeatingCharacterReplacement.java"
git commit -m "feat(leetcode): solve LC0424 Longest Repeating Character Replacement in Java"
sleep 2

# [6/6] LC0435_NonOverlappingIntervals.java
echo "[*] Committing [6/6]: LC0435 Non-overlapping Intervals..."
cp "staging/day7/LC0435_NonOverlappingIntervals.java" "./LC0435_NonOverlappingIntervals.java"
git add "LC0435_NonOverlappingIntervals.java"
git commit -m "feat(leetcode): solve LC0435 Non-overlapping Intervals in Java"
sleep 2

echo "[*] Pushing all 6 commits to GitHub..."
git push origin main

echo ""
echo "================================================================"
echo "✅ Day 7 COMPLETE: 6 new Java solutions pushed to GitHub!"
echo "================================================================"
