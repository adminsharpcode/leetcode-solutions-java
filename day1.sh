#!/bin/sh
# day1.sh — Week 3 Day 1 submission runner
set -e
echo "=== Week 3 Day 1 ==="

# --- LC0127 Word Ladder ---
FILE="staging/day1/LC0127_WordLadder.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0127 Word Ladder already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0127 Word Ladder in Java"
  echo "COMMITTED: LC0127 Word Ladder"
fi

# --- LC0130 Surrounded Regions ---
FILE="staging/day1/LC0130_SurroundedRegions.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0130 Surrounded Regions already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0130 Surrounded Regions in Java"
  echo "COMMITTED: LC0130 Surrounded Regions"
fi

# --- LC0261 Graph Valid Tree ---
FILE="staging/day1/LC0261_GraphValidTree.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0261 Graph Valid Tree already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0261 Graph Valid Tree in Java"
  echo "COMMITTED: LC0261 Graph Valid Tree"
fi

# --- LC0310 Minimum Height Trees ---
FILE="staging/day1/LC0310_MinimumHeightTrees.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0310 Minimum Height Trees already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0310 Minimum Height Trees in Java"
  echo "COMMITTED: LC0310 Minimum Height Trees"
fi

# --- LC0399 Evaluate Division ---
FILE="staging/day1/LC0399_EvaluateDivision.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0399 Evaluate Division already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0399 Evaluate Division in Java"
  echo "COMMITTED: LC0399 Evaluate Division"
fi

# --- LC0547 Number of Provinces ---
FILE="staging/day1/LC0547_NumberOfProvinces.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0547 Number of Provinces already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0547 Number of Provinces in Java"
  echo "COMMITTED: LC0547 Number of Provinces"
fi

git push origin main
echo "=== Day 1 push complete ==="
