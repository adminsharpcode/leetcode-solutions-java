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

# Ensure we have git configured
if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

# Pull latest commits cleanly
echo "[*] Syncing with remote repository..."
git pull --rebase origin main || true

# [1/6] LC0034_FindFirstAndLastPositionOfElementInSortedArray.java
echo "[*] Committing [1/6]: LC0034 Find First and Last Position of Element in Sorted Array..."
cp "staging/day3/LC0034_FindFirstAndLastPositionOfElementInSortedArray.java" "./LC0034_FindFirstAndLastPositionOfElementInSortedArray.java"
git add "LC0034_FindFirstAndLastPositionOfElementInSortedArray.java"
git commit -m "feat(leetcode): solve LC0034 Find First and Last Position of Element in Sorted Array in Java"
sleep 2

# [2/6] LC0035_SearchInsertPosition.java
echo "[*] Committing [2/6]: LC0035 Search Insert Position..."
cp "staging/day3/LC0035_SearchInsertPosition.java" "./LC0035_SearchInsertPosition.java"
git add "LC0035_SearchInsertPosition.java"
git commit -m "feat(leetcode): solve LC0035 Search Insert Position in Java"
sleep 2

# [3/6] LC0048_RotateImage.java
echo "[*] Committing [3/6]: LC0048 Rotate Image..."
cp "staging/day3/LC0048_RotateImage.java" "./LC0048_RotateImage.java"
git add "LC0048_RotateImage.java"
git commit -m "feat(leetcode): solve LC0048 Rotate Image in Java"
sleep 2

# [4/6] LC0073_SetMatrixZeroes.java
echo "[*] Committing [4/6]: LC0073 Set Matrix Zeroes..."
cp "staging/day3/LC0073_SetMatrixZeroes.java" "./LC0073_SetMatrixZeroes.java"
git add "LC0073_SetMatrixZeroes.java"
git commit -m "feat(leetcode): solve LC0073 Set Matrix Zeroes in Java"
sleep 2

# [5/6] LC0074_SearchA2DMatrix.java
echo "[*] Committing [5/6]: LC0074 Search a 2D Matrix..."
cp "staging/day3/LC0074_SearchA2DMatrix.java" "./LC0074_SearchA2DMatrix.java"
git add "LC0074_SearchA2DMatrix.java"
git commit -m "feat(leetcode): solve LC0074 Search a 2D Matrix in Java"
sleep 2

# [6/6] LC0240_SearchA2DMatrixII.java
echo "[*] Committing [6/6]: LC0240 Search a 2D Matrix II..."
cp "staging/day3/LC0240_SearchA2DMatrixII.java" "./LC0240_SearchA2DMatrixII.java"
git add "LC0240_SearchA2DMatrixII.java"
git commit -m "feat(leetcode): solve LC0240 Search a 2D Matrix II in Java"
sleep 2

echo "[*] Pushing all 6 commits to GitHub..."
git push origin main

echo ""
echo "================================================================"
echo "✅ Day 3 COMPLETE: 6 new Java solutions pushed to GitHub!"
echo "================================================================"
