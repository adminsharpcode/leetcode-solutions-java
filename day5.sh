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

# [1/6] LC0108_ConvertSortedArrayToBST.java
echo "[*] Processing [1/6]: LC0108 Convert Sorted Array to Binary Search Tree..."
if [ -f "./LC0108_ConvertSortedArrayToBST.java" ] && git ls-files --error-unmatch "./LC0108_ConvertSortedArrayToBST.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0108_ConvertSortedArrayToBST.java"; then
    echo "    [✓] LC0108_ConvertSortedArrayToBST.java is already committed in git repository."
else
    cp "staging/day5/LC0108_ConvertSortedArrayToBST.java" "./LC0108_ConvertSortedArrayToBST.java"
    git add "LC0108_ConvertSortedArrayToBST.java"
    git commit -m "feat(leetcode): solve LC0108 Convert Sorted Array to Binary Search Tree in Java"
    echo "    [+] Committed [1/6]: LC0108 Convert Sorted Array to Binary Search Tree"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [2/6] LC0111_MinimumDepthOfBinaryTree.java
echo "[*] Processing [2/6]: LC0111 Minimum Depth of Binary Tree..."
if [ -f "./LC0111_MinimumDepthOfBinaryTree.java" ] && git ls-files --error-unmatch "./LC0111_MinimumDepthOfBinaryTree.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0111_MinimumDepthOfBinaryTree.java"; then
    echo "    [✓] LC0111_MinimumDepthOfBinaryTree.java is already committed in git repository."
else
    cp "staging/day5/LC0111_MinimumDepthOfBinaryTree.java" "./LC0111_MinimumDepthOfBinaryTree.java"
    git add "LC0111_MinimumDepthOfBinaryTree.java"
    git commit -m "feat(leetcode): solve LC0111 Minimum Depth of Binary Tree in Java"
    echo "    [+] Committed [2/6]: LC0111 Minimum Depth of Binary Tree"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [3/6] LC0112_PathSum.java
echo "[*] Processing [3/6]: LC0112 Path Sum..."
if [ -f "./LC0112_PathSum.java" ] && git ls-files --error-unmatch "./LC0112_PathSum.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0112_PathSum.java"; then
    echo "    [✓] LC0112_PathSum.java is already committed in git repository."
else
    cp "staging/day5/LC0112_PathSum.java" "./LC0112_PathSum.java"
    git add "LC0112_PathSum.java"
    git commit -m "feat(leetcode): solve LC0112 Path Sum in Java"
    echo "    [+] Committed [3/6]: LC0112 Path Sum"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [4/6] LC0113_PathSumII.java
echo "[*] Processing [4/6]: LC0113 Path Sum II..."
if [ -f "./LC0113_PathSumII.java" ] && git ls-files --error-unmatch "./LC0113_PathSumII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0113_PathSumII.java"; then
    echo "    [✓] LC0113_PathSumII.java is already committed in git repository."
else
    cp "staging/day5/LC0113_PathSumII.java" "./LC0113_PathSumII.java"
    git add "LC0113_PathSumII.java"
    git commit -m "feat(leetcode): solve LC0113 Path Sum II in Java"
    echo "    [+] Committed [4/6]: LC0113 Path Sum II"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [5/6] LC0129_SumRootToLeafNumbers.java
echo "[*] Processing [5/6]: LC0129 Sum Root to Leaf Numbers..."
if [ -f "./LC0129_SumRootToLeafNumbers.java" ] && git ls-files --error-unmatch "./LC0129_SumRootToLeafNumbers.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0129_SumRootToLeafNumbers.java"; then
    echo "    [✓] LC0129_SumRootToLeafNumbers.java is already committed in git repository."
else
    cp "staging/day5/LC0129_SumRootToLeafNumbers.java" "./LC0129_SumRootToLeafNumbers.java"
    git add "LC0129_SumRootToLeafNumbers.java"
    git commit -m "feat(leetcode): solve LC0129 Sum Root to Leaf Numbers in Java"
    echo "    [+] Committed [5/6]: LC0129 Sum Root to Leaf Numbers"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [6/6] LC0199_BinaryTreeRightSideView.java
echo "[*] Processing [6/6]: LC0199 Binary Tree Right Side View..."
if [ -f "./LC0199_BinaryTreeRightSideView.java" ] && git ls-files --error-unmatch "./LC0199_BinaryTreeRightSideView.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0199_BinaryTreeRightSideView.java"; then
    echo "    [✓] LC0199_BinaryTreeRightSideView.java is already committed in git repository."
else
    cp "staging/day5/LC0199_BinaryTreeRightSideView.java" "./LC0199_BinaryTreeRightSideView.java"
    git add "LC0199_BinaryTreeRightSideView.java"
    git commit -m "feat(leetcode): solve LC0199 Binary Tree Right Side View in Java"
    echo "    [+] Committed [6/6]: LC0199 Binary Tree Right Side View"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

echo "================================================================"
echo "[*] Day 5 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 5 complete! 6 contributions pushed to GitHub."
echo "================================================================"
