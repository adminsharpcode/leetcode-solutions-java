/**
 * LeetCode 55: Jump Game
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/jump-game/
 *
 * Approach: Greedy furthest reachable position tracking
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0055_JumpGame {

    public boolean canJump(int[] nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) {
                return false;
            }
            maxReach = Math.max(maxReach, i + nums[i]);
            if (maxReach >= nums.length - 1) {
                return true;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        LC0055_JumpGame solver = new LC0055_JumpGame();

        int[] nums1 = {2, 3, 1, 1, 4};
        System.out.println("Test 1: " + solver.canJump(nums1)); // Expected: true

        int[] nums2 = {3, 2, 1, 0, 4};
        System.out.println("Test 2: " + solver.canJump(nums2)); // Expected: false
    }
}
