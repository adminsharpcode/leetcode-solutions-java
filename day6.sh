#!/bin/sh
# day6.sh — Week 3 Day 6 submission runner
set -e
echo "=== Week 3 Day 6 ==="

# --- LC0211 Design Add and Search Words Data Structure ---
FILE="staging/day6/LC0211_DesignAddSearchWords.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0211 Design Add and Search Words Data Structure already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0211 Design Add and Search Words Data Structure in Java"
  echo "COMMITTED: LC0211 Design Add and Search Words Data Structure"
fi

# --- LC0212 Word Search II ---
FILE="staging/day6/LC0212_WordSearchII.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0212 Word Search II already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0212 Word Search II in Java"
  echo "COMMITTED: LC0212 Word Search II"
fi

# --- LC0421 Maximum XOR of Two Numbers in an Array ---
FILE="staging/day6/LC0421_MaximumXOR.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0421 Maximum XOR of Two Numbers in an Array already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0421 Maximum XOR of Two Numbers in an Array in Java"
  echo "COMMITTED: LC0421 Maximum XOR of Two Numbers in an Array"
fi

# --- LC0472 Concatenated Words ---
FILE="staging/day6/LC0472_ConcatenatedWords.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0472 Concatenated Words already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0472 Concatenated Words in Java"
  echo "COMMITTED: LC0472 Concatenated Words"
fi

# --- LC0648 Replace Words ---
FILE="staging/day6/LC0648_ReplaceWords.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0648 Replace Words already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0648 Replace Words in Java"
  echo "COMMITTED: LC0648 Replace Words"
fi

# --- LC0336 Palindrome Pairs ---
FILE="staging/day6/LC0336_PalindromePairs.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0336 Palindrome Pairs already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0336 Palindrome Pairs in Java"
  echo "COMMITTED: LC0336 Palindrome Pairs"
fi

git push origin main
echo "=== Day 6 push complete ==="
