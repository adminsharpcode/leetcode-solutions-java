/**
 * LeetCode 416: Partition Equal Subset Sum
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/partition-equal-subset-sum/
 *
 * Approach: 0/1 Knapsack Dynamic Programming with 1D Bitwise/Array Space Optimization
 * Time Complexity: O(N * Target)
 * Space Complexity: O(Target)
 */
public class LC0416_PartitionEqualSubsetSum {

    public boolean canPartition(int[] nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        // An odd total sum can never be divided into two equal integers
        if (totalSum % 2 != 0) {
            return false;
        }

        int target = totalSum / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;

        for (int num : nums) {
            for (int j = target; j >= num; j--) {
                dp[j] = dp[j] || dp[j - num];
            }
        }

        return dp[target];
    }

    public static void main(String[] args) {
        LC0416_PartitionEqualSubsetSum solver = new LC0416_PartitionEqualSubsetSum();
        int[] nums = {1, 5, 11, 5};
        System.out.println("Can partition: " + solver.canPartition(nums)); // Expected: true ([1, 5, 5] and [11])
    }
}
