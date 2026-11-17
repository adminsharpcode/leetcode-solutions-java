#!/bin/bash
# =================================================================
# Day 3 LeetCode Submissions (6 Sequential Java Contributions)
# Compatible with Termux (Android) and standard Linux/macOS bash
# =================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================"
echo "🚀 Executing Day 3 Submissions (6 Problems in Java)"
echo "================================================================"

if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0006_ZigzagConversion.java
echo "[*] Processing [1/6]: LC0006 Zigzag Conversion..."
if [ -f "./LC0006_ZigzagConversion.java" ] && git ls-files --error-unmatch "./LC0006_ZigzagConversion.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0006_ZigzagConversion.java"; then
    echo "    [✓] LC0006_ZigzagConversion.java is already committed in git repository."
else
    cp "staging/day3/LC0006_ZigzagConversion.java" "./LC0006_ZigzagConversion.java"
    git add "LC0006_ZigzagConversion.java"
    git commit -m "feat(leetcode): solve LC0006 Zigzag Conversion in Java"
    echo "    [+] Committed [1/6]: LC0006 Zigzag Conversion"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [2/6] LC0012_IntegerToRoman.java
echo "[*] Processing [2/6]: LC0012 Integer to Roman..."
if [ -f "./LC0012_IntegerToRoman.java" ] && git ls-files --error-unmatch "./LC0012_IntegerToRoman.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0012_IntegerToRoman.java"; then
    echo "    [✓] LC0012_IntegerToRoman.java is already committed in git repository."
else
    cp "staging/day3/LC0012_IntegerToRoman.java" "./LC0012_IntegerToRoman.java"
    git add "LC0012_IntegerToRoman.java"
    git commit -m "feat(leetcode): solve LC0012 Integer to Roman in Java"
    echo "    [+] Committed [2/6]: LC0012 Integer to Roman"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [3/6] LC0013_RomanToInteger.java
echo "[*] Processing [3/6]: LC0013 Roman to Integer..."
if [ -f "./LC0013_RomanToInteger.java" ] && git ls-files --error-unmatch "./LC0013_RomanToInteger.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0013_RomanToInteger.java"; then
    echo "    [✓] LC0013_RomanToInteger.java is already committed in git repository."
else
    cp "staging/day3/LC0013_RomanToInteger.java" "./LC0013_RomanToInteger.java"
    git add "LC0013_RomanToInteger.java"
    git commit -m "feat(leetcode): solve LC0013 Roman to Integer in Java"
    echo "    [+] Committed [3/6]: LC0013 Roman to Integer"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [4/6] LC0043_MultiplyStrings.java
echo "[*] Processing [4/6]: LC0043 Multiply Strings..."
if [ -f "./LC0043_MultiplyStrings.java" ] && git ls-files --error-unmatch "./LC0043_MultiplyStrings.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0043_MultiplyStrings.java"; then
    echo "    [✓] LC0043_MultiplyStrings.java is already committed in git repository."
else
    cp "staging/day3/LC0043_MultiplyStrings.java" "./LC0043_MultiplyStrings.java"
    git add "LC0043_MultiplyStrings.java"
    git commit -m "feat(leetcode): solve LC0043 Multiply Strings in Java"
    echo "    [+] Committed [4/6]: LC0043 Multiply Strings"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [5/6] LC0058_LengthOfLastWord.java
echo "[*] Processing [5/6]: LC0058 Length of Last Word..."
if [ -f "./LC0058_LengthOfLastWord.java" ] && git ls-files --error-unmatch "./LC0058_LengthOfLastWord.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0058_LengthOfLastWord.java"; then
    echo "    [✓] LC0058_LengthOfLastWord.java is already committed in git repository."
else
    cp "staging/day3/LC0058_LengthOfLastWord.java" "./LC0058_LengthOfLastWord.java"
    git add "LC0058_LengthOfLastWord.java"
    git commit -m "feat(leetcode): solve LC0058 Length of Last Word in Java"
    echo "    [+] Committed [5/6]: LC0058 Length of Last Word"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [6/6] LC0125_ValidPalindrome.java
echo "[*] Processing [6/6]: LC0125 Valid Palindrome..."
if [ -f "./LC0125_ValidPalindrome.java" ] && git ls-files --error-unmatch "./LC0125_ValidPalindrome.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0125_ValidPalindrome.java"; then
    echo "    [✓] LC0125_ValidPalindrome.java is already committed in git repository."
else
    cp "staging/day3/LC0125_ValidPalindrome.java" "./LC0125_ValidPalindrome.java"
    git add "LC0125_ValidPalindrome.java"
    git commit -m "feat(leetcode): solve LC0125 Valid Palindrome in Java"
    echo "    [+] Committed [6/6]: LC0125 Valid Palindrome"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

echo "================================================================"
echo "[*] Day 3 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 3 complete! 6 contributions pushed to GitHub."
echo "================================================================"
