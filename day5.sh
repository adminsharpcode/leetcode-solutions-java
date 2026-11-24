#!/bin/sh
# day5.sh — Week 3 Day 5 submission runner
set -e
echo "=== Week 3 Day 5 ==="

# --- LC0097 Interleaving String ---
FILE="staging/day5/LC0097_InterleavingString.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0097 Interleaving String already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0097 Interleaving String in Java"
  echo "COMMITTED: LC0097 Interleaving String"
fi

# --- LC0115 Distinct Subsequences ---
FILE="staging/day5/LC0115_DistinctSubsequences.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0115 Distinct Subsequences already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0115 Distinct Subsequences in Java"
  echo "COMMITTED: LC0115 Distinct Subsequences"
fi

# --- LC0188 Best Time to Buy and Sell Stock IV ---
FILE="staging/day5/LC0188_BestTimeToBuyAndSellStockIV.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0188 Best Time to Buy and Sell Stock IV already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0188 Best Time to Buy and Sell Stock IV in Java"
  echo "COMMITTED: LC0188 Best Time to Buy and Sell Stock IV"
fi

# --- LC0309 Best Time to Buy and Sell Stock with Cooldown ---
FILE="staging/day5/LC0309_BestTimeCooldown.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0309 Best Time to Buy and Sell Stock with Cooldown already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0309 Best Time to Buy and Sell Stock with Cooldown in Java"
  echo "COMMITTED: LC0309 Best Time to Buy and Sell Stock with Cooldown"
fi

# --- LC0518 Coin Change II ---
FILE="staging/day5/LC0518_CoinChangeII.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0518 Coin Change II already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0518 Coin Change II in Java"
  echo "COMMITTED: LC0518 Coin Change II"
fi

# --- LC0132 Palindrome Partitioning II ---
FILE="staging/day5/LC0132_PalindromePartitioningII.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0132 Palindrome Partitioning II already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0132 Palindrome Partitioning II in Java"
  echo "COMMITTED: LC0132 Palindrome Partitioning II"
fi

git push origin main
echo "=== Day 5 push complete ==="
