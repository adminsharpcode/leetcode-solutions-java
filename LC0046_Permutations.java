import java.util.ArrayList;
import java.util.List;

/**
 * LeetCode 46: Permutations
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/permutations/
 *
 * Approach: Backtracking
 * Time Complexity: O(N * N!)
 * Space Complexity: O(N) recursion stack
 */
public class LC0046_Permutations {

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, new ArrayList<>(), new boolean[nums.length], result);
        return result;
    }

    private void backtrack(int[] nums, List<Integer> current, boolean[] used, List<List<Integer>> result) {
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            current.add(nums[i]);
            backtrack(nums, current, used, result);
            current.remove(current.size() - 1);
            used[i] = false;
        }
    }

    public static void main(String[] args) {
        LC0046_Permutations solver = new LC0046_Permutations();
        int[] nums = {1, 2, 3};
        System.out.println("Permutations: " + solver.permute(nums)); // Expected: 6 permutations
    }
}
