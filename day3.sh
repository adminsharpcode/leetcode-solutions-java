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

# [1/6] LC0030_SubstringConcatenation.java
echo "[*] Processing [1/6]: LC0030 Substring with Concatenation of All Words..."
if [ -f "./LC0030_SubstringConcatenation.java" ] && git ls-files --error-unmatch "./LC0030_SubstringConcatenation.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0030_SubstringConcatenation.java"; then
    echo "    [✓] LC0030_SubstringConcatenation.java is already committed in git repository."
else
    cp "staging/day3/LC0030_SubstringConcatenation.java" "./LC0030_SubstringConcatenation.java"
    git add "LC0030_SubstringConcatenation.java"
    git commit -m "feat(leetcode): solve LC0030 Substring with Concatenation of All Words in Java"
    echo "    [+] Committed [1/6]: LC0030 Substring with Concatenation of All Words"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [2/6] LC0159_LongestSubstringTwoDistinct.java
echo "[*] Processing [2/6]: LC0159 Longest Substring with At Most Two Distinct Characters..."
if [ -f "./LC0159_LongestSubstringTwoDistinct.java" ] && git ls-files --error-unmatch "./LC0159_LongestSubstringTwoDistinct.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0159_LongestSubstringTwoDistinct.java"; then
    echo "    [✓] LC0159_LongestSubstringTwoDistinct.java is already committed in git repository."
else
    cp "staging/day3/LC0159_LongestSubstringTwoDistinct.java" "./LC0159_LongestSubstringTwoDistinct.java"
    git add "LC0159_LongestSubstringTwoDistinct.java"
    git commit -m "feat(leetcode): solve LC0159 Longest Substring with At Most Two Distinct Characters in Java"
    echo "    [+] Committed [2/6]: LC0159 Longest Substring with At Most Two Distinct Characters"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [3/6] LC0239_SlidingWindowMaximum.java
echo "[*] Processing [3/6]: LC0239 Sliding Window Maximum..."
if [ -f "./LC0239_SlidingWindowMaximum.java" ] && git ls-files --error-unmatch "./LC0239_SlidingWindowMaximum.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0239_SlidingWindowMaximum.java"; then
    echo "    [✓] LC0239_SlidingWindowMaximum.java is already committed in git repository."
else
    cp "staging/day3/LC0239_SlidingWindowMaximum.java" "./LC0239_SlidingWindowMaximum.java"
    git add "LC0239_SlidingWindowMaximum.java"
    git commit -m "feat(leetcode): solve LC0239 Sliding Window Maximum in Java"
    echo "    [+] Committed [3/6]: LC0239 Sliding Window Maximum"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [4/6] LC0567_PermutationInString.java
echo "[*] Processing [4/6]: LC0567 Permutation in String..."
if [ -f "./LC0567_PermutationInString.java" ] && git ls-files --error-unmatch "./LC0567_PermutationInString.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0567_PermutationInString.java"; then
    echo "    [✓] LC0567_PermutationInString.java is already committed in git repository."
else
    cp "staging/day3/LC0567_PermutationInString.java" "./LC0567_PermutationInString.java"
    git add "LC0567_PermutationInString.java"
    git commit -m "feat(leetcode): solve LC0567 Permutation in String in Java"
    echo "    [+] Committed [4/6]: LC0567 Permutation in String"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [5/6] LC0632_SmallestRange.java
echo "[*] Processing [5/6]: LC0632 Smallest Range Covering Elements from K Lists..."
if [ -f "./LC0632_SmallestRange.java" ] && git ls-files --error-unmatch "./LC0632_SmallestRange.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0632_SmallestRange.java"; then
    echo "    [✓] LC0632_SmallestRange.java is already committed in git repository."
else
    cp "staging/day3/LC0632_SmallestRange.java" "./LC0632_SmallestRange.java"
    git add "LC0632_SmallestRange.java"
    git commit -m "feat(leetcode): solve LC0632 Smallest Range Covering Elements from K Lists in Java"
    echo "    [+] Committed [5/6]: LC0632 Smallest Range Covering Elements from K Lists"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [6/6] LC0643_MaximumAverageSubarrayI.java
echo "[*] Processing [6/6]: LC0643 Maximum Average Subarray I..."
if [ -f "./LC0643_MaximumAverageSubarrayI.java" ] && git ls-files --error-unmatch "./LC0643_MaximumAverageSubarrayI.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0643_MaximumAverageSubarrayI.java"; then
    echo "    [✓] LC0643_MaximumAverageSubarrayI.java is already committed in git repository."
else
    cp "staging/day3/LC0643_MaximumAverageSubarrayI.java" "./LC0643_MaximumAverageSubarrayI.java"
    git add "LC0643_MaximumAverageSubarrayI.java"
    git commit -m "feat(leetcode): solve LC0643 Maximum Average Subarray I in Java"
    echo "    [+] Committed [6/6]: LC0643 Maximum Average Subarray I"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

echo "================================================================"
echo "[*] Day 3 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 3 complete! 6 contributions pushed to GitHub."
echo "================================================================"
