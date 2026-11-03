import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * LeetCode 39: Combination Sum
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/combination-sum/
 *
 * Approach: Backtracking with unlimited element reuse
 * Time Complexity: O(2^(Target / Min_Candidate))
 * Space Complexity: O(Target / Min_Candidate)
 */
public class LC0039_CombinationSum {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
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
                break; // Candidates are sorted; remaining items exceed target
            }

            current.add(candidates[i]);
            backtrack(candidates, remain - candidates[i], i, current, result);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        LC0039_CombinationSum solver = new LC0039_CombinationSum();
        int[] candidates = {2, 3, 6, 7};
        System.out.println("Target 7: " + solver.combinationSum(candidates, 7));
        // Expected: [[2, 2, 3], [7]]
    }
}
