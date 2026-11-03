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

# Ensure we have git configured
if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

# Pull latest commits cleanly
echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0150_EvaluateReversePolishNotation.java
echo "[*] Committing [1/6]: LC0150 Evaluate Reverse Polish Notation..."
cp "staging/day4/LC0150_EvaluateReversePolishNotation.java" "./LC0150_EvaluateReversePolishNotation.java"
git add "LC0150_EvaluateReversePolishNotation.java"
git commit -m "feat(leetcode): solve LC0150 Evaluate Reverse Polish Notation in Java"
sleep 2

# [2/6] LC0155_MinStack.java
echo "[*] Committing [2/6]: LC0155 Min Stack..."
cp "staging/day4/LC0155_MinStack.java" "./LC0155_MinStack.java"
git add "LC0155_MinStack.java"
git commit -m "feat(leetcode): solve LC0155 Min Stack in Java"
sleep 2

# [3/6] LC0225_ImplementStackUsingQueues.java
echo "[*] Committing [3/6]: LC0225 Implement Stack using Queues..."
cp "staging/day4/LC0225_ImplementStackUsingQueues.java" "./LC0225_ImplementStackUsingQueues.java"
git add "LC0225_ImplementStackUsingQueues.java"
git commit -m "feat(leetcode): solve LC0225 Implement Stack using Queues in Java"
sleep 2

# [4/6] LC0232_ImplementQueueUsingStacks.java
echo "[*] Committing [4/6]: LC0232 Implement Queue using Stacks..."
cp "staging/day4/LC0232_ImplementQueueUsingStacks.java" "./LC0232_ImplementQueueUsingStacks.java"
git add "LC0232_ImplementQueueUsingStacks.java"
git commit -m "feat(leetcode): solve LC0232 Implement Queue using Stacks in Java"
sleep 2

# [5/6] LC0347_TopKFrequentElements.java
echo "[*] Committing [5/6]: LC0347 Top K Frequent Elements..."
cp "staging/day4/LC0347_TopKFrequentElements.java" "./LC0347_TopKFrequentElements.java"
git add "LC0347_TopKFrequentElements.java"
git commit -m "feat(leetcode): solve LC0347 Top K Frequent Elements in Java"
sleep 2

# [6/6] LC0373_FindKPairsWithSmallestSums.java
echo "[*] Committing [6/6]: LC0373 Find K Pairs with Smallest Sums..."
cp "staging/day4/LC0373_FindKPairsWithSmallestSums.java" "./LC0373_FindKPairsWithSmallestSums.java"
git add "LC0373_FindKPairsWithSmallestSums.java"
git commit -m "feat(leetcode): solve LC0373 Find K Pairs with Smallest Sums in Java"
sleep 2

echo "[*] Pushing all 6 commits to GitHub..."
git push origin main

echo ""
echo "================================================================"
echo "✅ Day 4 COMPLETE: 6 new Java solutions pushed to GitHub!"
echo "================================================================"
