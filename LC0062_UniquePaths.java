import java.util.Arrays;

/**
 * LeetCode 62: Unique Paths
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/unique-paths/
 *
 * Approach: 1D Space-Optimized Dynamic Programming
 * Time Complexity: O(M * N)
 * Space Complexity: O(N)
 */
public class LC0062_UniquePaths {

    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j - 1];
            }
        }

        return dp[n - 1];
    }

    public static void main(String[] args) {
        LC0062_UniquePaths solver = new LC0062_UniquePaths();

        System.out.println("Paths (3x7): " + solver.uniquePaths(3, 7)); // Expected: 28
        System.out.println("Paths (3x2): " + solver.uniquePaths(3, 2)); // Expected: 3
    }
}
