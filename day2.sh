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

# Ensure we have git configured
if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

# Pull latest commits cleanly
echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0024_SwapNodesInPairs.java
echo "[*] Committing [1/6]: LC0024 Swap Nodes in Pairs..."
cp "staging/day2/LC0024_SwapNodesInPairs.java" "./LC0024_SwapNodesInPairs.java"
git add "LC0024_SwapNodesInPairs.java"
git commit -m "feat(leetcode): solve LC0024 Swap Nodes in Pairs in Java"
sleep 2

# [2/6] LC0061_RotateList.java
echo "[*] Committing [2/6]: LC0061 Rotate List..."
cp "staging/day2/LC0061_RotateList.java" "./LC0061_RotateList.java"
git add "LC0061_RotateList.java"
git commit -m "feat(leetcode): solve LC0061 Rotate List in Java"
sleep 2

# [3/6] LC0141_LinkedListCycle.java
echo "[*] Committing [3/6]: LC0141 Linked List Cycle..."
cp "staging/day2/LC0141_LinkedListCycle.java" "./LC0141_LinkedListCycle.java"
git add "LC0141_LinkedListCycle.java"
git commit -m "feat(leetcode): solve LC0141 Linked List Cycle in Java"
sleep 2

# [4/6] LC0142_LinkedListCycleII.java
echo "[*] Committing [4/6]: LC0142 Linked List Cycle II..."
cp "staging/day2/LC0142_LinkedListCycleII.java" "./LC0142_LinkedListCycleII.java"
git add "LC0142_LinkedListCycleII.java"
git commit -m "feat(leetcode): solve LC0142 Linked List Cycle II in Java"
sleep 2

# [5/6] LC0143_ReorderList.java
echo "[*] Committing [5/6]: LC0143 Reorder List..."
cp "staging/day2/LC0143_ReorderList.java" "./LC0143_ReorderList.java"
git add "LC0143_ReorderList.java"
git commit -m "feat(leetcode): solve LC0143 Reorder List in Java"
sleep 2

# [6/6] LC0234_PalindromeLinkedList.java
echo "[*] Committing [6/6]: LC0234 Palindrome Linked List..."
cp "staging/day2/LC0234_PalindromeLinkedList.java" "./LC0234_PalindromeLinkedList.java"
git add "LC0234_PalindromeLinkedList.java"
git commit -m "feat(leetcode): solve LC0234 Palindrome Linked List in Java"
sleep 2

echo "[*] Pushing all 6 commits to GitHub..."
git push origin main

echo ""
echo "================================================================"
echo "✅ Day 2 COMPLETE: 6 new Java solutions pushed to GitHub!"
echo "================================================================"
