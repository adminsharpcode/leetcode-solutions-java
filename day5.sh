#!/bin/bash
# =================================================================
# Day 5 LeetCode Submissions (6 Sequential Java Contributions)
# Compatible with Termux (Android) and standard Linux/macOS bash
# =================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================"
echo "🚀 Executing Day 5 Submissions (6 Problems in Java)"
echo "================================================================"

if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0097_InterleavingString.java
echo "[*] Processing [1/6]: LC0097 Interleaving String..."
if [ -f "./LC0097_InterleavingString.java" ] && git ls-files --error-unmatch "./LC0097_InterleavingString.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0097_InterleavingString.java"; then
    echo "    [✓] LC0097_InterleavingString.java is already committed in git repository."
else
    cp "staging/day5/LC0097_InterleavingString.java" "./LC0097_InterleavingString.java"
    git add "LC0097_InterleavingString.java"
    git commit -m "feat(leetcode): solve LC0097 Interleaving String in Java"
    echo "    [+] Committed [1/6]: LC0097 Interleaving String"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [2/6] LC0115_DistinctSubsequences.java
echo "[*] Processing [2/6]: LC0115 Distinct Subsequences..."
if [ -f "./LC0115_DistinctSubsequences.java" ] && git ls-files --error-unmatch "./LC0115_DistinctSubsequences.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0115_DistinctSubsequences.java"; then
    echo "    [✓] LC0115_DistinctSubsequences.java is already committed in git repository."
else
    cp "staging/day5/LC0115_DistinctSubsequences.java" "./LC0115_DistinctSubsequences.java"
    git add "LC0115_DistinctSubsequences.java"
    git commit -m "feat(leetcode): solve LC0115 Distinct Subsequences in Java"
    echo "    [+] Committed [2/6]: LC0115 Distinct Subsequences"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [3/6] LC0132_PalindromePartitioningII.java
echo "[*] Processing [3/6]: LC0132 Palindrome Partitioning II..."
if [ -f "./LC0132_PalindromePartitioningII.java" ] && git ls-files --error-unmatch "./LC0132_PalindromePartitioningII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0132_PalindromePartitioningII.java"; then
    echo "    [✓] LC0132_PalindromePartitioningII.java is already committed in git repository."
else
    cp "staging/day5/LC0132_PalindromePartitioningII.java" "./LC0132_PalindromePartitioningII.java"
    git add "LC0132_PalindromePartitioningII.java"
    git commit -m "feat(leetcode): solve LC0132 Palindrome Partitioning II in Java"
    echo "    [+] Committed [3/6]: LC0132 Palindrome Partitioning II"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [4/6] LC0188_BestTimeToBuyAndSellStockIV.java
echo "[*] Processing [4/6]: LC0188 Best Time to Buy and Sell Stock IV..."
if [ -f "./LC0188_BestTimeToBuyAndSellStockIV.java" ] && git ls-files --error-unmatch "./LC0188_BestTimeToBuyAndSellStockIV.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0188_BestTimeToBuyAndSellStockIV.java"; then
    echo "    [✓] LC0188_BestTimeToBuyAndSellStockIV.java is already committed in git repository."
else
    cp "staging/day5/LC0188_BestTimeToBuyAndSellStockIV.java" "./LC0188_BestTimeToBuyAndSellStockIV.java"
    git add "LC0188_BestTimeToBuyAndSellStockIV.java"
    git commit -m "feat(leetcode): solve LC0188 Best Time to Buy and Sell Stock IV in Java"
    echo "    [+] Committed [4/6]: LC0188 Best Time to Buy and Sell Stock IV"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [5/6] LC0309_BestTimeCooldown.java
echo "[*] Processing [5/6]: LC0309 Best Time to Buy and Sell Stock with Cooldown..."
if [ -f "./LC0309_BestTimeCooldown.java" ] && git ls-files --error-unmatch "./LC0309_BestTimeCooldown.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0309_BestTimeCooldown.java"; then
    echo "    [✓] LC0309_BestTimeCooldown.java is already committed in git repository."
else
    cp "staging/day5/LC0309_BestTimeCooldown.java" "./LC0309_BestTimeCooldown.java"
    git add "LC0309_BestTimeCooldown.java"
    git commit -m "feat(leetcode): solve LC0309 Best Time to Buy and Sell Stock with Cooldown in Java"
    echo "    [+] Committed [5/6]: LC0309 Best Time to Buy and Sell Stock with Cooldown"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [6/6] LC0518_CoinChangeII.java
echo "[*] Processing [6/6]: LC0518 Coin Change II..."
if [ -f "./LC0518_CoinChangeII.java" ] && git ls-files --error-unmatch "./LC0518_CoinChangeII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0518_CoinChangeII.java"; then
    echo "    [✓] LC0518_CoinChangeII.java is already committed in git repository."
else
    cp "staging/day5/LC0518_CoinChangeII.java" "./LC0518_CoinChangeII.java"
    git add "LC0518_CoinChangeII.java"
    git commit -m "feat(leetcode): solve LC0518 Coin Change II in Java"
    echo "    [+] Committed [6/6]: LC0518 Coin Change II"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

echo "================================================================"
echo "[*] Day 5 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 5 complete! 6 contributions pushed to GitHub."
echo "================================================================"
