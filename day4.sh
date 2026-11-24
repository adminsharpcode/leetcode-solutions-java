#!/bin/sh
# day4.sh — Week 3 Day 4 submission runner
set -e
echo "=== Week 3 Day 4 ==="

# --- LC0190 Reverse Bits ---
FILE="staging/day4/LC0190_ReverseBits.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0190 Reverse Bits already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0190 Reverse Bits in Java"
  echo "COMMITTED: LC0190 Reverse Bits"
fi

# --- LC0191 Number of 1 Bits ---
FILE="staging/day4/LC0191_NumberOf1Bits.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0191 Number of 1 Bits already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0191 Number of 1 Bits in Java"
  echo "COMMITTED: LC0191 Number of 1 Bits"
fi

# --- LC0231 Power of Two ---
FILE="staging/day4/LC0231_PowerOfTwo.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0231 Power of Two already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0231 Power of Two in Java"
  echo "COMMITTED: LC0231 Power of Two"
fi

# --- LC0260 Single Number III ---
FILE="staging/day4/LC0260_SingleNumberIII.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0260 Single Number III already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0260 Single Number III in Java"
  echo "COMMITTED: LC0260 Single Number III"
fi

# --- LC0268 Missing Number ---
FILE="staging/day4/LC0268_MissingNumber.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0268 Missing Number already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0268 Missing Number in Java"
  echo "COMMITTED: LC0268 Missing Number"
fi

# --- LC0371 Sum of Two Integers ---
FILE="staging/day4/LC0371_SumOfTwoIntegers.java"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: LC0371 Sum of Two Integers already committed."
else
  git add "$FILE"
  git commit -m "feat(leetcode): solve LC0371 Sum of Two Integers in Java"
  echo "COMMITTED: LC0371 Sum of Two Integers"
fi

git push origin main
echo "=== Day 4 push complete ==="
