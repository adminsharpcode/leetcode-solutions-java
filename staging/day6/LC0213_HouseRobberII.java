/**
 * Problem: 213. House Robber II
 * Difficulty: Medium
 * Category: Array, Dynamic Programming
 *
 * Algorithm:
 * Since houses are in a circle (house 0 is adjacent to house n-1), solve two subproblems:
 * 1. Max rob from house 0 to n-2.
 * 2. Max rob from house 1 to n-1.
 * Return max of both.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0213_HouseRobberII {

    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);

        return Math.max(robLinear(nums, 0, nums.length - 2),
                        robLinear(nums, 1, nums.length - 1));
    }

    private int robLinear(int[] nums, int start, int end) {
        int prev1 = 0;
        int prev2 = 0;

        for (int i = start; i <= end; i++) {
            int temp = prev1;
            prev1 = Math.max(prev2 + nums[i], prev1);
            prev2 = temp;
        }
        return prev1;
    }

    public static void main(String[] args) {
        LC0213_HouseRobberII solver = new LC0213_HouseRobberII();
        int[] nums = {2, 3, 2};
        assert solver.rob(nums) == 3;
        int[] nums2 = {1, 2, 3, 1};
        assert solver.rob(nums2) == 4;
        System.out.println("LC0213_HouseRobberII passed all tests!");
    }
}
