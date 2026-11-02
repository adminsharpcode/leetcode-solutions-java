import java.util.ArrayList;
import java.util.List;

/**
 * LeetCode 78: Subsets
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/subsets/
 *
 * Approach: Backtracking Power Set Construction
 * Time Complexity: O(N * 2^N)
 * Space Complexity: O(N)
 */
public class LC0078_Subsets {

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(0, nums, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int start, int[] nums, List<Integer> current, List<List<Integer>> result) {
        result.add(new ArrayList<>(current));

        for (int i = start; i < nums.length; i++) {
            current.add(nums[i]);
            backtrack(i + 1, nums, current, result);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        LC0078_Subsets solver = new LC0078_Subsets();
        int[] nums = {1, 2, 3};
        List<List<Integer>> res = solver.subsets(nums);
        System.out.println("Subsets: " + res);
        // Expected: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    }
}
