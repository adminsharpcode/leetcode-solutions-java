import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * LeetCode 15: 3Sum
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/3sum/
 *
 * Approach: Sorting + Two Pointers with Duplicate Avoidance
 * Time Complexity: O(N^2)
 * Space Complexity: O(1) auxiliary (ignoring output)
 */
public class LC0015_ThreeSum {

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // Skip duplicate first numbers
            if (nums[i] > 0) break; // If smallest is positive, sum cannot be zero

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        LC0015_ThreeSum solver = new LC0015_ThreeSum();
        int[] nums = {-1, 0, 1, 2, -1, -4};
        System.out.println("3Sum: " + solver.threeSum(nums)); // Expected: [[-1, -1, 2], [-1, 0, 1]]
    }
}
