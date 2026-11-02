# LeetCode Solutions in Java 🚀

A curated collection of **30 comprehensive, production-grade Java solutions** to top LeetCode algorithm and data structure problems. Each solution includes problem statement links, approach breakdowns, Big-O time and space complexity analyses, and self-contained executable `main()` test cases.

---

## 📋 Problem Catalog

| # | Problem ID | Title | Difficulty | Category / Pattern | Time Complexity | Space Complexity | Solution File |
|---|---|---|---|---|---|---|---|
| 01 | 1 | Two Sum | 🟢 Easy | Hash Map | $O(N)$ | $O(N)$ | [`LC0001_TwoSum.java`](./LC0001_TwoSum.java) |
| 02 | 2 | Add Two Numbers | 🟡 Medium | Linked List / Math | $O(\max(N,M))$ | $O(\max(N,M))$ | [`LC0002_AddTwoNumbers.java`](./LC0002_AddTwoNumbers.java) |
| 03 | 3 | Longest Substring Without Repeating Characters | 🟡 Medium | Sliding Window | $O(N)$ | $O(\min(N,M))$ | [`LC0003_LongestSubstringWithoutRepeatingCharacters.java`](./LC0003_LongestSubstringWithoutRepeatingCharacters.java) |
| 04 | 4 | Median of Two Sorted Arrays | 🔴 Hard | Binary Search Partition | $O(\log(\min(M,N)))$ | $O(1)$ | [`LC0004_MedianOfTwoSortedArrays.java`](./LC0004_MedianOfTwoSortedArrays.java) |
| 05 | 5 | Longest Palindromic Substring | 🟡 Medium | Expand Around Center | $O(N^2)$ | $O(1)$ | [`LC0005_LongestPalindromicSubstring.java`](./LC0005_LongestPalindromicSubstring.java) |
| 06 | 11 | Container With Most Water | 🟡 Medium | Two Pointers | $O(N)$ | $O(1)$ | [`LC0011_ContainerWithMostWater.java`](./LC0011_ContainerWithMostWater.java) |
| 07 | 15 | 3Sum | 🟡 Medium | Two Pointers / Sorting | $O(N^2)$ | $O(1)$ | [`LC0015_ThreeSum.java`](./LC0015_ThreeSum.java) |
| 08 | 20 | Valid Parentheses | 🟢 Easy | Stack | $O(N)$ | $O(N)$ | [`LC0020_ValidParentheses.java`](./LC0020_ValidParentheses.java) |
| 09 | 21 | Merge Two Sorted Lists | 🟢 Easy | Linked List | $O(N+M)$ | $O(1)$ | [`LC0021_MergeTwoSortedLists.java`](./LC0021_MergeTwoSortedLists.java) |
| 10 | 23 | Merge k Sorted Lists | 🔴 Hard | Min-Heap PriorityQueue | $O(N \log k)$ | $O(k)$ | [`LC0023_MergeKSortedLists.java`](./LC0023_MergeKSortedLists.java) |
| 11 | 33 | Search in Rotated Sorted Array | 🟡 Medium | Binary Search | $O(\log N)$ | $O(1)$ | [`LC0033_SearchInRotatedSortedArray.java`](./LC0033_SearchInRotatedSortedArray.java) |
| 12 | 42 | Trapping Rain Water | 🔴 Hard | Two Pointers / Extremes | $O(N)$ | $O(1)$ | [`LC0042_TrappingRainWater.java`](./LC0042_TrappingRainWater.java) |
| 13 | 46 | Permutations | 🟡 Medium | Backtracking | $O(N \cdot N!)$ | $O(N)$ | [`LC0046_Permutations.java`](./LC0046_Permutations.java) |
| 14 | 49 | Group Anagrams | 🟡 Medium | Hash Map / Counting | $O(N \cdot K)$ | $O(N \cdot K)$ | [`LC0049_GroupAnagrams.java`](./LC0049_GroupAnagrams.java) |
| 15 | 53 | Maximum Subarray | 🟡 Medium | Kadane's Algorithm | $O(N)$ | $O(1)$ | [`LC0053_MaximumSubarray.java`](./LC0053_MaximumSubarray.java) |
| 16 | 56 | Merge Intervals | 🟡 Medium | Sorting & Intervals | $O(N \log N)$ | $O(N)$ | [`LC0056_MergeIntervals.java`](./LC0056_MergeIntervals.java) |
| 17 | 70 | Climbing Stairs | 🟢 Easy | Dynamic Programming | $O(N)$ | $O(1)$ | [`LC0070_ClimbingStairs.java`](./LC0070_ClimbingStairs.java) |
| 18 | 76 | Minimum Window Substring | 🔴 Hard | Sliding Window | $O(S + T)$ | $O(S + T)$ | [`LC0076_MinimumWindowSubstring.java`](./LC0076_MinimumWindowSubstring.java) |
| 19 | 98 | Validate Binary Search Tree | 🟡 Medium | DFS / Boundary Checks | $O(N)$ | $O(H)$ | [`LC0098_ValidateBinarySearchTree.java`](./LC0098_ValidateBinarySearchTree.java) |
| 20 | 102 | Binary Tree Level Order Traversal | 🟡 Medium | BFS Queue | $O(N)$ | $O(N)$ | [`LC0102_BinaryTreeLevelOrderTraversal.java`](./LC0102_BinaryTreeLevelOrderTraversal.java) |
| 21 | 121 | Best Time to Buy and Sell Stock | 🟢 Easy | One-Pass Greedy | $O(N)$ | $O(1)$ | [`LC0121_BestTimeToBuyAndSellStock.java`](./LC0121_BestTimeToBuyAndSellStock.java) |
| 22 | 124 | Binary Tree Maximum Path Sum | 🔴 Hard | Tree Post-Order DFS | $O(N)$ | $O(H)$ | [`LC0124_BinaryTreeMaximumPathSum.java`](./LC0124_BinaryTreeMaximumPathSum.java) |
| 23 | 133 | Clone Graph | 🟡 Medium | Graph DFS + Map | $O(V + E)$ | $O(V)$ | [`LC0133_CloneGraph.java`](./LC0133_CloneGraph.java) |
| 24 | 139 | Word Break | 🟡 Medium | 1D Dynamic Programming | $O(N^3)$ | $O(N + M)$ | [`LC0139_WordBreak.java`](./LC0139_WordBreak.java) |
| 25 | 146 | LRU Cache | 🟡 Medium | Doubly Linked List + Map | $O(1)$ | $O(C)$ | [`LC0146_LRUCache.java`](./LC0146_LRUCache.java) |
| 26 | 198 | House Robber | 🟡 Medium | 1D Dynamic Programming | $O(N)$ | $O(1)$ | [`LC0198_HouseRobber.java`](./LC0198_HouseRobber.java) |
| 27 | 200 | Number of Islands | 🟡 Medium | Grid DFS / Flood Fill | $O(M \cdot N)$ | $O(M \cdot N)$ | [`LC0200_NumberOfIslands.java`](./LC0200_NumberOfIslands.java) |
| 28 | 206 | Reverse Linked List | 🟢 Easy | Iterative 3-Pointer | $O(N)$ | $O(1)$ | [`LC0206_ReverseLinkedList.java`](./LC0206_ReverseLinkedList.java) |
| 29 | 215 | Kth Largest Element in an Array | 🟡 Medium | Min-Heap PriorityQueue | $O(N \log K)$ | $O(K)$ | [`LC0215_KthLargestElementInAnArray.java`](./LC0215_KthLargestElementInAnArray.java) |
| 30 | 300 | Longest Increasing Subsequence | 🟡 Medium | Patience Sorting + Binary Search | $O(N \log N)$ | $O(N)$ | [`LC0300_LongestIncreasingSubsequence.java`](./LC0300_LongestIncreasingSubsequence.java) |

---

## 🛠 Compilation & Execution

Each Java file is completely standalone and includes its own `main` test runner.

To compile and run any solution:

```bash
# Compile from root workspace
javac LC0001_TwoSum.java

# Run test cases
java LC0001_TwoSum
```

To compile all files at once:

```bash
javac *.java
```
