import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;

/**
 * LeetCode 1: Two Sum
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/two-sum/
 *
 * Approach: One-pass Hash Map
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0001_TwoSum {

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        LC0001_TwoSum solver = new LC0001_TwoSum();
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] res = solver.twoSum(nums, target);
        System.out.println("Result: " + Arrays.toString(res)); // Expected: [0, 1]
    }
}
