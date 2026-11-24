import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Problem: 90. Subsets II
 * Difficulty: Medium
 * Category: Array, Backtracking, Bit Manipulation
 *
 * Algorithm:
 * Sort input array to group duplicate values together.
 * In backtracking loop, if nums[i] == nums[i - 1] and i > start, skip to prevent duplicates.
 *
 * Time Complexity: O(N * 2^N)
 * Space Complexity: O(N) recursion stack
 */
public class LC0090_SubsetsII {

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(0, nums, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int start, int[] nums, List<Integer> current, List<List<Integer>> result) {
        result.add(new ArrayList<>(current));

        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i - 1]) continue;
            current.add(nums[i]);
            backtrack(i + 1, nums, current, result);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        LC0090_SubsetsII solver = new LC0090_SubsetsII();
        int[] nums = {1, 2, 2};
        List<List<Integer>> res = solver.subsetsWithDup(nums);
        assert res.size() == 6; // [], [1], [1,2], [1,2,2], [2], [2,2]
        System.out.println("LC0090_SubsetsII passed all tests!");
    }
}
