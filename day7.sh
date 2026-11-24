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

if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0297_SerializeDeserializeBinaryTree.java
echo "[*] Processing [1/6]: LC0297 Serialize and Deserialize Binary Tree..."
if [ -f "./LC0297_SerializeDeserializeBinaryTree.java" ] && git ls-files --error-unmatch "./LC0297_SerializeDeserializeBinaryTree.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0297_SerializeDeserializeBinaryTree.java"; then
    echo "    [✓] LC0297_SerializeDeserializeBinaryTree.java is already committed in git repository."
else
    cp "staging/day7/LC0297_SerializeDeserializeBinaryTree.java" "./LC0297_SerializeDeserializeBinaryTree.java"
    git add "LC0297_SerializeDeserializeBinaryTree.java"
    git commit -m "feat(leetcode): solve LC0297 Serialize and Deserialize Binary Tree in Java"
    echo "    [+] Committed [1/6]: LC0297 Serialize and Deserialize Binary Tree"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [2/6] LC0450_DeleteNodeInBST.java
echo "[*] Processing [2/6]: LC0450 Delete Node in a BST..."
if [ -f "./LC0450_DeleteNodeInBST.java" ] && git ls-files --error-unmatch "./LC0450_DeleteNodeInBST.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0450_DeleteNodeInBST.java"; then
    echo "    [✓] LC0450_DeleteNodeInBST.java is already committed in git repository."
else
    cp "staging/day7/LC0450_DeleteNodeInBST.java" "./LC0450_DeleteNodeInBST.java"
    git add "LC0450_DeleteNodeInBST.java"
    git commit -m "feat(leetcode): solve LC0450 Delete Node in a BST in Java"
    echo "    [+] Committed [2/6]: LC0450 Delete Node in a BST"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [3/6] LC0538_ConvertBSTToGreaterTree.java
echo "[*] Processing [3/6]: LC0538 Convert BST to Greater Tree..."
if [ -f "./LC0538_ConvertBSTToGreaterTree.java" ] && git ls-files --error-unmatch "./LC0538_ConvertBSTToGreaterTree.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0538_ConvertBSTToGreaterTree.java"; then
    echo "    [✓] LC0538_ConvertBSTToGreaterTree.java is already committed in git repository."
else
    cp "staging/day7/LC0538_ConvertBSTToGreaterTree.java" "./LC0538_ConvertBSTToGreaterTree.java"
    git add "LC0538_ConvertBSTToGreaterTree.java"
    git commit -m "feat(leetcode): solve LC0538 Convert BST to Greater Tree in Java"
    echo "    [+] Committed [3/6]: LC0538 Convert BST to Greater Tree"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [4/6] LC0543_DiameterOfBinaryTree.java
echo "[*] Processing [4/6]: LC0543 Diameter of Binary Tree..."
if [ -f "./LC0543_DiameterOfBinaryTree.java" ] && git ls-files --error-unmatch "./LC0543_DiameterOfBinaryTree.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0543_DiameterOfBinaryTree.java"; then
    echo "    [✓] LC0543_DiameterOfBinaryTree.java is already committed in git repository."
else
    cp "staging/day7/LC0543_DiameterOfBinaryTree.java" "./LC0543_DiameterOfBinaryTree.java"
    git add "LC0543_DiameterOfBinaryTree.java"
    git commit -m "feat(leetcode): solve LC0543 Diameter of Binary Tree in Java"
    echo "    [+] Committed [4/6]: LC0543 Diameter of Binary Tree"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [5/6] LC0572_SubtreeOfAnotherTree.java
echo "[*] Processing [5/6]: LC0572 Subtree of Another Tree..."
if [ -f "./LC0572_SubtreeOfAnotherTree.java" ] && git ls-files --error-unmatch "./LC0572_SubtreeOfAnotherTree.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0572_SubtreeOfAnotherTree.java"; then
    echo "    [✓] LC0572_SubtreeOfAnotherTree.java is already committed in git repository."
else
    cp "staging/day7/LC0572_SubtreeOfAnotherTree.java" "./LC0572_SubtreeOfAnotherTree.java"
    git add "LC0572_SubtreeOfAnotherTree.java"
    git commit -m "feat(leetcode): solve LC0572 Subtree of Another Tree in Java"
    echo "    [+] Committed [5/6]: LC0572 Subtree of Another Tree"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [6/6] LC0652_FindDuplicateSubtrees.java
echo "[*] Processing [6/6]: LC0652 Find Duplicate Subtrees..."
if [ -f "./LC0652_FindDuplicateSubtrees.java" ] && git ls-files --error-unmatch "./LC0652_FindDuplicateSubtrees.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0652_FindDuplicateSubtrees.java"; then
    echo "    [✓] LC0652_FindDuplicateSubtrees.java is already committed in git repository."
else
    cp "staging/day7/LC0652_FindDuplicateSubtrees.java" "./LC0652_FindDuplicateSubtrees.java"
    git add "LC0652_FindDuplicateSubtrees.java"
    git commit -m "feat(leetcode): solve LC0652 Find Duplicate Subtrees in Java"
    echo "    [+] Committed [6/6]: LC0652 Find Duplicate Subtrees"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

echo "================================================================"
echo "[*] Day 7 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 7 complete! 6 contributions pushed to GitHub."
echo "================================================================"
