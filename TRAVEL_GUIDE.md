# 📱 Termux LeetCode Auto-Submissions Guide (Week 2)

This guide allows you to maintain your GitHub contribution streak effortlessly using Termux on your Android device while traveling.

With the new **Auto-Detector Engine**, you do **not** need to manually check what is uploaded or keep track of which day you are on. Just run one single command each day!

---

## ⚡ Quick Daily Routine (Zero Friction)

Every day, simply open Termux and run:

```bash
cd ~/leetcode-solutions-java
./auto_submit.sh
```

*(Alternatively: `./run_day.sh`)*

### What the Auto-Detector Does:
1. **Scans Repository**: Detects all problems currently merged and pushed to GitHub.
2. **Finds Next Batch**: Analyzes `staging/day1` through `staging/day7` and finds the next pending day.
3. **Sequential Commits**: Copies each problem into the root directory and creates individual Git commits with clean commit messages.
4. **Pushes to GitHub**: Automatically pushes your 6 contributions for the day.
5. **Prints Summary**: Displays your active streak and remaining queued problems.

---

## 🔍 Checking Status

If you ever want to see what has been submitted vs what is pending without running commits:

```bash
./run_day.sh status
```

Example Output:
```
================================================================
⚡ LeetCode Auto-Detector & Submission Engine
================================================================
[*] Total Java solutions currently active in root: 95
----------------------------------------------------------------
  [✓] Day 1: Completed (6/6 uploaded)
  [ ] Day 2: Queued (0/6 uploaded)
  [ ] Day 3: Queued (0/6 uploaded)
  [ ] Day 4: Queued (0/6 uploaded)
  [ ] Day 5: Queued (0/6 uploaded)
  [ ] Day 6: Queued (0/6 uploaded)
  [ ] Day 7: Queued (0/6 uploaded)
----------------------------------------------------------------
⚡ Next batch queued: DAY 2. Run './auto_submit.sh' to execute.
```

---

## 📅 Week 2 Catalog Breakdown (42 Brand New Java Solutions)

### 🟢 Day 1: Arrays, Two Pointers & In-Place Manipulations
- `LC0018_4Sum.java` (Medium) — Two Pointers / 4-Sum
- `LC0027_RemoveElement.java` (Easy) — Two Pointers Fast/Slow
- `LC0080_RemoveDuplicatesFromSortedArrayII.java` (Medium) — In-Place Array Filter
- `LC0088_MergeSortedArray.java` (Easy) — 3-Pointer Reverse Fill
- `LC0209_MinimumSizeSubarraySum.java` (Medium) — Sliding Window
- `LC0283_MoveZeroes.java` (Easy) — Two Pointers In-Place Swap

### 🟢 Day 2: Linked Lists & Two-Pointer Traversals
- `LC0082_RemoveDuplicatesFromSortedListII.java` (Medium) — Sentinel Dummy Head
- `LC0083_RemoveDuplicatesFromSortedList.java` (Easy) — Linked List Deduplication
- `LC0086_PartitionList.java` (Medium) — Two Sublists Partitioning
- `LC0092_ReverseLinkedListII.java` (Medium) — Subsegment Pointer Inversion
- `LC0160_IntersectionOfTwoLinkedLists.java` (Easy) — Two Pointers Cycle/Intersection
- `LC0203_RemoveLinkedListElements.java` (Easy) — Sentinel Node Deletion

### 🟢 Day 3: Strings & Parsing / Math
- `LC0006_ZigzagConversion.java` (Medium) — Directional Simulation
- `LC0012_IntegerToRoman.java` (Medium) — Greedy Value Extraction
- `LC0013_RomanToInteger.java` (Easy) — Lookahead Subtraction
- `LC0043_MultiplyStrings.java` (Medium) — Grade-School Multiplication
- `LC0058_LengthOfLastWord.java` (Easy) — Backward Traversal
- `LC0125_ValidPalindrome.java` (Easy) — Two Pointers Alpha-Numeric

### 🟢 Day 4: Binary Search & Intervals
- `LC0057_InsertInterval.java` (Medium) — 3-Stage Interval Merge
- `LC0081_SearchInRotatedSortedArrayII.java` (Medium) — Rotated Search with Duplicates
- `LC0162_FindPeakElement.java` (Medium) — Binary Search Slope Analysis
- `LC0278_FirstBadVersion.java` (Easy) — Binary Search Boundary Condition
- `LC0704_BinarySearch.java` (Easy) — Standard Closed-Range Binary Search
- `LC0875_KokoEatingBananas.java` (Medium) — Binary Search on Answer

### 🟢 Day 5: Trees & DFS/BFS
- `LC0108_ConvertSortedArrayToBST.java` (Easy) — Divide and Conquer Height-Balanced BST
- `LC0111_MinimumDepthOfBinaryTree.java` (Easy) — BFS Level-Order Shortest Path
- `LC0112_PathSum.java` (Easy) — DFS Leaf Target Path
- `LC0113_PathSumII.java` (Medium) — DFS Path Backtracking
- `LC0129_SumRootToLeafNumbers.java` (Medium) — DFS Running Radix-10 Sum
- `LC0199_BinaryTreeRightSideView.java` (Medium) — BFS Level-Order Rightmost Node

### 🟢 Day 6: Dynamic Programming & Greedy
- `LC0045_JumpGameII.java` (Medium) — Greedy BFS Boundary Intervals
- `LC0063_UniquePathsII.java` (Medium) — 1D DP with Obstacles
- `LC0134_GasStation.java` (Medium) — Greedy Circuit Deficit Tracking
- `LC0213_HouseRobberII.java` (Medium) — Circular House Robber DP
- `LC0279_PerfectSquares.java` (Medium) — Coin-Change Style DP
- `LC0338_CountingBits.java` (Easy) — Bitwise DP Transition

### 🟢 Day 7: Bit Manipulation, Backtracking & Heaps
- `LC0029_DivideTwoIntegers.java` (Medium) — Exponential Bitwise Shifts
- `LC0077_Combinations.java` (Medium) — Pruned Backtracking
- `LC0090_SubsetsII.java` (Medium) — Backtracking with Duplicate Pruning
- `LC0202_HappyNumber.java` (Easy) — Floyd's Cycle-Finding Algorithm
- `LC0242_ValidAnagram.java` (Easy) — 26-Bucket Frequency Array
- `LC0295_FindMedianFromDataStream.java` (Hard) — Balanced Dual-Heap (Min/Max Heap)

---

## 🛠 Manual Override (Optional)

If you ever want to force-run a specific day:
```bash
./run_day.sh 1    # Force Day 1
./run_day.sh 2    # Force Day 2
# ... etc.
```

Happy submitting and enjoy your travels!
