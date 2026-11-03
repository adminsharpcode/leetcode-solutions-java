import java.util.Arrays;

/**
 * LeetCode 16: 3Sum Closest
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/3sum-closest/
 *
 * Approach: Sorting + Two Pointers
 * Time Complexity: O(N^2)
 * Space Complexity: O(1)
 */
public class LC0016_3SumClosest {

    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closestSum = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int currentSum = nums[i] + nums[left] + nums[right];

                if (Math.abs(target - currentSum) < Math.abs(target - closestSum)) {
                    closestSum = currentSum;
                }

                if (currentSum < target) {
                    left++;
                } else if (currentSum > target) {
                    right--;
                } else {
                    return target;
                }
            }
        }
        return closestSum;
    }

    public static void main(String[] args) {
        LC0016_3SumClosest solver = new LC0016_3SumClosest();
        int[] nums = {-1, 2, 1, -4};
        int target = 1;
        System.out.println("Result: " + solver.threeSumClosest(nums, target)); // Expected: 2
    }
}
