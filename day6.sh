#!/bin/bash
# =================================================================
# Day 6 LeetCode Submissions (6 Sequential Java Contributions)
# Compatible with Termux (Android) and standard Linux/macOS bash
# =================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================"
echo "🚀 Executing Day 6 Submissions (6 Problems in Java)"
echo "================================================================"

# Ensure we have git configured
if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

# Pull latest commits cleanly
echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0017_LetterCombinationsOfAPhoneNumber.java
echo "[*] Committing [1/6]: LC0017 Letter Combinations of a Phone Number..."
cp "staging/day6/LC0017_LetterCombinationsOfAPhoneNumber.java" "./LC0017_LetterCombinationsOfAPhoneNumber.java"
git add "LC0017_LetterCombinationsOfAPhoneNumber.java"
git commit -m "feat(leetcode): solve LC0017 Letter Combinations of a Phone Number in Java"
sleep 2

# [2/6] LC0039_CombinationSum.java
echo "[*] Committing [2/6]: LC0039 Combination Sum..."
cp "staging/day6/LC0039_CombinationSum.java" "./LC0039_CombinationSum.java"
git add "LC0039_CombinationSum.java"
git commit -m "feat(leetcode): solve LC0039 Combination Sum in Java"
sleep 2

# [3/6] LC0040_CombinationSumII.java
echo "[*] Committing [3/6]: LC0040 Combination Sum II..."
cp "staging/day6/LC0040_CombinationSumII.java" "./LC0040_CombinationSumII.java"
git add "LC0040_CombinationSumII.java"
git commit -m "feat(leetcode): solve LC0040 Combination Sum II in Java"
sleep 2

# [4/6] LC0064_MinimumPathSum.java
echo "[*] Committing [4/6]: LC0064 Minimum Path Sum..."
cp "staging/day6/LC0064_MinimumPathSum.java" "./LC0064_MinimumPathSum.java"
git add "LC0064_MinimumPathSum.java"
git commit -m "feat(leetcode): solve LC0064 Minimum Path Sum in Java"
sleep 2

# [5/6] LC0091_DecodeWays.java
echo "[*] Committing [5/6]: LC0091 Decode Ways..."
cp "staging/day6/LC0091_DecodeWays.java" "./LC0091_DecodeWays.java"
git add "LC0091_DecodeWays.java"
git commit -m "feat(leetcode): solve LC0091 Decode Ways in Java"
sleep 2

# [6/6] LC0120_Triangle.java
echo "[*] Committing [6/6]: LC0120 Triangle..."
cp "staging/day6/LC0120_Triangle.java" "./LC0120_Triangle.java"
git add "LC0120_Triangle.java"
git commit -m "feat(leetcode): solve LC0120 Triangle in Java"
sleep 2

echo "[*] Pushing all 6 commits to GitHub..."
git push origin main

echo ""
echo "================================================================"
echo "✅ Day 6 COMPLETE: 6 new Java solutions pushed to GitHub!"
echo "================================================================"
