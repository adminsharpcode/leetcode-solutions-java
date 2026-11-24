#!/bin/bash
# =================================================================
# Day 4 LeetCode Submissions (6 Sequential Java Contributions)
# Compatible with Termux (Android) and standard Linux/macOS bash
# =================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================"
echo "🚀 Executing Day 4 Submissions (6 Problems in Java)"
echo "================================================================"

if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0190_ReverseBits.java
echo "[*] Processing [1/6]: LC0190 Reverse Bits..."
if [ -f "./LC0190_ReverseBits.java" ] && git ls-files --error-unmatch "./LC0190_ReverseBits.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0190_ReverseBits.java"; then
    echo "    [✓] LC0190_ReverseBits.java is already committed in git repository."
else
    cp "staging/day4/LC0190_ReverseBits.java" "./LC0190_ReverseBits.java"
    git add "LC0190_ReverseBits.java"
    git commit -m "feat(leetcode): solve LC0190 Reverse Bits in Java"
    echo "    [+] Committed [1/6]: LC0190 Reverse Bits"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [2/6] LC0191_NumberOf1Bits.java
echo "[*] Processing [2/6]: LC0191 Number of 1 Bits..."
if [ -f "./LC0191_NumberOf1Bits.java" ] && git ls-files --error-unmatch "./LC0191_NumberOf1Bits.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0191_NumberOf1Bits.java"; then
    echo "    [✓] LC0191_NumberOf1Bits.java is already committed in git repository."
else
    cp "staging/day4/LC0191_NumberOf1Bits.java" "./LC0191_NumberOf1Bits.java"
    git add "LC0191_NumberOf1Bits.java"
    git commit -m "feat(leetcode): solve LC0191 Number of 1 Bits in Java"
    echo "    [+] Committed [2/6]: LC0191 Number of 1 Bits"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [3/6] LC0231_PowerOfTwo.java
echo "[*] Processing [3/6]: LC0231 Power of Two..."
if [ -f "./LC0231_PowerOfTwo.java" ] && git ls-files --error-unmatch "./LC0231_PowerOfTwo.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0231_PowerOfTwo.java"; then
    echo "    [✓] LC0231_PowerOfTwo.java is already committed in git repository."
else
    cp "staging/day4/LC0231_PowerOfTwo.java" "./LC0231_PowerOfTwo.java"
    git add "LC0231_PowerOfTwo.java"
    git commit -m "feat(leetcode): solve LC0231 Power of Two in Java"
    echo "    [+] Committed [3/6]: LC0231 Power of Two"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [4/6] LC0260_SingleNumberIII.java
echo "[*] Processing [4/6]: LC0260 Single Number III..."
if [ -f "./LC0260_SingleNumberIII.java" ] && git ls-files --error-unmatch "./LC0260_SingleNumberIII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0260_SingleNumberIII.java"; then
    echo "    [✓] LC0260_SingleNumberIII.java is already committed in git repository."
else
    cp "staging/day4/LC0260_SingleNumberIII.java" "./LC0260_SingleNumberIII.java"
    git add "LC0260_SingleNumberIII.java"
    git commit -m "feat(leetcode): solve LC0260 Single Number III in Java"
    echo "    [+] Committed [4/6]: LC0260 Single Number III"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [5/6] LC0268_MissingNumber.java
echo "[*] Processing [5/6]: LC0268 Missing Number..."
if [ -f "./LC0268_MissingNumber.java" ] && git ls-files --error-unmatch "./LC0268_MissingNumber.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0268_MissingNumber.java"; then
    echo "    [✓] LC0268_MissingNumber.java is already committed in git repository."
else
    cp "staging/day4/LC0268_MissingNumber.java" "./LC0268_MissingNumber.java"
    git add "LC0268_MissingNumber.java"
    git commit -m "feat(leetcode): solve LC0268 Missing Number in Java"
    echo "    [+] Committed [5/6]: LC0268 Missing Number"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [6/6] LC0371_SumOfTwoIntegers.java
echo "[*] Processing [6/6]: LC0371 Sum of Two Integers..."
if [ -f "./LC0371_SumOfTwoIntegers.java" ] && git ls-files --error-unmatch "./LC0371_SumOfTwoIntegers.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0371_SumOfTwoIntegers.java"; then
    echo "    [✓] LC0371_SumOfTwoIntegers.java is already committed in git repository."
else
    cp "staging/day4/LC0371_SumOfTwoIntegers.java" "./LC0371_SumOfTwoIntegers.java"
    git add "LC0371_SumOfTwoIntegers.java"
    git commit -m "feat(leetcode): solve LC0371 Sum of Two Integers in Java"
    echo "    [+] Committed [6/6]: LC0371 Sum of Two Integers"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

echo "================================================================"
echo "[*] Day 4 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 4 complete! 6 contributions pushed to GitHub."
echo "================================================================"
