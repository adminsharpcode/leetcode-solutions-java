#!/bin/sh
# day7.sh — Week 3 Day 7 submission runner
set -e
echo "=== Week 3 Day 7 ==="

# --- LC0297 Serialize and Deserialize Binary Tree ---
FILE="staging/day7/LC0297_SerializeDeserializeBinaryTree.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0297 Serialize and Deserialize Binary Tree already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0297 Serialize and Deserialize Binary Tree in Java"
  echo "COMMITTED: LC0297 Serialize and Deserialize Binary Tree"
fi

# --- LC0450 Delete Node in a BST ---
FILE="staging/day7/LC0450_DeleteNodeInBST.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0450 Delete Node in a BST already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0450 Delete Node in a BST in Java"
  echo "COMMITTED: LC0450 Delete Node in a BST"
fi

# --- LC0538 Convert BST to Greater Tree ---
FILE="staging/day7/LC0538_ConvertBSTToGreaterTree.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0538 Convert BST to Greater Tree already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0538 Convert BST to Greater Tree in Java"
  echo "COMMITTED: LC0538 Convert BST to Greater Tree"
fi

# --- LC0543 Diameter of Binary Tree ---
FILE="staging/day7/LC0543_DiameterOfBinaryTree.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0543 Diameter of Binary Tree already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0543 Diameter of Binary Tree in Java"
  echo "COMMITTED: LC0543 Diameter of Binary Tree"
fi

# --- LC0572 Subtree of Another Tree ---
FILE="staging/day7/LC0572_SubtreeOfAnotherTree.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0572 Subtree of Another Tree already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0572 Subtree of Another Tree in Java"
  echo "COMMITTED: LC0572 Subtree of Another Tree"
fi

# --- LC0652 Find Duplicate Subtrees ---
FILE="staging/day7/LC0652_FindDuplicateSubtrees.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0652 Find Duplicate Subtrees already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0652 Find Duplicate Subtrees in Java"
  echo "COMMITTED: LC0652 Find Duplicate Subtrees"
fi

git push origin main
echo "=== Day 7 push complete ==="
