# LeetCode Solutions in Java 🚀

A curated collection of **95 comprehensive, production-grade Java solutions** to top LeetCode algorithm and data structure problems. Each solution includes problem statement references, algorithmic breakdowns, Big-O time and space complexity analyses, and self-contained executable `main()` test cases.

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

## 📋 Problem Catalog (95 Solutions)

| # | Problem ID | Title | Difficulty | Category / Pattern | Time Complexity | Space Complexity | Solution File |
|---|---|---|---|---|---|---|---|
| 01 | 1 | TwoSum | 🟢 Easy | Algorithms | $O(N)$ | $O(N)$ | [`LC0001_TwoSum.java`](./LC0001_TwoSum.java) |
| 02 | 2 | AddTwoNumbers | 🟡 Medium | Algorithms | $O(max(N, M)$)$ | $O(max(N, M)$)$ | [`LC0002_AddTwoNumbers.java`](./LC0002_AddTwoNumbers.java) |
| 03 | 3 | LongestSubstringWithoutRepeatingCharacters | 🟡 Medium | Algorithms | $O(N)$ | $O(min(N, M)$)$ where M is alphabet size | [`LC0003_LongestSubstringWithoutRepeatingCharacters.java`](./LC0003_LongestSubstringWithoutRepeatingCharacters.java) |
| 04 | 4 | MedianOfTwoSortedArrays | 🔴 Hard | Algorithms | $O(log(min(M, N)$)$)$ | $O(1)$ | [`LC0004_MedianOfTwoSortedArrays.java`](./LC0004_MedianOfTwoSortedArrays.java) |
| 05 | 5 | LongestPalindromicSubstring | 🟡 Medium | Algorithms | $O(N^2)$ | $O(1)$ | [`LC0005_LongestPalindromicSubstring.java`](./LC0005_LongestPalindromicSubstring.java) |
| 06 | 8 | String to Integer (atoi) | 🟡 Medium | Strings, Math | $O(N)$ where N is length of string | $O(1)$ | [`LC0008_StringToIntegerAtoi.java`](./LC0008_StringToIntegerAtoi.java) |
| 07 | 11 | ContainerWithMostWater | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0011_ContainerWithMostWater.java`](./LC0011_ContainerWithMostWater.java) |
| 08 | 14 | Longest Common Prefix | 🟢 Easy | Strings | $O(S)$ where S is the sum of all characters in strings | $O(1)$ | [`LC0014_LongestCommonPrefix.java`](./LC0014_LongestCommonPrefix.java) |
| 09 | 15 | ThreeSum | 🟡 Medium | Algorithms | $O(N^2)$ | $O(1)$ auxiliary (ignoring output)$ | [`LC0015_ThreeSum.java`](./LC0015_ThreeSum.java) |
| 10 | 16 | 3SumClosest | 🟡 Medium | Algorithms | $O(N^2)$ | $O(1)$ | [`LC0016_3SumClosest.java`](./LC0016_3SumClosest.java) |
| 11 | 17 | LetterCombinationsOfAPhoneNumber | 🟡 Medium | Algorithms | $O(4^N)$ | $O(N)$ | [`LC0017_LetterCombinationsOfAPhoneNumber.java`](./LC0017_LetterCombinationsOfAPhoneNumber.java) |
| 12 | 19 | RemoveNthNodeFromEndOfList | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0019_RemoveNthNodeFromEndOfList.java`](./LC0019_RemoveNthNodeFromEndOfList.java) |
| 13 | 20 | ValidParentheses | 🟢 Easy | Algorithms | $O(N)$ | $O(N)$ | [`LC0020_ValidParentheses.java`](./LC0020_ValidParentheses.java) |
| 14 | 21 | MergeTwoSortedLists | 🟢 Easy | Algorithms | $O(N + M)$ | $O(1)$ | [`LC0021_MergeTwoSortedLists.java`](./LC0021_MergeTwoSortedLists.java) |
| 15 | 22 | GenerateParentheses | 🟡 Medium | Algorithms | $O(4^N / sqrt(N)$)$ (N-th Catalan number)$ | $O(N)$ | [`LC0022_GenerateParentheses.java`](./LC0022_GenerateParentheses.java) |
| 16 | 23 | MergeKSortedLists | 🔴 Hard | Algorithms | $O(N log k)$ where N is total nodes, k is number of lists | $O(k)$ for heap | [`LC0023_MergeKSortedLists.java`](./LC0023_MergeKSortedLists.java) |
| 17 | 24 | SwapNodesInPairs | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0024_SwapNodesInPairs.java`](./LC0024_SwapNodesInPairs.java) |
| 18 | 26 | RemoveDuplicatesFromSortedArray | 🟢 Easy | Algorithms | $O(N)$ | $O(1)$ | [`LC0026_RemoveDuplicatesFromSortedArray.java`](./LC0026_RemoveDuplicatesFromSortedArray.java) |
| 19 | 28 | Find the Index of the First Occurrence in a String | 🟢 Easy | Strings, Two Pointers, String Matching (KMP) | $O(N + M)$ where N = haystack.length()$, M = needle.length()$ | $O(M)$ for LPS array | [`LC0028_FindTheIndexOfTheFirstOccurrenceInAString.java`](./LC0028_FindTheIndexOfTheFirstOccurrenceInAString.java) |
| 20 | 33 | SearchInRotatedSortedArray | 🟡 Medium | Algorithms | $O(log N)$ | $O(1)$ | [`LC0033_SearchInRotatedSortedArray.java`](./LC0033_SearchInRotatedSortedArray.java) |
| 21 | 34 | FindFirstAndLastPositionOfElementInSortedArray | 🟡 Medium | Algorithms | $O(log N)$ | $O(1)$ | [`LC0034_FindFirstAndLastPositionOfElementInSortedArray.java`](./LC0034_FindFirstAndLastPositionOfElementInSortedArray.java) |
| 22 | 35 | SearchInsertPosition | 🟢 Easy | Algorithms | $O(log N)$ | $O(1)$ | [`LC0035_SearchInsertPosition.java`](./LC0035_SearchInsertPosition.java) |
| 23 | 36 | Valid Sudoku | 🟡 Medium | Array, Hash Table, Matrix | $O(1)$ fixed 9x9 board = 81 cells | $O(1)$ fixed 9x9 board | [`LC0036_ValidSudoku.java`](./LC0036_ValidSudoku.java) |
| 24 | 39 | CombinationSum | 🟡 Medium | Algorithms | $O(2^(Target / Min_Candidate)$)$ | $O(Target / Min_Candidate)$ | [`LC0039_CombinationSum.java`](./LC0039_CombinationSum.java) |
| 25 | 40 | CombinationSumII | 🟡 Medium | Algorithms | $O(2^N)$ | $O(N)$ | [`LC0040_CombinationSumII.java`](./LC0040_CombinationSumII.java) |
| 26 | 42 | TrappingRainWater | 🔴 Hard | Algorithms | $O(N)$ | $O(1)$ | [`LC0042_TrappingRainWater.java`](./LC0042_TrappingRainWater.java) |
| 27 | 46 | Permutations | 🟡 Medium | Algorithms | $O(N * N!)$ | $O(N)$ recursion stack | [`LC0046_Permutations.java`](./LC0046_Permutations.java) |
| 28 | 48 | RotateImage | 🟡 Medium | Algorithms | $O(N^2)$ | $O(1)$ in-place | [`LC0048_RotateImage.java`](./LC0048_RotateImage.java) |
| 29 | 49 | GroupAnagrams | 🟡 Medium | Algorithms | $O(N * K)$ where K is max string length | $O(N * K)$ | [`LC0049_GroupAnagrams.java`](./LC0049_GroupAnagrams.java) |
| 30 | 53 | MaximumSubarray | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0053_MaximumSubarray.java`](./LC0053_MaximumSubarray.java) |
| 31 | 54 | SpiralMatrix | 🟡 Medium | Algorithms | $O(M * N)$ | $O(1)$ | [`LC0054_SpiralMatrix.java`](./LC0054_SpiralMatrix.java) |
| 32 | 55 | JumpGame | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0055_JumpGame.java`](./LC0055_JumpGame.java) |
| 33 | 56 | MergeIntervals | 🟡 Medium | Algorithms | $O(N log N)$ | $O(N)$ | [`LC0056_MergeIntervals.java`](./LC0056_MergeIntervals.java) |
| 34 | 61 | RotateList | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0061_RotateList.java`](./LC0061_RotateList.java) |
| 35 | 62 | UniquePaths | 🟡 Medium | Algorithms | $O(M * N)$ | $O(N)$ | [`LC0062_UniquePaths.java`](./LC0062_UniquePaths.java) |
| 36 | 64 | MinimumPathSum | 🟡 Medium | Algorithms | $O(M * N)$ | $O(1)$ in-place | [`LC0064_MinimumPathSum.java`](./LC0064_MinimumPathSum.java) |
| 37 | 66 | Plus One | 🟢 Easy | Array, Math | $O(N)$ where N is number of digits | $O(1)$ in-place (or $O(N)$ only if all digits are 9)$ | [`LC0066_PlusOne.java`](./LC0066_PlusOne.java) |
| 38 | 69 | Sqrt(x) | 🟢 Easy | Math, Binary Search | $O(log x)$ | $O(1)$ | [`LC0069_Sqrtx.java`](./LC0069_Sqrtx.java) |
| 39 | 70 | ClimbingStairs | 🟢 Easy | Algorithms | $O(N)$ | $O(1)$ | [`LC0070_ClimbingStairs.java`](./LC0070_ClimbingStairs.java) |
| 40 | 72 | EditDistance | 🟡 Medium | Algorithms | $O(M * N)$ | $O(N)$ | [`LC0072_EditDistance.java`](./LC0072_EditDistance.java) |
| 41 | 73 | SetMatrixZeroes | 🟡 Medium | Algorithms | $O(M * N)$ | $O(1)$ | [`LC0073_SetMatrixZeroes.java`](./LC0073_SetMatrixZeroes.java) |
| 42 | 74 | SearchA2DMatrix | 🟡 Medium | Algorithms | $O(log(M * N)$)$ | $O(1)$ | [`LC0074_SearchA2DMatrix.java`](./LC0074_SearchA2DMatrix.java) |
| 43 | 75 | SortColors | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0075_SortColors.java`](./LC0075_SortColors.java) |
| 44 | 76 | MinimumWindowSubstring | 🔴 Hard | Algorithms | $O(S + T)$ | $O(S + T)$ | [`LC0076_MinimumWindowSubstring.java`](./LC0076_MinimumWindowSubstring.java) |
| 45 | 78 | Subsets | 🟡 Medium | Algorithms | $O(N * 2^N)$ | $O(N)$ | [`LC0078_Subsets.java`](./LC0078_Subsets.java) |
| 46 | 79 | WordSearch | 🟡 Medium | Algorithms | $O(M * N * 3^L)$ where L is length of word | $O(L)$ recursion stack depth | [`LC0079_WordSearch.java`](./LC0079_WordSearch.java) |
| 47 | 84 | LargestRectangleInHistogram | 🔴 Hard | Algorithms | $O(N)$ | $O(N)$ | [`LC0084_LargestRectangleInHistogram.java`](./LC0084_LargestRectangleInHistogram.java) |
| 48 | 91 | DecodeWays | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0091_DecodeWays.java`](./LC0091_DecodeWays.java) |
| 49 | 98 | ValidateBinarySearchTree | 🟡 Medium | Algorithms | $O(N)$ | $O(H)$ call stack height | [`LC0098_ValidateBinarySearchTree.java`](./LC0098_ValidateBinarySearchTree.java) |
| 50 | 100 | SameTree | 🟢 Easy | Algorithms | $O(N)$ | $O(H)$ where H is tree height | [`LC0100_SameTree.java`](./LC0100_SameTree.java) |
| 51 | 101 | SymmetricTree | 🟢 Easy | Algorithms | $O(N)$ | $O(H)$ where H is tree height | [`LC0101_SymmetricTree.java`](./LC0101_SymmetricTree.java) |
| 52 | 102 | BinaryTreeLevelOrderTraversal | 🟡 Medium | Algorithms | $O(N)$ | $O(N)$ | [`LC0102_BinaryTreeLevelOrderTraversal.java`](./LC0102_BinaryTreeLevelOrderTraversal.java) |
| 53 | 103 | BinaryTreeZigzagLevelOrderTraversal | 🟡 Medium | Algorithms | $O(N)$ | $O(N)$ | [`LC0103_BinaryTreeZigzagLevelOrderTraversal.java`](./LC0103_BinaryTreeZigzagLevelOrderTraversal.java) |
| 54 | 104 | MaximumDepthOfBinaryTree | 🟢 Easy | Algorithms | $O(N)$ | $O(H)$ where H is tree height | [`LC0104_MaximumDepthOfBinaryTree.java`](./LC0104_MaximumDepthOfBinaryTree.java) |
| 55 | 105 | ConstructBinaryTreeFromPreorderAndInorderTraversal | 🟡 Medium | Algorithms | $O(N)$ | $O(N)$ | [`LC0105_ConstructBinaryTreeFromPreorderAndInorderTraversal.java`](./LC0105_ConstructBinaryTreeFromPreorderAndInorderTraversal.java) |
| 56 | 110 | BalancedBinaryTree | 🟢 Easy | Algorithms | $O(N)$ | $O(H)$ where H is tree height | [`LC0110_BalancedBinaryTree.java`](./LC0110_BalancedBinaryTree.java) |
| 57 | 120 | Triangle | 🟡 Medium | Algorithms | $O(N^2)$ | $O(N)$ | [`LC0120_Triangle.java`](./LC0120_Triangle.java) |
| 58 | 121 | BestTimeToBuyAndSellStock | 🟢 Easy | Algorithms | $O(N)$ | $O(1)$ | [`LC0121_BestTimeToBuyAndSellStock.java`](./LC0121_BestTimeToBuyAndSellStock.java) |
| 59 | 124 | BinaryTreeMaximumPathSum | 🔴 Hard | Algorithms | $O(N)$ | $O(H)$ recursion height | [`LC0124_BinaryTreeMaximumPathSum.java`](./LC0124_BinaryTreeMaximumPathSum.java) |
| 60 | 128 | LongestConsecutiveSequence | 🟡 Medium | Algorithms | $O(N)$ | $O(N)$ | [`LC0128_LongestConsecutiveSequence.java`](./LC0128_LongestConsecutiveSequence.java) |
| 61 | 133 | CloneGraph | 🟡 Medium | Algorithms | $O(V + E)$ | $O(V)$ | [`LC0133_CloneGraph.java`](./LC0133_CloneGraph.java) |
| 62 | 138 | CopyListWithRandomPointer | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0138_CopyListWithRandomPointer.java`](./LC0138_CopyListWithRandomPointer.java) |
| 63 | 139 | WordBreak | 🟡 Medium | Algorithms | $O(N^3)$ (string substring hashing)$ | $O(N + M)$ | [`LC0139_WordBreak.java`](./LC0139_WordBreak.java) |
| 64 | 141 | LinkedListCycle | 🟢 Easy | Algorithms | $O(N)$ | $O(1)$ | [`LC0141_LinkedListCycle.java`](./LC0141_LinkedListCycle.java) |
| 65 | 142 | LinkedListCycleII | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0142_LinkedListCycleII.java`](./LC0142_LinkedListCycleII.java) |
| 66 | 143 | ReorderList | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0143_ReorderList.java`](./LC0143_ReorderList.java) |
| 67 | 146 | LRUCache | 🟡 Medium | Algorithms | $O(1)$ for both get and put | $O(capacity)$ | [`LC0146_LRUCache.java`](./LC0146_LRUCache.java) |
| 68 | 150 | EvaluateReversePolishNotation | 🟡 Medium | Algorithms | $O(N)$ | $O(N)$ | [`LC0150_EvaluateReversePolishNotation.java`](./LC0150_EvaluateReversePolishNotation.java) |
| 69 | 152 | MaximumProductSubarray | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0152_MaximumProductSubarray.java`](./LC0152_MaximumProductSubarray.java) |
| 70 | 153 | FindMinimumInRotatedSortedArray | 🟡 Medium | Algorithms | $O(log N)$ | $O(1)$ | [`LC0153_FindMinimumInRotatedSortedArray.java`](./LC0153_FindMinimumInRotatedSortedArray.java) |
| 71 | 155 | MinStack | 🟡 Medium | Algorithms | $O(1)$ for all operations | $O(N)$ | [`LC0155_MinStack.java`](./LC0155_MinStack.java) |
| 72 | 167 | TwoSumIIInputArrayIsSorted | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0167_TwoSumIIInputArrayIsSorted.java`](./LC0167_TwoSumIIInputArrayIsSorted.java) |
| 73 | 189 | RotateArray | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0189_RotateArray.java`](./LC0189_RotateArray.java) |
| 74 | 198 | HouseRobber | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ | [`LC0198_HouseRobber.java`](./LC0198_HouseRobber.java) |
| 75 | 200 | NumberOfIslands | 🟡 Medium | Algorithms | $O(M * N)$ | $O(M * N)$ worst-case recursion stack | [`LC0200_NumberOfIslands.java`](./LC0200_NumberOfIslands.java) |
| 76 | 206 | ReverseLinkedList | 🟢 Easy | Algorithms | $O(N)$ | $O(1)$ | [`LC0206_ReverseLinkedList.java`](./LC0206_ReverseLinkedList.java) |
| 77 | 207 | CourseSchedule | 🟡 Medium | Algorithms | $O(V + E)$ | $O(V + E)$ | [`LC0207_CourseSchedule.java`](./LC0207_CourseSchedule.java) |
| 78 | 208 | ImplementTrie | 🟡 Medium | Algorithms | $O(L)$ for insert, search, and startsWith (L = word length)$ | $O(Total inserted characters * 26)$ | [`LC0208_ImplementTrie.java`](./LC0208_ImplementTrie.java) |
| 79 | 210 | CourseScheduleII | 🟡 Medium | Algorithms | $O(V + E)$ | $O(V + E)$ | [`LC0210_CourseScheduleII.java`](./LC0210_CourseScheduleII.java) |
| 80 | 215 | KthLargestElementInAnArray | 🟡 Medium | Algorithms | $O(N log K)$ | $O(K)$ | [`LC0215_KthLargestElementInAnArray.java`](./LC0215_KthLargestElementInAnArray.java) |
| 81 | 225 | ImplementStackUsingQueues | 🟢 Easy | Algorithms | push: $O(N)$, pop/top/empty: $O(1)$ | $O(N)$ | [`LC0225_ImplementStackUsingQueues.java`](./LC0225_ImplementStackUsingQueues.java) |
| 82 | 226 | InvertBinaryTree | 🟢 Easy | Algorithms | $O(N)$ | $O(H)$ where H is tree height | [`LC0226_InvertBinaryTree.java`](./LC0226_InvertBinaryTree.java) |
| 83 | 230 | KthSmallestElementInABST | 🟡 Medium | Algorithms | $O(H + K)$ | $O(H)$ where H is tree height | [`LC0230_KthSmallestElementInABST.java`](./LC0230_KthSmallestElementInABST.java) |
| 84 | 232 | ImplementQueueUsingStacks | 🟢 Easy | Algorithms | Amortized $O(1)$ for pop and peek, $O(1)$ for push | $O(N)$ | [`LC0232_ImplementQueueUsingStacks.java`](./LC0232_ImplementQueueUsingStacks.java) |
| 85 | 234 | PalindromeLinkedList | 🟢 Easy | Algorithms | $O(N)$ | $O(1)$ | [`LC0234_PalindromeLinkedList.java`](./LC0234_PalindromeLinkedList.java) |
| 86 | 236 | LowestCommonAncestorOfABinaryTree | 🟡 Medium | Algorithms | $O(N)$ | $O(H)$ where H is tree height | [`LC0236_LowestCommonAncestorOfABinaryTree.java`](./LC0236_LowestCommonAncestorOfABinaryTree.java) |
| 87 | 238 | ProductOfArrayExceptSelf | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ auxiliary space (output array does not count toward memory)$ | [`LC0238_ProductOfArrayExceptSelf.java`](./LC0238_ProductOfArrayExceptSelf.java) |
| 88 | 240 | SearchA2DMatrixII | 🟡 Medium | Algorithms | $O(M + N)$ | $O(1)$ | [`LC0240_SearchA2DMatrixII.java`](./LC0240_SearchA2DMatrixII.java) |
| 89 | 300 | LongestIncreasingSubsequence | 🟡 Medium | Algorithms | $O(N log N)$ | $O(N)$ | [`LC0300_LongestIncreasingSubsequence.java`](./LC0300_LongestIncreasingSubsequence.java) |
| 90 | 322 | CoinChange | 🟡 Medium | Algorithms | $O(Amount * Coins.length)$ | $O(Amount)$ | [`LC0322_CoinChange.java`](./LC0322_CoinChange.java) |
| 91 | 347 | TopKFrequentElements | 🟡 Medium | Algorithms | $O(N log K)$ | $O(N + K)$ | [`LC0347_TopKFrequentElements.java`](./LC0347_TopKFrequentElements.java) |
| 92 | 373 | FindKPairsWithSmallestSums | 🟡 Medium | Algorithms | $O(K log(min(N, K)$)$)$ | $O(min(N, K)$)$ | [`LC0373_FindKPairsWithSmallestSums.java`](./LC0373_FindKPairsWithSmallestSums.java) |
| 93 | 416 | PartitionEqualSubsetSum | 🟡 Medium | Algorithms | $O(N * Target)$ | $O(Target)$ | [`LC0416_PartitionEqualSubsetSum.java`](./LC0416_PartitionEqualSubsetSum.java) |
| 94 | 424 | LongestRepeatingCharacterReplacement | 🟡 Medium | Algorithms | $O(N)$ | $O(1)$ (26 uppercase English letters)$ | [`LC0424_LongestRepeatingCharacterReplacement.java`](./LC0424_LongestRepeatingCharacterReplacement.java) |
| 95 | 435 | NonOverlappingIntervals | 🟡 Medium | Algorithms | $O(N log N)$ | $O(1)$ | [`LC0435_NonOverlappingIntervals.java`](./LC0435_NonOverlappingIntervals.java) |

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
