# LeetCode Solutions in Java 🚀

A curated collection of **131 comprehensive, production-grade Java solutions** to top LeetCode algorithm and data structure problems. Each solution includes problem statement references, algorithmic breakdowns, Big-O time and space complexity analyses, and self-contained executable `main()` test cases.

---

## ⚡ Intelligent Auto-Detector & Mobile Submissions Runner

This repository includes an autonomous **Auto-Detector & Daily Submissions Engine** designed for seamless contribution streaks from Android (Termux) or any desktop environment.

### 📱 One-Command Daily Automation
```bash
./auto_submit.sh
# or: ./run_day.sh
```
- **Self-Detecting**: Scans repository history and automatically detects which problems have already been uploaded and which day is pending.
- **Sequential Commits**: Submits the 6 daily problems sequentially with formatted commit messages (`feat(leetcode): solve LCxxxx ...`).
- **Crash-Safe & Idempotent**: Resumes seamlessly if interrupted without duplicating commits.
- **Zero Configuration Needed**: Run once per day while on mobile/travel and it handles the rest!

To check current progress without submitting:
```bash
./run_day.sh status
```

---

## 📋 Problem Catalog (131 Solutions)

| # | Problem ID | Title | Difficulty | Category / Pattern | Time Complexity | Space Complexity | Solution File |
|---|---|---|---|---|---|---|---|
| 01 | 1 | TwoSum | 🟢 Easy | Algorithms | $O(N)$ | $O(N)$ | [`LC0001_TwoSum.java`](./LC0001_TwoSum.java) |
| 02 | 2 | AddTwoNumbers | 🟡 Medium | Algorithms | $O(max(N, M)$)$ | $O(max(N, M)$)$ | [`LC0002_AddTwoNumbers.java`](./LC0002_AddTwoNumbers.java) |
| 03 | 3 | LongestSubstringWithoutRepeatingCharacters | 🟡 Medium | Algorithms | $O(N)$ | $O(min(N, M)$)$ where M is alphabet size | [`LC0003_LongestSubstringWithoutRepeatingCharacters.java`](./LC0003_LongestSubstringWithoutRepeatingCharacters.java) |
| 04 | 4 | MedianOfTwoSortedArrays | 🔴 Hard | Algorithms | $O(log(min(M, N)$)$)$ | $O(1)$ | [`LC0004_MedianOfTwoSortedArrays.java`](./LC0004_MedianOfTwoSortedArrays.java) |
| 05 | 5 | LongestPalindromicSubstring | 🟡 Medium | Algorithms | $O(N^2)$ | $O(1)$ | [`LC0005_LongestPalindromicSubstring.java`](./LC0005_LongestPalindromicSubstring.java) |
| 06 | 6 | Zigzag Conversion | 🟡 Medium | String | $O(N)$ | $O(N)$ | [`LC0006_ZigzagConversion.java`](./LC0006_ZigzagConversion.java) |
| 07 | 8 | String to Integer (atoi) | 🟡 Medium | Strings, Math | $O(N)$ where N is length of string | $O(1)$ | [`LC0008_StringToIntegerAtoi.java`](./LC0008_StringToIntegerAtoi.java) |
| 08 | 11 | ContainerWithMostWater | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0011_ContainerWithMostWater.java`](./LC0011_ContainerWithMostWater.java) |
| 09 | 12 | Integer to Roman | 🟡 Medium | Hash Table, Math, String | $O(1)$ bounded by 3999 | $O(1)$ | [`LC0012_IntegerToRoman.java`](./LC0012_IntegerToRoman.java) |
| 10 | 13 | Roman to Integer | 🟢 Easy | Hash Table, Math, String | $O(N)$ | $O(1)$ | [`LC0013_RomanToInteger.java`](./LC0013_RomanToInteger.java) |
| 11 | 14 | Longest Common Prefix | 🟢 Easy | Strings | $O(S)$ where S is the sum of all characters in strings | $O(1)$ | [`LC0014_LongestCommonPrefix.java`](./LC0014_LongestCommonPrefix.java) |
| 12 | 15 | ThreeSum | 🟡 Medium | Algorithms | $O(N^2)$ | $O(1)$ auxiliary (ignoring output)$ | [`LC0015_ThreeSum.java`](./LC0015_ThreeSum.java) |
| 13 | 16 | 3SumClosest | 🟡 Medium | Algorithms | $O(N^2)$ | $O(1)$ | [`LC0016_3SumClosest.java`](./LC0016_3SumClosest.java) |
| 14 | 17 | LetterCombinationsOfAPhoneNumber | 🟡 Medium | Algorithms | $O(4^N)$ | $O(N)$ | [`LC0017_LetterCombinationsOfAPhoneNumber.java`](./LC0017_LetterCombinationsOfAPhoneNumber.java) |
| 15 | 18 | 4Sum | 🟡 Medium | Array, Two Pointers, Sorting | $O(N^3)$ | $O(1)$ auxiliary (ignoring output list)$ | [`LC0018_4Sum.java`](./LC0018_4Sum.java) |
| 16 | 19 | RemoveNthNodeFromEndOfList | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0019_RemoveNthNodeFromEndOfList.java`](./LC0019_RemoveNthNodeFromEndOfList.java) |
| 17 | 20 | ValidParentheses | 🟢 Easy | Algorithms | $O(N)$ | $O(N)$ | [`LC0020_ValidParentheses.java`](./LC0020_ValidParentheses.java) |
| 18 | 21 | MergeTwoSortedLists | 🟢 Easy | Algorithms | $O(N + M)$ | $O(1)$ | [`LC0021_MergeTwoSortedLists.java`](./LC0021_MergeTwoSortedLists.java) |
| 19 | 22 | GenerateParentheses | 🟡 Medium | Algorithms | $O(4^N / sqrt(N)$)$ (N-th Catalan number)$ | $O(N)$ | [`LC0022_GenerateParentheses.java`](./LC0022_GenerateParentheses.java) |
| 20 | 23 | MergeKSortedLists | 🔴 Hard | Algorithms | $O(N log k)$ where N is total nodes, k is number of lists | $O(k)$ for heap | [`LC0023_MergeKSortedLists.java`](./LC0023_MergeKSortedLists.java) |
| 21 | 24 | SwapNodesInPairs | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0024_SwapNodesInPairs.java`](./LC0024_SwapNodesInPairs.java) |
| 22 | 26 | RemoveDuplicatesFromSortedArray | 🟢 Easy | Algorithms | $O(N)$ | $O(1)$ | [`LC0026_RemoveDuplicatesFromSortedArray.java`](./LC0026_RemoveDuplicatesFromSortedArray.java) |
| 23 | 27 | Remove Element | 🟢 Easy | Array, Two Pointers | $O(N)$ | $O(1)$ | [`LC0027_RemoveElement.java`](./LC0027_RemoveElement.java) |
| 24 | 28 | Find the Index of the First Occurrence in a String | 🟢 Easy | Strings, Two Pointers, String Matching (KMP) | $O(N + M)$ where N = haystack.length()$, M = needle.length()$ | $O(M)$ for LPS array | [`LC0028_FindTheIndexOfTheFirstOccurrenceInAString.java`](./LC0028_FindTheIndexOfTheFirstOccurrenceInAString.java) |
| 25 | 33 | SearchInRotatedSortedArray | 🟡 Medium | Algorithms | $O(log N)$ | $O(1)$ | [`LC0033_SearchInRotatedSortedArray.java`](./LC0033_SearchInRotatedSortedArray.java) |
| 26 | 34 | FindFirstAndLastPositionOfElementInSortedArray | 🟡 Medium | Algorithms | $O(log N)$ | $O(1)$ | [`LC0034_FindFirstAndLastPositionOfElementInSortedArray.java`](./LC0034_FindFirstAndLastPositionOfElementInSortedArray.java) |
| 27 | 35 | SearchInsertPosition | 🟢 Easy | Algorithms | $O(log N)$ | $O(1)$ | [`LC0035_SearchInsertPosition.java`](./LC0035_SearchInsertPosition.java) |
| 28 | 36 | Valid Sudoku | 🟡 Medium | Array, Hash Table, Matrix | $O(1)$ fixed 9x9 board = 81 cells | $O(1)$ fixed 9x9 board | [`LC0036_ValidSudoku.java`](./LC0036_ValidSudoku.java) |
| 29 | 39 | CombinationSum | 🟡 Medium | Algorithms | $O(2^(Target / Min_Candidate)$)$ | $O(Target / Min_Candidate)$ | [`LC0039_CombinationSum.java`](./LC0039_CombinationSum.java) |
| 30 | 40 | CombinationSumII | 🟡 Medium | Algorithms | $O(2^N)$ | $O(N)$ | [`LC0040_CombinationSumII.java`](./LC0040_CombinationSumII.java) |
| 31 | 42 | TrappingRainWater | 🔴 Hard | Algorithms | $O(N)$ | $O(1)$ | [`LC0042_TrappingRainWater.java`](./LC0042_TrappingRainWater.java) |
| 32 | 43 | Multiply Strings | 🟡 Medium | Math, String, Simulation | $O(N * M)$ | $O(N + M)$ | [`LC0043_MultiplyStrings.java`](./LC0043_MultiplyStrings.java) |
| 33 | 45 | Jump Game II | 🟡 Medium | Array, Dynamic Programming, Greedy | $O(N)$ | $O(1)$ | [`LC0045_JumpGameII.java`](./LC0045_JumpGameII.java) |
| 34 | 46 | Permutations | 🟡 Medium | Algorithms | $O(N * N!)$ | $O(N)$ recursion stack | [`LC0046_Permutations.java`](./LC0046_Permutations.java) |
| 35 | 48 | RotateImage | 🟡 Medium | Algorithms | $O(N^2)$ | $O(1)$ in-place | [`LC0048_RotateImage.java`](./LC0048_RotateImage.java) |
| 36 | 49 | GroupAnagrams | 🟡 Medium | Algorithms | $O(N * K)$ where K is max string length | $O(N * K)$ | [`LC0049_GroupAnagrams.java`](./LC0049_GroupAnagrams.java) |
| 37 | 53 | MaximumSubarray | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0053_MaximumSubarray.java`](./LC0053_MaximumSubarray.java) |
| 38 | 54 | SpiralMatrix | 🟡 Medium | Algorithms | $O(M * N)$ | $O(1)$ | [`LC0054_SpiralMatrix.java`](./LC0054_SpiralMatrix.java) |
| 39 | 55 | JumpGame | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0055_JumpGame.java`](./LC0055_JumpGame.java) |
| 40 | 56 | MergeIntervals | 🟡 Medium | Algorithms | $O(N log N)$ | $O(N)$ | [`LC0056_MergeIntervals.java`](./LC0056_MergeIntervals.java) |
| 41 | 57 | Insert Interval | 🟡 Medium | Array, Intervals | $O(N)$ | $O(N)$ for output | [`LC0057_InsertInterval.java`](./LC0057_InsertInterval.java) |
| 42 | 58 | Length of Last Word | 🟢 Easy | String | $O(N)$ | $O(1)$ | [`LC0058_LengthOfLastWord.java`](./LC0058_LengthOfLastWord.java) |
| 43 | 61 | RotateList | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0061_RotateList.java`](./LC0061_RotateList.java) |
| 44 | 62 | UniquePaths | 🟡 Medium | Algorithms | $O(M * N)$ | $O(N)$ | [`LC0062_UniquePaths.java`](./LC0062_UniquePaths.java) |
| 45 | 63 | Unique Paths II | 🟡 Medium | Array, Dynamic Programming, Matrix | $O(M * N)$ | $O(N)$ | [`LC0063_UniquePathsII.java`](./LC0063_UniquePathsII.java) |
| 46 | 64 | MinimumPathSum | 🟡 Medium | Algorithms | $O(M * N)$ | $O(1)$ in-place | [`LC0064_MinimumPathSum.java`](./LC0064_MinimumPathSum.java) |
| 47 | 66 | Plus One | 🟢 Easy | Array, Math | $O(N)$ where N is number of digits | $O(1)$ in-place (or $O(N)$ only if all digits are 9)$ | [`LC0066_PlusOne.java`](./LC0066_PlusOne.java) |
| 48 | 69 | Sqrt(x) | 🟢 Easy | Math, Binary Search | $O(log x)$ | $O(1)$ | [`LC0069_Sqrtx.java`](./LC0069_Sqrtx.java) |
| 49 | 70 | ClimbingStairs | 🟢 Easy | Algorithms | $O(N)$ | $O(1)$ | [`LC0070_ClimbingStairs.java`](./LC0070_ClimbingStairs.java) |
| 50 | 72 | EditDistance | 🟡 Medium | Algorithms | $O(M * N)$ | $O(N)$ | [`LC0072_EditDistance.java`](./LC0072_EditDistance.java) |
| 51 | 73 | SetMatrixZeroes | 🟡 Medium | Algorithms | $O(M * N)$ | $O(1)$ | [`LC0073_SetMatrixZeroes.java`](./LC0073_SetMatrixZeroes.java) |
| 52 | 74 | SearchA2DMatrix | 🟡 Medium | Algorithms | $O(log(M * N)$)$ | $O(1)$ | [`LC0074_SearchA2DMatrix.java`](./LC0074_SearchA2DMatrix.java) |
| 53 | 75 | SortColors | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0075_SortColors.java`](./LC0075_SortColors.java) |
| 54 | 76 | MinimumWindowSubstring | 🔴 Hard | Algorithms | $O(S + T)$ | $O(S + T)$ | [`LC0076_MinimumWindowSubstring.java`](./LC0076_MinimumWindowSubstring.java) |
| 55 | 78 | Subsets | 🟡 Medium | Algorithms | $O(N * 2^N)$ | $O(N)$ | [`LC0078_Subsets.java`](./LC0078_Subsets.java) |
| 56 | 79 | WordSearch | 🟡 Medium | Algorithms | $O(M * N * 3^L)$ where L is length of word | $O(L)$ recursion stack depth | [`LC0079_WordSearch.java`](./LC0079_WordSearch.java) |
| 57 | 80 | Remove Duplicates from Sorted Array II | 🟡 Medium | Array, Two Pointers | $O(N)$ | $O(1)$ | [`LC0080_RemoveDuplicatesFromSortedArrayII.java`](./LC0080_RemoveDuplicatesFromSortedArrayII.java) |
| 58 | 81 | Search in Rotated Sorted Array II | 🟡 Medium | Array, Binary Search | $O(log N)$ average, $O(N)$ worst-case with all duplicates | $O(1)$ | [`LC0081_SearchInRotatedSortedArrayII.java`](./LC0081_SearchInRotatedSortedArrayII.java) |
| 59 | 82 | Remove Duplicates from Sorted List II | 🟡 Medium | Linked List, Two Pointers | $O(N)$ | $O(1)$ | [`LC0082_RemoveDuplicatesFromSortedListII.java`](./LC0082_RemoveDuplicatesFromSortedListII.java) |
| 60 | 83 | Remove Duplicates from Sorted List | 🟢 Easy | Linked List | $O(N)$ | $O(1)$ | [`LC0083_RemoveDuplicatesFromSortedList.java`](./LC0083_RemoveDuplicatesFromSortedList.java) |
| 61 | 84 | LargestRectangleInHistogram | 🔴 Hard | Algorithms | $O(N)$ | $O(N)$ | [`LC0084_LargestRectangleInHistogram.java`](./LC0084_LargestRectangleInHistogram.java) |
| 62 | 86 | Partition List | 🟡 Medium | Linked List, Two Pointers | $O(N)$ | $O(1)$ | [`LC0086_PartitionList.java`](./LC0086_PartitionList.java) |
| 63 | 88 | Merge Sorted Array | 🟢 Easy | Array, Two Pointers, Sorting | $O(M + N)$ | $O(1)$ | [`LC0088_MergeSortedArray.java`](./LC0088_MergeSortedArray.java) |
| 64 | 91 | DecodeWays | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0091_DecodeWays.java`](./LC0091_DecodeWays.java) |
| 65 | 92 | Reverse Linked List II | 🟡 Medium | Linked List | $O(N)$ | $O(1)$ | [`LC0092_ReverseLinkedListII.java`](./LC0092_ReverseLinkedListII.java) |
| 66 | 98 | ValidateBinarySearchTree | 🟡 Medium | Algorithms | $O(N)$ | $O(H)$ call stack height | [`LC0098_ValidateBinarySearchTree.java`](./LC0098_ValidateBinarySearchTree.java) |
| 67 | 100 | SameTree | 🟢 Easy | Algorithms | $O(N)$ | $O(H)$ where H is tree height | [`LC0100_SameTree.java`](./LC0100_SameTree.java) |
| 68 | 101 | SymmetricTree | 🟢 Easy | Algorithms | $O(N)$ | $O(H)$ where H is tree height | [`LC0101_SymmetricTree.java`](./LC0101_SymmetricTree.java) |
| 69 | 102 | BinaryTreeLevelOrderTraversal | 🟡 Medium | Algorithms | $O(N)$ | $O(N)$ | [`LC0102_BinaryTreeLevelOrderTraversal.java`](./LC0102_BinaryTreeLevelOrderTraversal.java) |
| 70 | 103 | BinaryTreeZigzagLevelOrderTraversal | 🟡 Medium | Algorithms | $O(N)$ | $O(N)$ | [`LC0103_BinaryTreeZigzagLevelOrderTraversal.java`](./LC0103_BinaryTreeZigzagLevelOrderTraversal.java) |
| 71 | 104 | MaximumDepthOfBinaryTree | 🟢 Easy | Algorithms | $O(N)$ | $O(H)$ where H is tree height | [`LC0104_MaximumDepthOfBinaryTree.java`](./LC0104_MaximumDepthOfBinaryTree.java) |
| 72 | 105 | ConstructBinaryTreeFromPreorderAndInorderTraversal | 🟡 Medium | Algorithms | $O(N)$ | $O(N)$ | [`LC0105_ConstructBinaryTreeFromPreorderAndInorderTraversal.java`](./LC0105_ConstructBinaryTreeFromPreorderAndInorderTraversal.java) |
| 73 | 108 | Convert Sorted Array to Binary Search Tree | 🟢 Easy | Tree, Binary Search Tree, Binary Tree, Divide and Conquer | $O(N)$ | $O(log N)$ recursion stack | [`LC0108_ConvertSortedArrayToBST.java`](./LC0108_ConvertSortedArrayToBST.java) |
| 74 | 110 | BalancedBinaryTree | 🟢 Easy | Algorithms | $O(N)$ | $O(H)$ where H is tree height | [`LC0110_BalancedBinaryTree.java`](./LC0110_BalancedBinaryTree.java) |
| 75 | 111 | Minimum Depth of Binary Tree | 🟢 Easy | Tree, Depth-First Search, Breadth-First Search, Binary Tree | $O(N)$ | $O(N)$ | [`LC0111_MinimumDepthOfBinaryTree.java`](./LC0111_MinimumDepthOfBinaryTree.java) |
| 76 | 112 | Path Sum | 🟢 Easy | Tree, Depth-First Search, Binary Tree | $O(N)$ | $O(H)$ where H is tree height | [`LC0112_PathSum.java`](./LC0112_PathSum.java) |
| 77 | 113 | Path Sum II | 🟡 Medium | Tree, Backtracking, Depth-First Search, Binary Tree | $O(N)$ | $O(H)$ recursion stack | [`LC0113_PathSumII.java`](./LC0113_PathSumII.java) |
| 78 | 120 | Triangle | 🟡 Medium | Algorithms | $O(N^2)$ | $O(N)$ | [`LC0120_Triangle.java`](./LC0120_Triangle.java) |
| 79 | 121 | BestTimeToBuyAndSellStock | 🟢 Easy | Algorithms | $O(N)$ | $O(1)$ | [`LC0121_BestTimeToBuyAndSellStock.java`](./LC0121_BestTimeToBuyAndSellStock.java) |
| 80 | 124 | BinaryTreeMaximumPathSum | 🔴 Hard | Algorithms | $O(N)$ | $O(H)$ recursion height | [`LC0124_BinaryTreeMaximumPathSum.java`](./LC0124_BinaryTreeMaximumPathSum.java) |
| 81 | 125 | Valid Palindrome | 🟢 Easy | Two Pointers, String | $O(N)$ | $O(1)$ | [`LC0125_ValidPalindrome.java`](./LC0125_ValidPalindrome.java) |
| 82 | 128 | LongestConsecutiveSequence | 🟡 Medium | Algorithms | $O(N)$ | $O(N)$ | [`LC0128_LongestConsecutiveSequence.java`](./LC0128_LongestConsecutiveSequence.java) |
| 83 | 129 | Sum Root to Leaf Numbers | 🟡 Medium | Tree, Depth-First Search, Binary Tree | $O(N)$ | $O(H)$ | [`LC0129_SumRootToLeafNumbers.java`](./LC0129_SumRootToLeafNumbers.java) |
| 84 | 133 | CloneGraph | 🟡 Medium | Algorithms | $O(V + E)$ | $O(V)$ | [`LC0133_CloneGraph.java`](./LC0133_CloneGraph.java) |
| 85 | 134 | Gas Station | 🟡 Medium | Array, Greedy | $O(N)$ | $O(1)$ | [`LC0134_GasStation.java`](./LC0134_GasStation.java) |
| 86 | 138 | CopyListWithRandomPointer | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0138_CopyListWithRandomPointer.java`](./LC0138_CopyListWithRandomPointer.java) |
| 87 | 139 | WordBreak | 🟡 Medium | Algorithms | $O(N^3)$ (string substring hashing)$ | $O(N + M)$ | [`LC0139_WordBreak.java`](./LC0139_WordBreak.java) |
| 88 | 141 | LinkedListCycle | 🟢 Easy | Algorithms | $O(N)$ | $O(1)$ | [`LC0141_LinkedListCycle.java`](./LC0141_LinkedListCycle.java) |
| 89 | 142 | LinkedListCycleII | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0142_LinkedListCycleII.java`](./LC0142_LinkedListCycleII.java) |
| 90 | 143 | ReorderList | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0143_ReorderList.java`](./LC0143_ReorderList.java) |
| 91 | 146 | LRUCache | 🟡 Medium | Algorithms | $O(1)$ for both get and put | $O(capacity)$ | [`LC0146_LRUCache.java`](./LC0146_LRUCache.java) |
| 92 | 150 | EvaluateReversePolishNotation | 🟡 Medium | Algorithms | $O(N)$ | $O(N)$ | [`LC0150_EvaluateReversePolishNotation.java`](./LC0150_EvaluateReversePolishNotation.java) |
| 93 | 152 | MaximumProductSubarray | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0152_MaximumProductSubarray.java`](./LC0152_MaximumProductSubarray.java) |
| 94 | 153 | FindMinimumInRotatedSortedArray | 🟡 Medium | Algorithms | $O(log N)$ | $O(1)$ | [`LC0153_FindMinimumInRotatedSortedArray.java`](./LC0153_FindMinimumInRotatedSortedArray.java) |
| 95 | 155 | MinStack | 🟡 Medium | Algorithms | $O(1)$ for all operations | $O(N)$ | [`LC0155_MinStack.java`](./LC0155_MinStack.java) |
| 96 | 160 | Intersection of Two Linked Lists | 🟢 Easy | Linked List, Two Pointers | $O(N + M)$ | $O(1)$ | [`LC0160_IntersectionOfTwoLinkedLists.java`](./LC0160_IntersectionOfTwoLinkedLists.java) |
| 97 | 162 | Find Peak Element | 🟡 Medium | Array, Binary Search | $O(log N)$ | $O(1)$ | [`LC0162_FindPeakElement.java`](./LC0162_FindPeakElement.java) |
| 98 | 167 | TwoSumIIInputArrayIsSorted | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0167_TwoSumIIInputArrayIsSorted.java`](./LC0167_TwoSumIIInputArrayIsSorted.java) |
| 99 | 189 | RotateArray | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0189_RotateArray.java`](./LC0189_RotateArray.java) |
| 100 | 198 | HouseRobber | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0198_HouseRobber.java`](./LC0198_HouseRobber.java) |
| 101 | 199 | Binary Tree Right Side View | 🟡 Medium | Tree, Depth-First Search, Breadth-First Search, Binary Tree | $O(N)$ | $O(D)$ where D is max diameter of tree | [`LC0199_BinaryTreeRightSideView.java`](./LC0199_BinaryTreeRightSideView.java) |
| 102 | 200 | NumberOfIslands | 🟡 Medium | Algorithms | $O(M * N)$ | $O(M * N)$ worst-case recursion stack | [`LC0200_NumberOfIslands.java`](./LC0200_NumberOfIslands.java) |
| 103 | 203 | Remove Linked List Elements | 🟢 Easy | Linked List, Recursion | $O(N)$ | $O(1)$ | [`LC0203_RemoveLinkedListElements.java`](./LC0203_RemoveLinkedListElements.java) |
| 104 | 206 | ReverseLinkedList | 🟢 Easy | Algorithms | $O(N)$ | $O(1)$ | [`LC0206_ReverseLinkedList.java`](./LC0206_ReverseLinkedList.java) |
| 105 | 207 | CourseSchedule | 🟡 Medium | Algorithms | $O(V + E)$ | $O(V + E)$ | [`LC0207_CourseSchedule.java`](./LC0207_CourseSchedule.java) |
| 106 | 208 | ImplementTrie | 🟡 Medium | Algorithms | $O(L)$ for insert, search, and startsWith (L = word length)$ | $O(Total inserted characters * 26)$ | [`LC0208_ImplementTrie.java`](./LC0208_ImplementTrie.java) |
| 107 | 209 | Minimum Size Subarray Sum | 🟡 Medium | Array, Binary Search, Sliding Window | $O(N)$ | $O(1)$ | [`LC0209_MinimumSizeSubarraySum.java`](./LC0209_MinimumSizeSubarraySum.java) |
| 108 | 210 | CourseScheduleII | 🟡 Medium | Algorithms | $O(V + E)$ | $O(V + E)$ | [`LC0210_CourseScheduleII.java`](./LC0210_CourseScheduleII.java) |
| 109 | 213 | House Robber II | 🟡 Medium | Array, Dynamic Programming | $O(N)$ | $O(1)$ | [`LC0213_HouseRobberII.java`](./LC0213_HouseRobberII.java) |
| 110 | 215 | KthLargestElementInAnArray | 🟡 Medium | Algorithms | $O(N log K)$ | $O(K)$ | [`LC0215_KthLargestElementInAnArray.java`](./LC0215_KthLargestElementInAnArray.java) |
| 111 | 225 | ImplementStackUsingQueues | 🟢 Easy | Algorithms | push: $O(N)$, pop/top/empty: $O(1)$ | $O(N)$ | [`LC0225_ImplementStackUsingQueues.java`](./LC0225_ImplementStackUsingQueues.java) |
| 112 | 226 | InvertBinaryTree | 🟢 Easy | Algorithms | $O(N)$ | $O(H)$ where H is tree height | [`LC0226_InvertBinaryTree.java`](./LC0226_InvertBinaryTree.java) |
| 113 | 230 | KthSmallestElementInABST | 🟡 Medium | Algorithms | $O(H + K)$ | $O(H)$ where H is tree height | [`LC0230_KthSmallestElementInABST.java`](./LC0230_KthSmallestElementInABST.java) |
| 114 | 232 | ImplementQueueUsingStacks | 🟢 Easy | Algorithms | Amortized $O(1)$ for pop and peek, $O(1)$ for push | $O(N)$ | [`LC0232_ImplementQueueUsingStacks.java`](./LC0232_ImplementQueueUsingStacks.java) |
| 115 | 234 | PalindromeLinkedList | 🟢 Easy | Algorithms | $O(N)$ | $O(1)$ | [`LC0234_PalindromeLinkedList.java`](./LC0234_PalindromeLinkedList.java) |
| 116 | 236 | LowestCommonAncestorOfABinaryTree | 🟡 Medium | Algorithms | $O(N)$ | $O(H)$ where H is tree height | [`LC0236_LowestCommonAncestorOfABinaryTree.java`](./LC0236_LowestCommonAncestorOfABinaryTree.java) |
| 117 | 238 | ProductOfArrayExceptSelf | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ auxiliary space (output array does not count toward memory)$ | [`LC0238_ProductOfArrayExceptSelf.java`](./LC0238_ProductOfArrayExceptSelf.java) |
| 118 | 240 | SearchA2DMatrixII | 🟡 Medium | Algorithms | $O(M + N)$ | $O(1)$ | [`LC0240_SearchA2DMatrixII.java`](./LC0240_SearchA2DMatrixII.java) |
| 119 | 278 | First Bad Version | 🟢 Easy | Binary Search, Interactive | $O(log N)$ | $O(1)$ | [`LC0278_FirstBadVersion.java`](./LC0278_FirstBadVersion.java) |
| 120 | 279 | Perfect Squares | 🟡 Medium | Math, Dynamic Programming, Breadth-First Search | $O(N * sqrt(N)$)$ | $O(N)$ | [`LC0279_PerfectSquares.java`](./LC0279_PerfectSquares.java) |
| 121 | 283 | Move Zeroes | 🟢 Easy | Array, Two Pointers | $O(N)$ | $O(1)$ | [`LC0283_MoveZeroes.java`](./LC0283_MoveZeroes.java) |
| 122 | 300 | LongestIncreasingSubsequence | 🟡 Medium | Algorithms | $O(N log N)$ | $O(N)$ | [`LC0300_LongestIncreasingSubsequence.java`](./LC0300_LongestIncreasingSubsequence.java) |
| 123 | 322 | CoinChange | 🟡 Medium | Algorithms | $O(Amount * Coins.length)$ | $O(Amount)$ | [`LC0322_CoinChange.java`](./LC0322_CoinChange.java) |
| 124 | 338 | Counting Bits | 🟢 Easy | Dynamic Programming, Bit Manipulation | $O(N)$ | $O(1)$ auxiliary (excluding output array)$ | [`LC0338_CountingBits.java`](./LC0338_CountingBits.java) |
| 125 | 347 | TopKFrequentElements | 🟡 Medium | Algorithms | $O(N log K)$ | $O(N + K)$ | [`LC0347_TopKFrequentElements.java`](./LC0347_TopKFrequentElements.java) |
| 126 | 373 | FindKPairsWithSmallestSums | 🟡 Medium | Algorithms | $O(K log(min(N, K)$)$)$ | $O(min(N, K)$)$ | [`LC0373_FindKPairsWithSmallestSums.java`](./LC0373_FindKPairsWithSmallestSums.java) |
| 127 | 416 | PartitionEqualSubsetSum | 🟡 Medium | Algorithms | $O(N * Target)$ | $O(Target)$ | [`LC0416_PartitionEqualSubsetSum.java`](./LC0416_PartitionEqualSubsetSum.java) |
| 128 | 424 | LongestRepeatingCharacterReplacement | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ (26 uppercase English letters)$ | [`LC0424_LongestRepeatingCharacterReplacement.java`](./LC0424_LongestRepeatingCharacterReplacement.java) |
| 129 | 435 | NonOverlappingIntervals | 🟡 Medium | Algorithms | $O(N log N)$ | $O(1)$ | [`LC0435_NonOverlappingIntervals.java`](./LC0435_NonOverlappingIntervals.java) |
| 130 | 704 | Binary Search | 🟢 Easy | Array, Binary Search | $O(log N)$ | $O(1)$ | [`LC0704_BinarySearch.java`](./LC0704_BinarySearch.java) |
| 131 | 875 | Koko Eating Bananas | 🟡 Medium | Array, Binary Search on Answer | $O(N * log(max(piles)$)$)$ | $O(1)$ | [`LC0875_KokoEatingBananas.java`](./LC0875_KokoEatingBananas.java) |

---

## 🛠 Compilation & Execution

Each Java file is completely standalone and includes its own `main` test runner.

```bash
# Compile any single solution
javac LC0001_TwoSum.java

# Run test cases
java LC0001_TwoSum
```

To compile all files at once:
```bash
javac *.java
```
