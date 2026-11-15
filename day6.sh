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

if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0045_JumpGameII.java
echo "[*] Processing [1/6]: LC0045 Jump Game II..."
if [ -f "./LC0045_JumpGameII.java" ] && git ls-files --error-unmatch "./LC0045_JumpGameII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0045_JumpGameII.java"; then
    echo "    [✓] LC0045_JumpGameII.java is already committed in git repository."
else
    cp "staging/day6/LC0045_JumpGameII.java" "./LC0045_JumpGameII.java"
    git add "LC0045_JumpGameII.java"
    git commit -m "feat(leetcode): solve LC0045 Jump Game II in Java"
    echo "    [+] Committed [1/6]: LC0045 Jump Game II"
    sleep 2
fi

# [2/6] LC0063_UniquePathsII.java
echo "[*] Processing [2/6]: LC0063 Unique Paths II..."
if [ -f "./LC0063_UniquePathsII.java" ] && git ls-files --error-unmatch "./LC0063_UniquePathsII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0063_UniquePathsII.java"; then
    echo "    [✓] LC0063_UniquePathsII.java is already committed in git repository."
else
    cp "staging/day6/LC0063_UniquePathsII.java" "./LC0063_UniquePathsII.java"
    git add "LC0063_UniquePathsII.java"
    git commit -m "feat(leetcode): solve LC0063 Unique Paths II in Java"
    echo "    [+] Committed [2/6]: LC0063 Unique Paths II"
    sleep 2
fi

# [3/6] LC0134_GasStation.java
echo "[*] Processing [3/6]: LC0134 Gas Station..."
if [ -f "./LC0134_GasStation.java" ] && git ls-files --error-unmatch "./LC0134_GasStation.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0134_GasStation.java"; then
    echo "    [✓] LC0134_GasStation.java is already committed in git repository."
else
    cp "staging/day6/LC0134_GasStation.java" "./LC0134_GasStation.java"
    git add "LC0134_GasStation.java"
    git commit -m "feat(leetcode): solve LC0134 Gas Station in Java"
    echo "    [+] Committed [3/6]: LC0134 Gas Station"
    sleep 2
fi

# [4/6] LC0213_HouseRobberII.java
echo "[*] Processing [4/6]: LC0213 House Robber II..."
if [ -f "./LC0213_HouseRobberII.java" ] && git ls-files --error-unmatch "./LC0213_HouseRobberII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0213_HouseRobberII.java"; then
    echo "    [✓] LC0213_HouseRobberII.java is already committed in git repository."
else
    cp "staging/day6/LC0213_HouseRobberII.java" "./LC0213_HouseRobberII.java"
    git add "LC0213_HouseRobberII.java"
    git commit -m "feat(leetcode): solve LC0213 House Robber II in Java"
    echo "    [+] Committed [4/6]: LC0213 House Robber II"
    sleep 2
fi

# [5/6] LC0279_PerfectSquares.java
echo "[*] Processing [5/6]: LC0279 Perfect Squares..."
if [ -f "./LC0279_PerfectSquares.java" ] && git ls-files --error-unmatch "./LC0279_PerfectSquares.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0279_PerfectSquares.java"; then
    echo "    [✓] LC0279_PerfectSquares.java is already committed in git repository."
else
    cp "staging/day6/LC0279_PerfectSquares.java" "./LC0279_PerfectSquares.java"
    git add "LC0279_PerfectSquares.java"
    git commit -m "feat(leetcode): solve LC0279 Perfect Squares in Java"
    echo "    [+] Committed [5/6]: LC0279 Perfect Squares"
    sleep 2
fi

# [6/6] LC0338_CountingBits.java
echo "[*] Processing [6/6]: LC0338 Counting Bits..."
if [ -f "./LC0338_CountingBits.java" ] && git ls-files --error-unmatch "./LC0338_CountingBits.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0338_CountingBits.java"; then
    echo "    [✓] LC0338_CountingBits.java is already committed in git repository."
else
    cp "staging/day6/LC0338_CountingBits.java" "./LC0338_CountingBits.java"
    git add "LC0338_CountingBits.java"
    git commit -m "feat(leetcode): solve LC0338 Counting Bits in Java"
    echo "    [+] Committed [6/6]: LC0338 Counting Bits"
    sleep 2
fi

echo "================================================================"
echo "[*] Day 6 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 6 complete! 6 contributions pushed to GitHub."
echo "================================================================"
