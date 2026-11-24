#!/bin/bash
# =================================================================
# Day 1 LeetCode Submissions (6 Sequential Java Contributions)
# Compatible with Termux (Android) and standard Linux/macOS bash
# =================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================"
echo "🚀 Executing Day 1 Submissions (6 Problems in Java)"
echo "================================================================"

if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0127_WordLadder.java
echo "[*] Processing [1/6]: LC0127 Word Ladder..."
if [ -f "./LC0127_WordLadder.java" ] && git ls-files --error-unmatch "./LC0127_WordLadder.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0127_WordLadder.java"; then
    echo "    [✓] LC0127_WordLadder.java is already committed in git repository."
else
    cp "staging/day1/LC0127_WordLadder.java" "./LC0127_WordLadder.java"
    git add "LC0127_WordLadder.java"
    git commit -m "feat(leetcode): solve LC0127 Word Ladder in Java"
    echo "    [+] Committed [1/6]: LC0127 Word Ladder"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [2/6] LC0130_SurroundedRegions.java
echo "[*] Processing [2/6]: LC0130 Surrounded Regions..."
if [ -f "./LC0130_SurroundedRegions.java" ] && git ls-files --error-unmatch "./LC0130_SurroundedRegions.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0130_SurroundedRegions.java"; then
    echo "    [✓] LC0130_SurroundedRegions.java is already committed in git repository."
else
    cp "staging/day1/LC0130_SurroundedRegions.java" "./LC0130_SurroundedRegions.java"
    git add "LC0130_SurroundedRegions.java"
    git commit -m "feat(leetcode): solve LC0130 Surrounded Regions in Java"
    echo "    [+] Committed [2/6]: LC0130 Surrounded Regions"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [3/6] LC0261_GraphValidTree.java
echo "[*] Processing [3/6]: LC0261 Graph Valid Tree..."
if [ -f "./LC0261_GraphValidTree.java" ] && git ls-files --error-unmatch "./LC0261_GraphValidTree.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0261_GraphValidTree.java"; then
    echo "    [✓] LC0261_GraphValidTree.java is already committed in git repository."
else
    cp "staging/day1/LC0261_GraphValidTree.java" "./LC0261_GraphValidTree.java"
    git add "LC0261_GraphValidTree.java"
    git commit -m "feat(leetcode): solve LC0261 Graph Valid Tree in Java"
    echo "    [+] Committed [3/6]: LC0261 Graph Valid Tree"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [4/6] LC0310_MinimumHeightTrees.java
echo "[*] Processing [4/6]: LC0310 Minimum Height Trees..."
if [ -f "./LC0310_MinimumHeightTrees.java" ] && git ls-files --error-unmatch "./LC0310_MinimumHeightTrees.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0310_MinimumHeightTrees.java"; then
    echo "    [✓] LC0310_MinimumHeightTrees.java is already committed in git repository."
else
    cp "staging/day1/LC0310_MinimumHeightTrees.java" "./LC0310_MinimumHeightTrees.java"
    git add "LC0310_MinimumHeightTrees.java"
    git commit -m "feat(leetcode): solve LC0310 Minimum Height Trees in Java"
    echo "    [+] Committed [4/6]: LC0310 Minimum Height Trees"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [5/6] LC0399_EvaluateDivision.java
echo "[*] Processing [5/6]: LC0399 Evaluate Division..."
if [ -f "./LC0399_EvaluateDivision.java" ] && git ls-files --error-unmatch "./LC0399_EvaluateDivision.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0399_EvaluateDivision.java"; then
    echo "    [✓] LC0399_EvaluateDivision.java is already committed in git repository."
else
    cp "staging/day1/LC0399_EvaluateDivision.java" "./LC0399_EvaluateDivision.java"
    git add "LC0399_EvaluateDivision.java"
    git commit -m "feat(leetcode): solve LC0399 Evaluate Division in Java"
    echo "    [+] Committed [5/6]: LC0399 Evaluate Division"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

# [6/6] LC0547_NumberOfProvinces.java
echo "[*] Processing [6/6]: LC0547 Number of Provinces..."
if [ -f "./LC0547_NumberOfProvinces.java" ] && git ls-files --error-unmatch "./LC0547_NumberOfProvinces.java" >/dev/null 2>&1 && git diff --quiet HEAD -- "./LC0547_NumberOfProvinces.java"; then
    echo "    [✓] LC0547_NumberOfProvinces.java is already committed in git repository."
else
    cp "staging/day1/LC0547_NumberOfProvinces.java" "./LC0547_NumberOfProvinces.java"
    git add "LC0547_NumberOfProvinces.java"
    git commit -m "feat(leetcode): solve LC0547 Number of Provinces in Java"
    echo "    [+] Committed [6/6]: LC0547 Number of Provinces"
    command -v sleep >/dev/null 2>&1 && sleep 2 || true
fi

echo "================================================================"
echo "[*] Day 1 commits recorded! Pushing to GitHub..."
echo "================================================================"
git push origin main || git push

echo ""
echo "🎉 [SUCCESS] Day 1 complete! 6 contributions pushed to GitHub."
echo "================================================================"
