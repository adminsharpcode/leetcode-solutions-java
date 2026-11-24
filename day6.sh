#!/bin/bash
# =================================================================
# Day 6 LeetCode Submissions (6 Sequential Java Contributions)
# Compatible with Termux (Android) and standard Linux/macOS bash
# =================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================"
echo "🚀 Executing Day 6 Submissions (6 Problems in Java)"
echo "================================================================"

if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0211_DesignAddSearchWords.java
echo "[*] Processing [1/6]: LC0211 Design Add and Search Words Data Structure..."
if [ -f "./LC0211_DesignAddSearchWords.java" ] && git ls-files --error-unmatch "./LC0211_DesignAddSearchWords.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0211_DesignAddSearchWords.java"; then
    echo "    [✓] LC0211_DesignAddSearchWords.java is already committed in git repository."
else
    cp "staging/day6/LC0211_DesignAddSearchWords.java" "./LC0211_DesignAddSearchWords.java"
    git add "LC0211_DesignAddSearchWords.java"
    git commit -m "feat(leetcode): solve LC0211 Design Add and Search Words Data Structure in Java"
    echo "    [+] Committed [1/6]: LC0211 Design Add and Search Words Data Structure"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [2/6] LC0212_WordSearchII.java
echo "[*] Processing [2/6]: LC0212 Word Search II..."
if [ -f "./LC0212_WordSearchII.java" ] && git ls-files --error-unmatch "./LC0212_WordSearchII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0212_WordSearchII.java"; then
    echo "    [✓] LC0212_WordSearchII.java is already committed in git repository."
else
    cp "staging/day6/LC0212_WordSearchII.java" "./LC0212_WordSearchII.java"
    git add "LC0212_WordSearchII.java"
    git commit -m "feat(leetcode): solve LC0212 Word Search II in Java"
    echo "    [+] Committed [2/6]: LC0212 Word Search II"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [3/6] LC0336_PalindromePairs.java
echo "[*] Processing [3/6]: LC0336 Palindrome Pairs..."
if [ -f "./LC0336_PalindromePairs.java" ] && git ls-files --error-unmatch "./LC0336_PalindromePairs.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0336_PalindromePairs.java"; then
    echo "    [✓] LC0336_PalindromePairs.java is already committed in git repository."
else
    cp "staging/day6/LC0336_PalindromePairs.java" "./LC0336_PalindromePairs.java"
    git add "LC0336_PalindromePairs.java"
    git commit -m "feat(leetcode): solve LC0336 Palindrome Pairs in Java"
    echo "    [+] Committed [3/6]: LC0336 Palindrome Pairs"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [4/6] LC0421_MaximumXOR.java
echo "[*] Processing [4/6]: LC0421 Maximum XOR of Two Numbers in an Array..."
if [ -f "./LC0421_MaximumXOR.java" ] && git ls-files --error-unmatch "./LC0421_MaximumXOR.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0421_MaximumXOR.java"; then
    echo "    [✓] LC0421_MaximumXOR.java is already committed in git repository."
else
    cp "staging/day6/LC0421_MaximumXOR.java" "./LC0421_MaximumXOR.java"
    git add "LC0421_MaximumXOR.java"
    git commit -m "feat(leetcode): solve LC0421 Maximum XOR of Two Numbers in an Array in Java"
    echo "    [+] Committed [4/6]: LC0421 Maximum XOR of Two Numbers in an Array"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [5/6] LC0472_ConcatenatedWords.java
echo "[*] Processing [5/6]: LC0472 Concatenated Words..."
if [ -f "./LC0472_ConcatenatedWords.java" ] && git ls-files --error-unmatch "./LC0472_ConcatenatedWords.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0472_ConcatenatedWords.java"; then
    echo "    [✓] LC0472_ConcatenatedWords.java is already committed in git repository."
else
    cp "staging/day6/LC0472_ConcatenatedWords.java" "./LC0472_ConcatenatedWords.java"
    git add "LC0472_ConcatenatedWords.java"
    git commit -m "feat(leetcode): solve LC0472 Concatenated Words in Java"
    echo "    [+] Committed [5/6]: LC0472 Concatenated Words"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [6/6] LC0648_ReplaceWords.java
echo "[*] Processing [6/6]: LC0648 Replace Words..."
if [ -f "./LC0648_ReplaceWords.java" ] && git ls-files --error-unmatch "./LC0648_ReplaceWords.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0648_ReplaceWords.java"; then
    echo "    [✓] LC0648_ReplaceWords.java is already committed in git repository."
else
    cp "staging/day6/LC0648_ReplaceWords.java" "./LC0648_ReplaceWords.java"
    git add "LC0648_ReplaceWords.java"
    git commit -m "feat(leetcode): solve LC0648 Replace Words in Java"
    echo "    [+] Committed [6/6]: LC0648 Replace Words"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

echo "================================================================"
echo "[*] Day 6 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 6 complete! 6 contributions pushed to GitHub."
echo "================================================================"
