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

# Ensure we have git configured
if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

# Pull latest commits cleanly
echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0100_SameTree.java
echo "[*] Committing [1/6]: LC0100 Same Tree..."
cp "staging/day5/LC0100_SameTree.java" "./LC0100_SameTree.java"
git add "LC0100_SameTree.java"
git commit -m "feat(leetcode): solve LC0100 Same Tree in Java"
sleep 2

# [2/6] LC0101_SymmetricTree.java
echo "[*] Committing [2/6]: LC0101 Symmetric Tree..."
cp "staging/day5/LC0101_SymmetricTree.java" "./LC0101_SymmetricTree.java"
git add "LC0101_SymmetricTree.java"
git commit -m "feat(leetcode): solve LC0101 Symmetric Tree in Java"
sleep 2

# [3/6] LC0103_BinaryTreeZigzagLevelOrderTraversal.java
echo "[*] Committing [3/6]: LC0103 Binary Tree Zigzag Level Order Traversal..."
cp "staging/day5/LC0103_BinaryTreeZigzagLevelOrderTraversal.java" "./LC0103_BinaryTreeZigzagLevelOrderTraversal.java"
git add "LC0103_BinaryTreeZigzagLevelOrderTraversal.java"
git commit -m "feat(leetcode): solve LC0103 Binary Tree Zigzag Level Order Traversal in Java"
sleep 2

# [4/6] LC0110_BalancedBinaryTree.java
echo "[*] Committing [4/6]: LC0110 Balanced Binary Tree..."
cp "staging/day5/LC0110_BalancedBinaryTree.java" "./LC0110_BalancedBinaryTree.java"
git add "LC0110_BalancedBinaryTree.java"
git commit -m "feat(leetcode): solve LC0110 Balanced Binary Tree in Java"
sleep 2

# [5/6] LC0230_KthSmallestElementInABST.java
echo "[*] Committing [5/6]: LC0230 Kth Smallest Element in a BST..."
cp "staging/day5/LC0230_KthSmallestElementInABST.java" "./LC0230_KthSmallestElementInABST.java"
git add "LC0230_KthSmallestElementInABST.java"
git commit -m "feat(leetcode): solve LC0230 Kth Smallest Element in a BST in Java"
sleep 2

# [6/6] LC0236_LowestCommonAncestorOfABinaryTree.java
echo "[*] Committing [6/6]: LC0236 Lowest Common Ancestor of a Binary Tree..."
cp "staging/day5/LC0236_LowestCommonAncestorOfABinaryTree.java" "./LC0236_LowestCommonAncestorOfABinaryTree.java"
git add "LC0236_LowestCommonAncestorOfABinaryTree.java"
git commit -m "feat(leetcode): solve LC0236 Lowest Common Ancestor of a Binary Tree in Java"
sleep 2

echo "[*] Pushing all 6 commits to GitHub..."
git push origin main

echo ""
echo "================================================================"
echo "✅ Day 5 COMPLETE: 6 new Java solutions pushed to GitHub!"
echo "================================================================"
