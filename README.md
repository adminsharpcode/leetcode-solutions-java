# LeetCode Solutions in Java 🚀

A curated collection of **47 comprehensive, production-grade Java solutions** to top LeetCode algorithm and data structure problems. Each solution includes problem statement links, approach breakdowns, Big-O time and space complexity analyses, and self-contained executable `main()` test cases.

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
| 08 | 19 | Remove Nth Node From End of List | 🟡 Medium | Two Pointers (Fast & Slow) | $O(N)$ | $O(1)$ | [`LC0019_RemoveNthNodeFromEndOfList.java`](./LC0019_RemoveNthNodeFromEndOfList.java) |
| 09 | 20 | Valid Parentheses | 🟢 Easy | Stack | $O(N)$ | $O(N)$ | [`LC0020_ValidParentheses.java`](./LC0020_ValidParentheses.java) |
| 10 | 21 | Merge Two Sorted Lists | 🟢 Easy | Linked List | $O(N+M)$ | $O(1)$ | [`LC0021_MergeTwoSortedLists.java`](./LC0021_MergeTwoSortedLists.java) |
| 11 | 22 | Generate Parentheses | 🟡 Medium | Backtracking | $O(4^N / \sqrt{N})$ | $O(N)$ | [`LC0022_GenerateParentheses.java`](./LC0022_GenerateParentheses.java) |
| 12 | 23 | Merge k Sorted Lists | 🔴 Hard | Min-Heap PriorityQueue | $O(N \log k)$ | $O(k)$ | [`LC0023_MergeKSortedLists.java`](./LC0023_MergeKSortedLists.java) |
| 13 | 33 | Search in Rotated Sorted Array | 🟡 Medium | Binary Search | $O(\log N)$ | $O(1)$ | [`LC0033_SearchInRotatedSortedArray.java`](./LC0033_SearchInRotatedSortedArray.java) |
| 14 | 42 | Trapping Rain Water | 🔴 Hard | Two Pointers / Extremes | $O(N)$ | $O(1)$ | [`LC0042_TrappingRainWater.java`](./LC0042_TrappingRainWater.java) |
| 15 | 46 | Permutations | 🟡 Medium | Backtracking | $O(N \cdot N!)$ | $O(N)$ | [`LC0046_Permutations.java`](./LC0046_Permutations.java) |
| 16 | 49 | Group Anagrams | 🟡 Medium | Hash Map / Counting | $O(N \cdot K)$ | $O(N \cdot K)$ | [`LC0049_GroupAnagrams.java`](./LC0049_GroupAnagrams.java) |
| 17 | 53 | Maximum Subarray | 🟡 Medium | Kadane's Algorithm | $O(N)$ | $O(1)$ | [`LC0053_MaximumSubarray.java`](./LC0053_MaximumSubarray.java) |
| 18 | 54 | Spiral Matrix | 🟡 Medium | Boundary Simulation | $O(M \cdot N)$ | $O(1)$ | [`LC0054_SpiralMatrix.java`](./LC0054_SpiralMatrix.java) |
| 19 | 55 | Jump Game | 🟡 Medium | Greedy Reachability | $O(N)$ | $O(1)$ | [`LC0055_JumpGame.java`](./LC0055_JumpGame.java) |
| 20 | 56 | Merge Intervals | 🟡 Medium | Sorting & Intervals | $O(N \log N)$ | $O(N)$ | [`LC0056_MergeIntervals.java`](./LC0056_MergeIntervals.java) |
| 21 | 62 | Unique Paths | 🟡 Medium | 1D Dynamic Programming | $O(M \cdot N)$ | $O(N)$ | [`LC0062_UniquePaths.java`](./LC0062_UniquePaths.java) |
| 22 | 70 | Climbing Stairs | 🟢 Easy | Dynamic Programming | $O(N)$ | $O(1)$ | [`LC0070_ClimbingStairs.java`](./LC0070_ClimbingStairs.java) |
| 23 | 76 | Minimum Window Substring | 🔴 Hard | Sliding Window | $O(S + T)$ | $O(S + T)$ | [`LC0076_MinimumWindowSubstring.java`](./LC0076_MinimumWindowSubstring.java) |
| 24 | 78 | Subsets | 🟡 Medium | Backtracking Power Set | $O(N \cdot 2^N)$ | $O(N)$ | [`LC0078_Subsets.java`](./LC0078_Subsets.java) |
| 25 | 79 | Word Search | 🟡 Medium | Grid DFS Backtracking | $O(M \cdot N \cdot 3^L)$ | $O(L)$ | [`LC0079_WordSearch.java`](./LC0079_WordSearch.java) |
| 26 | 84 | Largest Rectangle in Histogram | 🔴 Hard | Monotonic Stack | $O(N)$ | $O(N)$ | [`LC0084_LargestRectangleInHistogram.java`](./LC0084_LargestRectangleInHistogram.java) |
| 27 | 98 | Validate Binary Search Tree | 🟡 Medium | DFS / Boundary Checks | $O(N)$ | $O(H)$ | [`LC0098_ValidateBinarySearchTree.java`](./LC0098_ValidateBinarySearchTree.java) |
| 28 | 102 | Binary Tree Level Order Traversal | 🟡 Medium | BFS Queue | $O(N)$ | $O(N)$ | [`LC0102_BinaryTreeLevelOrderTraversal.java`](./LC0102_BinaryTreeLevelOrderTraversal.java) |
| 29 | 104 | Maximum Depth of Binary Tree | 🟢 Easy | Post-Order DFS | $O(N)$ | $O(H)$ | [`LC0104_MaximumDepthOfBinaryTree.java`](./LC0104_MaximumDepthOfBinaryTree.java) |
| 30 | 105 | Construct Binary Tree from Preorder & Inorder | 🟡 Medium | Divide & Conquer + Map | $O(N)$ | $O(N)$ | [`LC0105_ConstructBinaryTreeFromPreorderAndInorderTraversal.java`](./LC0105_ConstructBinaryTreeFromPreorderAndInorderTraversal.java) |
| 31 | 121 | Best Time to Buy and Sell Stock | 🟢 Easy | One-Pass Greedy | $O(N)$ | $O(1)$ | [`LC0121_BestTimeToBuyAndSellStock.java`](./LC0121_BestTimeToBuyAndSellStock.java) |
| 32 | 124 | Binary Tree Maximum Path Sum | 🔴 Hard | Tree Post-Order DFS | $O(N)$ | $O(H)$ | [`LC0124_BinaryTreeMaximumPathSum.java`](./LC0124_BinaryTreeMaximumPathSum.java) |
| 33 | 133 | Clone Graph | 🟡 Medium | Graph DFS + Map | $O(V + E)$ | $O(V)$ | [`LC0133_CloneGraph.java`](./LC0133_CloneGraph.java) |
| 34 | 138 | Copy List with Random Pointer | 🟡 Medium | Interweaving Nodes | $O(N)$ | $O(1)$ | [`LC0138_CopyListWithRandomPointer.java`](./LC0138_CopyListWithRandomPointer.java) |
| 35 | 139 | Word Break | 🟡 Medium | 1D Dynamic Programming | $O(N^3)$ | $O(N + M)$ | [`LC0139_WordBreak.java`](./LC0139_WordBreak.java) |
| 36 | 146 | LRU Cache | 🟡 Medium | Doubly Linked List + Map | $O(1)$ | $O(C)$ | [`LC0146_LRUCache.java`](./LC0146_LRUCache.java) |
| 37 | 152 | Maximum Product Subarray | 🟡 Medium | Running Min/Max DP | $O(N)$ | $O(1)$ | [`LC0152_MaximumProductSubarray.java`](./LC0152_MaximumProductSubarray.java) |
| 38 | 153 | Find Minimum in Rotated Sorted Array | 🟡 Medium | Binary Search | $O(\log N)$ | $O(1)$ | [`LC0153_FindMinimumInRotatedSortedArray.java`](./LC0153_FindMinimumInRotatedSortedArray.java) |
| 39 | 198 | House Robber | 🟡 Medium | 1D Dynamic Programming | $O(N)$ | $O(1)$ | [`LC0198_HouseRobber.java`](./LC0198_HouseRobber.java) |
| 40 | 200 | Number of Islands | 🟡 Medium | Grid DFS / Flood Fill | $O(M \cdot N)$ | $O(M \cdot N)$ | [`LC0200_NumberOfIslands.java`](./LC0200_NumberOfIslands.java) |
| 41 | 206 | Reverse Linked List | 🟢 Easy | Iterative 3-Pointer | $O(N)$ | $O(1)$ | [`LC0206_ReverseLinkedList.java`](./LC0206_ReverseLinkedList.java) |
| 42 | 207 | Course Schedule | 🟡 Medium | Kahn's Topological Sort | $O(V + E)$ | $O(V + E)$ | [`LC0207_CourseSchedule.java`](./LC0207_CourseSchedule.java) |
| 43 | 208 | Implement Trie (Prefix Tree) | 🟡 Medium | 26-ary Trie Tree | $O(L)$ | $O(\Sigma \cdot L)$ | [`LC0208_ImplementTrie.java`](./LC0208_ImplementTrie.java) |
| 44 | 215 | Kth Largest Element in an Array | 🟡 Medium | Min-Heap PriorityQueue | $O(N \log K)$ | $O(K)$ | [`LC0215_KthLargestElementInAnArray.java`](./LC0215_KthLargestElementInAnArray.java) |
| 45 | 226 | Invert Binary Tree | 🟢 Easy | Recursive DFS | $O(N)$ | $O(H)$ | [`LC0226_InvertBinaryTree.java`](./LC0226_InvertBinaryTree.java) |
| 46 | 238 | Product of Array Except Self | 🟡 Medium | Prefix & Suffix Products | $O(N)$ | $O(1)$ | [`LC0238_ProductOfArrayExceptSelf.java`](./LC0238_ProductOfArrayExceptSelf.java) |
| 47 | 300 | Longest Increasing Subsequence | 🟡 Medium | Patience Sorting + Binary Search | $O(N \log N)$ | $O(N)$ | [`LC0300_LongestIncreasingSubsequence.java`](./LC0300_LongestIncreasingSubsequence.java) |

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
