import os

REPO_ROOT = r"E:\LeetCode-Solutions-Java"

DAY_MAP = {
    1: [
        ("LC0016_3SumClosest.java", "LC0016 3Sum Closest"),
        ("LC0026_RemoveDuplicatesFromSortedArray.java", "LC0026 Remove Duplicates from Sorted Array"),
        ("LC0075_SortColors.java", "LC0075 Sort Colors"),
        ("LC0128_LongestConsecutiveSequence.java", "LC0128 Longest Consecutive Sequence"),
        ("LC0167_TwoSumIIInputArrayIsSorted.java", "LC0167 Two Sum II - Input Array Is Sorted"),
        ("LC0189_RotateArray.java", "LC0189 Rotate Array"),
    ],
    2: [
        ("LC0024_SwapNodesInPairs.java", "LC0024 Swap Nodes in Pairs"),
        ("LC0061_RotateList.java", "LC0061 Rotate List"),
        ("LC0141_LinkedListCycle.java", "LC0141 Linked List Cycle"),
        ("LC0142_LinkedListCycleII.java", "LC0142 Linked List Cycle II"),
        ("LC0143_ReorderList.java", "LC0143 Reorder List"),
        ("LC0234_PalindromeLinkedList.java", "LC0234 Palindrome Linked List"),
    ],
    3: [
        ("LC0034_FindFirstAndLastPositionOfElementInSortedArray.java", "LC0034 Find First and Last Position of Element in Sorted Array"),
        ("LC0035_SearchInsertPosition.java", "LC0035 Search Insert Position"),
        ("LC0048_RotateImage.java", "LC0048 Rotate Image"),
        ("LC0073_SetMatrixZeroes.java", "LC0073 Set Matrix Zeroes"),
        ("LC0074_SearchA2DMatrix.java", "LC0074 Search a 2D Matrix"),
        ("LC0240_SearchA2DMatrixII.java", "LC0240 Search a 2D Matrix II"),
    ],
    4: [
        ("LC0150_EvaluateReversePolishNotation.java", "LC0150 Evaluate Reverse Polish Notation"),
        ("LC0155_MinStack.java", "LC0155 Min Stack"),
        ("LC0225_ImplementStackUsingQueues.java", "LC0225 Implement Stack using Queues"),
        ("LC0232_ImplementQueueUsingStacks.java", "LC0232 Implement Queue using Stacks"),
        ("LC0347_TopKFrequentElements.java", "LC0347 Top K Frequent Elements"),
        ("LC0373_FindKPairsWithSmallestSums.java", "LC0373 Find K Pairs with Smallest Sums"),
    ],
    5: [
        ("LC0100_SameTree.java", "LC0100 Same Tree"),
        ("LC0101_SymmetricTree.java", "LC0101 Symmetric Tree"),
        ("LC0103_BinaryTreeZigzagLevelOrderTraversal.java", "LC0103 Binary Tree Zigzag Level Order Traversal"),
        ("LC0110_BalancedBinaryTree.java", "LC0110 Balanced Binary Tree"),
        ("LC0230_KthSmallestElementInABST.java", "LC0230 Kth Smallest Element in a BST"),
        ("LC0236_LowestCommonAncestorOfABinaryTree.java", "LC0236 Lowest Common Ancestor of a Binary Tree"),
    ],
    6: [
        ("LC0017_LetterCombinationsOfAPhoneNumber.java", "LC0017 Letter Combinations of a Phone Number"),
        ("LC0039_CombinationSum.java", "LC0039 Combination Sum"),
        ("LC0040_CombinationSumII.java", "LC0040 Combination Sum II"),
        ("LC0064_MinimumPathSum.java", "LC0064 Minimum Path Sum"),
        ("LC0091_DecodeWays.java", "LC0091 Decode Ways"),
        ("LC0120_Triangle.java", "LC0120 Triangle"),
    ],
    7: [
        ("LC0072_EditDistance.java", "LC0072 Edit Distance"),
        ("LC0210_CourseScheduleII.java", "LC0210 Course Schedule II"),
        ("LC0322_CoinChange.java", "LC0322 Coin Change"),
        ("LC0416_PartitionEqualSubsetSum.java", "LC0416 Partition Equal Subset Sum"),
        ("LC0424_LongestRepeatingCharacterReplacement.java", "LC0424 Longest Repeating Character Replacement"),
        ("LC0435_NonOverlappingIntervals.java", "LC0435 Non-overlapping Intervals"),
    ]
}

def generate_day_script(day_num, items):
    lines = [
        "#!/bin/bash",
        "# =================================================================",
        f"# Day {day_num} LeetCode Submissions (6 Sequential Java Contributions)",
        "# Compatible with Termux (Android) and standard Linux/macOS bash",
        "# =================================================================",
        "set -e",
        "",
        'SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"',
        'cd "$SCRIPT_DIR"',
        "",
        'echo "================================================================"',
        f'echo "🚀 Executing Day {day_num} Submissions (6 Problems in Java)"',
        'echo "================================================================"',
        "",
        '# Ensure we have git configured',
        'if ! command -v git &> /dev/null; then',
        '    echo "[-] Git is not installed. In Termux, run: pkg install git"',
        '    exit 1',
        'fi',
        "",
        '# Pull latest commits cleanly',
        'echo "[*] Syncing with remote repository..."',
        'git pull --rebase origin main || true',
        "",
    ]

    for idx, (filename, title) in enumerate(items, 1):
        lines.append(f'# [{idx}/6] {filename}')
        lines.append(f'echo "[*] Committing [{idx}/6]: {title}..."')
        lines.append(f'cp "staging/day{day_num}/{filename}" "./{filename}"')
        lines.append(f'git add "{filename}"')
        lines.append(f'git commit -m "feat(leetcode): solve {title} in Java"')
        lines.append('sleep 2')
        lines.append('')

    lines.extend([
        'echo "[*] Pushing all 6 commits to GitHub..."',
        'git push origin main',
        "",
        'echo ""',
        'echo "================================================================"',
        f'echo "✅ Day {day_num} COMPLETE: 6 new Java solutions pushed to GitHub!"',
        'echo "================================================================"',
    ])

    # Join with Unix LF
    return "\n".join(lines) + "\n"

def main():
    for day_num, items in DAY_MAP.items():
        script_content = generate_day_script(day_num, items)
        script_path = os.path.join(REPO_ROOT, f"day{day_num}.sh")
        with open(script_path, "wb") as f:
            f.write(script_content.encode("utf-8"))
        print(f"Generated day{day_num}.sh")

    # Generate master runner: run_day.sh
    master_lines = [
        "#!/bin/bash",
        "# Master Daily Runner for Termux (Android) / Linux",
        "# Usage:",
        "#   ./run_day.sh 1   (runs Day 1)",
        "#   ./run_day.sh 2   (runs Day 2)",
        "#   ...",
        "#   ./run_day.sh     (prompts for Day 1-7)",
        "set -e",
        "",
        'SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"',
        'cd "$SCRIPT_DIR"',
        "",
        'DAY="$1"',
        'if [ -z "$DAY" ]; then',
        '    echo "=================================================="',
        '    echo "⚡ LeetCode Daily Submissions Runner (Android/Termux) ⚡"',
        '    echo "=================================================="',
        '    echo "Which day would you like to submit? (1 - 7): "',
        '    read -r DAY',
        'fi',
        "",
        'if [ ! -f "day${DAY}.sh" ]; then',
        '    echo "[-] Error: Invalid day \\"$DAY\\". Please choose between 1 and 7."',
        '    exit 1',
        'fi',
        "",
        'chmod +x "day${DAY}.sh"',
        'bash "day${DAY}.sh"',
    ]
    master_content = "\n".join(master_lines) + "\n"
    with open(os.path.join(REPO_ROOT, "run_day.sh"), "wb") as f:
        f.write(master_content.encode("utf-8"))
    print("Generated run_day.sh")

if __name__ == "__main__":
    main()
