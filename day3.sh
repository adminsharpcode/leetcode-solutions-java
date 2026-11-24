#!/bin/sh
# day3.sh — Week 3 Day 3 submission runner
set -e
echo "=== Week 3 Day 3 ==="

# --- LC0030 Substring with Concatenation of All Words ---
FILE="staging/day3/LC0030_SubstringConcatenation.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0030 Substring with Concatenation of All Words already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0030 Substring with Concatenation of All Words in Java"
  echo "COMMITTED: LC0030 Substring with Concatenation of All Words"
fi

# --- LC0239 Sliding Window Maximum ---
FILE="staging/day3/LC0239_SlidingWindowMaximum.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0239 Sliding Window Maximum already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0239 Sliding Window Maximum in Java"
  echo "COMMITTED: LC0239 Sliding Window Maximum"
fi

# --- LC0567 Permutation in String ---
FILE="staging/day3/LC0567_PermutationInString.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0567 Permutation in String already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0567 Permutation in String in Java"
  echo "COMMITTED: LC0567 Permutation in String"
fi

# --- LC0632 Smallest Range Covering Elements from K Lists ---
FILE="staging/day3/LC0632_SmallestRange.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0632 Smallest Range Covering Elements from K Lists already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0632 Smallest Range Covering Elements from K Lists in Java"
  echo "COMMITTED: LC0632 Smallest Range Covering Elements from K Lists"
fi

# --- LC0643 Maximum Average Subarray I ---
FILE="staging/day3/LC0643_MaximumAverageSubarrayI.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0643 Maximum Average Subarray I already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0643 Maximum Average Subarray I in Java"
  echo "COMMITTED: LC0643 Maximum Average Subarray I"
fi

# --- LC0159 Longest Substring with At Most Two Distinct Characters ---
FILE="staging/day3/LC0159_LongestSubstringTwoDistinct.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0159 Longest Substring with At Most Two Distinct Characters already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0159 Longest Substring with At Most Two Distinct Characters in Java"
  echo "COMMITTED: LC0159 Longest Substring with At Most Two Distinct Characters"
fi

git push origin main
echo "=== Day 3 push complete ==="
