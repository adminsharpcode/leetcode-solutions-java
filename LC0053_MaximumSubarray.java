/**
 * LeetCode 53: Maximum Subarray
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/maximum-subarray/
 *
 * Approach: Kadane's Algorithm
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0053_MaximumSubarray {

    public int maxSubArray(int[] nums) {
        int maxSoFar = nums[0];
        int currentMax = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currentMax = Math.max(nums[i], currentMax + nums[i]);
            maxSoFar = Math.max(maxSoFar, currentMax);
        }

        return maxSoFar;
    }

    public static void main(String[] args) {
        LC0053_MaximumSubarray solver = new LC0053_MaximumSubarray();
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println("Max Subarray Sum: " + solver.maxSubArray(nums)); // Expected: 6 [4,-1,2,1]
    }
}
