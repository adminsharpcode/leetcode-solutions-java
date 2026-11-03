# 📱 Termux 7-Day LeetCode Submission Guide

This guide allows you to maintain your GitHub contribution streak and add **6 verified Java LeetCode solutions per day for the next 7 days** using Termux on your Android device while traveling.

---

## 🚀 One-Time Termux Setup (5 Minutes on Android)

1. Open **Termux** on your Android device.
2. Clone this repository (if not already cloned):
   ```bash
   pkg update && pkg install -y git gh
   git clone https://github.com/adminsharpcode/leetcode-solutions-java.git
   cd leetcode-solutions-java
   ```
3. Run the setup script to configure Git and script permissions:
   ```bash
   bash termux_setup.sh
   ```
4. Authenticate GitHub CLI (one-time):
   ```bash
   gh auth login
   ```
   - **What account do you want to log into?** `GitHub.com`
   - **What is your preferred protocol for Git operations?** `HTTPS`
   - **Authenticate Git with your GitHub credentials?** `Yes`
   - **How would you like to authenticate?** `Login with a web browser`
   - Copy the one-time code shown, hit Enter to open browser, and approve.

---

## 📅 Daily Execution Schedule (6 Submissions / Day)

Each day, open Termux, navigate to the repo directory, and run the designated day's script.

```bash
cd ~/leetcode-solutions-java
git pull origin main
```

---

### 🟢 Day 1: Array & Two Pointers
Run command in Termux:
```bash
./run_day.sh 1
# or: bash day1.sh
```
**Submissions (6 commits):**
1. `LC0016_3SumClosest.java` — 3Sum Closest (Medium)
2. `LC0026_RemoveDuplicatesFromSortedArray.java` — Remove Duplicates from Sorted Array (Easy)
3. `LC0075_SortColors.java` — Sort Colors (Medium)
4. `LC0128_LongestConsecutiveSequence.java` — Longest Consecutive Sequence (Medium)
5. `LC0167_TwoSumIIInputArrayIsSorted.java` — Two Sum II - Input Array Is Sorted (Medium)
6. `LC0189_RotateArray.java` — Rotate Array (Medium)

---

### 🟢 Day 2: Linked Lists & Fast/Slow Pointers
Run command in Termux:
```bash
./run_day.sh 2
# or: bash day2.sh
```
**Submissions (6 commits):**
1. `LC0024_SwapNodesInPairs.java` — Swap Nodes in Pairs (Medium)
2. `LC0061_RotateList.java` — Rotate List (Medium)
3. `LC0141_LinkedListCycle.java` — Linked List Cycle (Easy)
4. `LC0142_LinkedListCycleII.java` — Linked List Cycle II (Medium)
5. `LC0143_ReorderList.java` — Reorder List (Medium)
6. `LC0234_PalindromeLinkedList.java` — Palindrome Linked List (Easy)

---

### 🟢 Day 3: Binary Search & 2D Matrices
Run command in Termux:
```bash
./run_day.sh 3
# or: bash day3.sh
```
**Submissions (6 commits):**
1. `LC0034_FindFirstAndLastPositionOfElementInSortedArray.java` — Find First and Last Position in Sorted Array (Medium)
2. `LC0035_SearchInsertPosition.java` — Search Insert Position (Easy)
3. `LC0048_RotateImage.java` — Rotate Image (Medium)
4. `LC0073_SetMatrixZeroes.java` — Set Matrix Zeroes (Medium)
5. `LC0074_SearchA2DMatrix.java` — Search a 2D Matrix (Medium)
6. `LC0240_SearchA2DMatrixII.java` — Search a 2D Matrix II (Medium)

---

### 🟢 Day 4: Stacks, Queues, & PriorityQueue
Run command in Termux:
```bash
./run_day.sh 4
# or: bash day4.sh
```
**Submissions (6 commits):**
1. `LC0150_EvaluateReversePolishNotation.java` — Evaluate Reverse Polish Notation (Medium)
2. `LC0155_MinStack.java` — Min Stack (Medium)
3. `LC0225_ImplementStackUsingQueues.java` — Implement Stack using Queues (Easy)
4. `LC0232_ImplementQueueUsingStacks.java` — Implement Queue using Stacks (Easy)
5. `LC0347_TopKFrequentElements.java` — Top K Frequent Elements (Medium)
6. `LC0373_FindKPairsWithSmallestSums.java` — Find K Pairs with Smallest Sums (Medium)

---

### 🟢 Day 5: Trees & Binary Search Trees
Run command in Termux:
```bash
./run_day.sh 5
# or: bash day5.sh
```
**Submissions (6 commits):**
1. `LC0100_SameTree.java` — Same Tree (Easy)
2. `LC0101_SymmetricTree.java` — Symmetric Tree (Easy)
3. `LC0103_BinaryTreeZigzagLevelOrderTraversal.java` — Zigzag Level Order Traversal (Medium)
4. `LC0110_BalancedBinaryTree.java` — Balanced Binary Tree (Easy)
5. `LC0230_KthSmallestElementInABST.java` — Kth Smallest Element in a BST (Medium)
6. `LC0236_LowestCommonAncestorOfABinaryTree.java` — Lowest Common Ancestor of a Binary Tree (Medium)

---

### 🟢 Day 6: Backtracking & Dynamic Programming
Run command in Termux:
```bash
./run_day.sh 6
# or: bash day6.sh
```
**Submissions (6 commits):**
1. `LC0017_LetterCombinationsOfAPhoneNumber.java` — Letter Combinations of a Phone Number (Medium)
2. `LC0039_CombinationSum.java` — Combination Sum (Medium)
3. `LC0040_CombinationSumII.java` — Combination Sum II (Medium)
4. `LC0064_MinimumPathSum.java` — Minimum Path Sum (Medium)
5. `LC0091_DecodeWays.java` — Decode Ways (Medium)
6. `LC0120_Triangle.java` — Triangle (Medium)

---

### 🟢 Day 7: Advanced DP & Graphs / Intervals
Run command in Termux:
```bash
./run_day.sh 7
# or: bash day7.sh
```
**Submissions (6 commits):**
1. `LC0072_EditDistance.java` — Edit Distance (Medium)
2. `LC0210_CourseScheduleII.java` — Course Schedule II (Medium)
3. `LC0322_CoinChange.java` — Coin Change (Medium)
4. `LC0416_PartitionEqualSubsetSum.java` — Partition Equal Subset Sum (Medium)
5. `LC0424_LongestRepeatingCharacterReplacement.java` — Longest Repeating Character Replacement (Medium)
6. `LC0435_NonOverlappingIntervals.java` — Non-overlapping Intervals (Medium)

---

## ⚡ What Each Script Does Behind the Scenes
- Copies the day's 6 pre-tested, production Java solutions from `staging/dayX/` to the root repository.
- Commits each problem sequentially with standardized conventional commits (`feat(leetcode): solve LCXXXX in Java`).
- Automatically pushes the 6 commits to GitHub (`origin main`), logging real-time progress.
