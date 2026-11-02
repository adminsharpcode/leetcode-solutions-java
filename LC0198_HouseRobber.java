/**
 * LeetCode 198: House Robber
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/house-robber/
 *
 * Approach: 1D Dynamic Programming with Constant Space
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0198_HouseRobber {

    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];

        int prev2 = 0;
        int prev1 = 0;

        for (int num : nums) {
            int current = Math.max(prev1, prev2 + num);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }

    public static void main(String[] args) {
        LC0198_HouseRobber solver = new LC0198_HouseRobber();
        int[] nums = {2, 7, 9, 3, 1};
        System.out.println("Max robbed: " + solver.rob(nums)); // Expected: 12 (2 + 9 + 1)
    }
}
