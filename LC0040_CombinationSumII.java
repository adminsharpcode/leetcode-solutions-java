import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * LeetCode 40: Combination Sum II
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/combination-sum-ii/
 *
 * Approach: Backtracking with duplicate skipping
 * Time Complexity: O(2^N)
 * Space Complexity: O(N)
 */
public class LC0040_CombinationSumII {

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] candidates, int remain, int start, List<Integer> current, List<List<Integer>> result) {
        if (remain == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remain) {
                break;
            }
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue; // Skip duplicate combinations at same depth
            }

            current.add(candidates[i]);
            backtrack(candidates, remain - candidates[i], i + 1, current, result);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        LC0040_CombinationSumII solver = new LC0040_CombinationSumII();
        int[] candidates = {10, 1, 2, 7, 6, 1, 5};
        System.out.println("Target 8: " + solver.combinationSum2(candidates, 8));
        // Expected: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    }
}
