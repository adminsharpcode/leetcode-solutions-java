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

# [1/6] LC0029_DivideTwoIntegers.java
echo "[*] Processing [1/6]: LC0029 Divide Two Integers..."
if [ -f "./LC0029_DivideTwoIntegers.java" ] && git ls-files --error-unmatch "./LC0029_DivideTwoIntegers.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0029_DivideTwoIntegers.java"; then
    echo "    [✓] LC0029_DivideTwoIntegers.java is already committed in git repository."
else
    cp "staging/day7/LC0029_DivideTwoIntegers.java" "./LC0029_DivideTwoIntegers.java"
    git add "LC0029_DivideTwoIntegers.java"
    git commit -m "feat(leetcode): solve LC0029 Divide Two Integers in Java"
    echo "    [+] Committed [1/6]: LC0029 Divide Two Integers"
    sleep 2
fi

# [2/6] LC0077_Combinations.java
echo "[*] Processing [2/6]: LC0077 Combinations..."
if [ -f "./LC0077_Combinations.java" ] && git ls-files --error-unmatch "./LC0077_Combinations.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0077_Combinations.java"; then
    echo "    [✓] LC0077_Combinations.java is already committed in git repository."
else
    cp "staging/day7/LC0077_Combinations.java" "./LC0077_Combinations.java"
    git add "LC0077_Combinations.java"
    git commit -m "feat(leetcode): solve LC0077 Combinations in Java"
    echo "    [+] Committed [2/6]: LC0077 Combinations"
    sleep 2
fi

# [3/6] LC0090_SubsetsII.java
echo "[*] Processing [3/6]: LC0090 Subsets II..."
if [ -f "./LC0090_SubsetsII.java" ] && git ls-files --error-unmatch "./LC0090_SubsetsII.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0090_SubsetsII.java"; then
    echo "    [✓] LC0090_SubsetsII.java is already committed in git repository."
else
    cp "staging/day7/LC0090_SubsetsII.java" "./LC0090_SubsetsII.java"
    git add "LC0090_SubsetsII.java"
    git commit -m "feat(leetcode): solve LC0090 Subsets II in Java"
    echo "    [+] Committed [3/6]: LC0090 Subsets II"
    sleep 2
fi

# [4/6] LC0202_HappyNumber.java
echo "[*] Processing [4/6]: LC0202 Happy Number..."
if [ -f "./LC0202_HappyNumber.java" ] && git ls-files --error-unmatch "./LC0202_HappyNumber.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0202_HappyNumber.java"; then
    echo "    [✓] LC0202_HappyNumber.java is already committed in git repository."
else
    cp "staging/day7/LC0202_HappyNumber.java" "./LC0202_HappyNumber.java"
    git add "LC0202_HappyNumber.java"
    git commit -m "feat(leetcode): solve LC0202 Happy Number in Java"
    echo "    [+] Committed [4/6]: LC0202 Happy Number"
    sleep 2
fi

# [5/6] LC0242_ValidAnagram.java
echo "[*] Processing [5/6]: LC0242 Valid Anagram..."
if [ -f "./LC0242_ValidAnagram.java" ] && git ls-files --error-unmatch "./LC0242_ValidAnagram.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0242_ValidAnagram.java"; then
    echo "    [✓] LC0242_ValidAnagram.java is already committed in git repository."
else
    cp "staging/day7/LC0242_ValidAnagram.java" "./LC0242_ValidAnagram.java"
    git add "LC0242_ValidAnagram.java"
    git commit -m "feat(leetcode): solve LC0242 Valid Anagram in Java"
    echo "    [+] Committed [5/6]: LC0242 Valid Anagram"
    sleep 2
fi

# [6/6] LC0295_FindMedianFromDataStream.java
echo "[*] Processing [6/6]: LC0295 Find Median from Data Stream..."
if [ -f "./LC0295_FindMedianFromDataStream.java" ] && git ls-files --error-unmatch "./LC0295_FindMedianFromDataStream.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0295_FindMedianFromDataStream.java"; then
    echo "    [✓] LC0295_FindMedianFromDataStream.java is already committed in git repository."
else
    cp "staging/day7/LC0295_FindMedianFromDataStream.java" "./LC0295_FindMedianFromDataStream.java"
    git add "LC0295_FindMedianFromDataStream.java"
    git commit -m "feat(leetcode): solve LC0295 Find Median from Data Stream in Java"
    echo "    [+] Committed [6/6]: LC0295 Find Median from Data Stream"
    sleep 2
fi

echo "================================================================"
echo "[*] Day 7 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 7 complete! 6 contributions pushed to GitHub."
echo "================================================================"
