# 📱 Termux LeetCode Auto-Submissions Guide (Week 3)

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

---

## 📅 Week 3 Catalog Breakdown (42 Brand New Java Solutions)

### 🟢 Day 1: Graphs & BFS / Union Find
- `LC0127_WordLadder.java` (Hard) — Breadth-First Search / Mutating Characters
- `LC0130_SurroundedRegions.java` (Medium) — Boundary DFS In-Place Flood Fill
- `LC0261_GraphValidTree.java` (Medium) — Disjoint Set Union (DSU) Cycle Detection
- `LC0310_MinimumHeightTrees.java` (Medium) — BFS Topological Leaf Trimming
- `LC0399_EvaluateDivision.java` (Medium) — Graph DFS Path Product
- `LC0547_NumberOfProvinces.java` (Medium) — Connected Components DFS / DSU

### 🟢 Day 2: Stack & Monotonic Stack
- `LC0085_MaximalRectangle.java` (Hard) — Monotonic Stack on 2D Histogram Heights
- `LC0316_RemoveDuplicateLetters.java` (Medium) — Greedy Monotonic Stack with Frequency Tracking
- `LC0394_DecodeString.java` (Medium) — Dual Stacks (Multipliers & StringBuffers)
- `LC0496_NextGreaterElementI.java` (Easy) — Monotonic Decreasing Stack + HashMap
- `LC0503_NextGreaterElementII.java` (Medium) — Circular Monotonic Decreasing Index Stack
- `LC0739_DailyTemperatures.java` (Medium) — Monotonic Decreasing Stack Index Spans

### 🟢 Day 3: Sliding Window & Two Pointers
- `LC0030_SubstringConcatenation.java` (Hard) — Fixed-Length Sliding Window with Word Frequency Maps
- `LC0159_LongestSubstringTwoDistinct.java` (Medium) — Dynamic Sliding Window with 2 Distinct Chars
- `LC0239_SlidingWindowMaximum.java` (Hard) — Monotonic Decreasing Deque Window Bounds
- `LC0567_PermutationInString.java` (Medium) — Fixed-Length Frequency Difference Window
- `LC0632_SmallestRange.java` (Hard) — K-Pointer Min-Heap with Maximum Tracker
- `LC0643_MaximumAverageSubarrayI.java` (Easy) — Fixed-Length Sliding Window Running Sum

### 🟢 Day 4: Bit Manipulation & Math
- `LC0190_ReverseBits.java` (Easy) — 32-Bit Shift and Mask
- `LC0191_NumberOf1Bits.java` (Easy) — Brian Kernighan's Bit Manipulation
- `LC0231_PowerOfTwo.java` (Easy) — Single Set Bit Validation
- `LC0260_SingleNumberIII.java` (Medium) — Two-Bucket Bit Partitioning by Lowest Diff Bit
- `LC0268_MissingNumber.java` (Easy) — Gauss Formula / XOR Sum
- `LC0371_SumOfTwoIntegers.java` (Medium) — Bitwise Adder Simulation (XOR & Carry Shift)

### 🟢 Day 5: Dynamic Programming (2D & State Transitions)
- `LC0097_InterleavingString.java` (Medium) — 2D Matrix Interleaving DP
- `LC0115_DistinctSubsequences.java` (Hard) — 2D Subsequence Matching DP
- `LC0132_PalindromePartitioningII.java` (Hard) — Palindrome Table + 1D Min-Cut DP
- `LC0188_BestTimeToBuyAndSellStockIV.java` (Hard) — K-Transaction Buy/Sell DP
- `LC0309_BestTimeCooldown.java` (Medium) — 3-State Finite State Machine DP (Held, Sold, Rest)
- `LC0518_CoinChangeII.java` (Medium) — Unbounded Knapsack / Combinations DP

### 🟢 Day 6: Trie & String Algorithms
- `LC0211_DesignAddSearchWords.java` (Medium) — 26-Way Trie with Recursive DFS Wildcard Matching
- `LC0212_WordSearchII.java` (Hard) — 2D Grid DFS Backtracking over Prefix Trie
- `LC0336_PalindromePairs.java` (Hard) — Reversed Prefix/Suffix Palindrome Matching
- `LC0421_MaximumXOR.java` (Medium) — Bitwise Prefix Trie Greedy Bit Inversion
- `LC0472_ConcatenatedWords.java` (Hard) — Dictionary Set + 1D DP Word Formation
- `LC0648_ReplaceWords.java` (Medium) — Prefix Trie Shortest Root Substitution

### 🟢 Day 7: Advanced Trees & LCA
- `LC0297_SerializeDeserializeBinaryTree.java` (Hard) — Preorder DFS with Null Sentinels
- `LC0450_DeleteNodeInBST.java` (Medium) — BST Key Search + In-Order Successor Deletion
- `LC0538_ConvertBSTToGreaterTree.java` (Medium) — Reverse In-Order DFS Accumulator
- `LC0543_DiameterOfBinaryTree.java` (Easy) — Post-Order DFS Max Depth Span
- `LC0572_SubtreeOfAnotherTree.java` (Easy) — Subtree Equality DFS Traversal
- `LC0652_FindDuplicateSubtrees.java` (Medium) — Post-Order Serialization HashMap Deduplication

---

## 🛠 Manual Override (Optional)

If you ever want to force-run a specific day:
```bash
./run_day.sh 1    # Force Day 1
./run_day.sh 2    # Force Day 2
# ... etc.
```

Happy submitting and enjoy your travels!
