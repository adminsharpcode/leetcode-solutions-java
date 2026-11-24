#!/bin/sh
# day2.sh — Week 3 Day 2 submission runner
set -e
echo "=== Week 3 Day 2 ==="

# --- LC0085 Maximal Rectangle ---
FILE="staging/day2/LC0085_MaximalRectangle.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0085 Maximal Rectangle already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0085 Maximal Rectangle in Java"
  echo "COMMITTED: LC0085 Maximal Rectangle"
fi

# --- LC0316 Remove Duplicate Letters ---
FILE="staging/day2/LC0316_RemoveDuplicateLetters.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0316 Remove Duplicate Letters already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0316 Remove Duplicate Letters in Java"
  echo "COMMITTED: LC0316 Remove Duplicate Letters"
fi

# --- LC0394 Decode String ---
FILE="staging/day2/LC0394_DecodeString.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0394 Decode String already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0394 Decode String in Java"
  echo "COMMITTED: LC0394 Decode String"
fi

# --- LC0496 Next Greater Element I ---
FILE="staging/day2/LC0496_NextGreaterElementI.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0496 Next Greater Element I already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0496 Next Greater Element I in Java"
  echo "COMMITTED: LC0496 Next Greater Element I"
fi

# --- LC0503 Next Greater Element II ---
FILE="staging/day2/LC0503_NextGreaterElementII.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0503 Next Greater Element II already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0503 Next Greater Element II in Java"
  echo "COMMITTED: LC0503 Next Greater Element II"
fi

# --- LC0739 Daily Temperatures ---
FILE="staging/day2/LC0739_DailyTemperatures.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0739 Daily Temperatures already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0739 Daily Temperatures in Java"
  echo "COMMITTED: LC0739 Daily Temperatures"
fi

git push origin main
echo "=== Day 2 push complete ==="
