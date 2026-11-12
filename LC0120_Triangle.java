import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * LeetCode 120: Triangle
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/triangle/
 *
 * Approach: Bottom-up 1D Dynamic Programming
 * Time Complexity: O(N^2)
 * Space Complexity: O(N)
 */
public class LC0120_Triangle {

    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[] dp = new int[n];

        // Seed DP table with the bottom row
        for (int j = 0; j < n; j++) {
            dp[j] = triangle.get(n - 1).get(j);
        }

        // Collapse upwards towards the apex
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                dp[j] = triangle.get(i).get(j) + Math.min(dp[j], dp[j + 1]);
            }
        }

        return dp[0];
    }

    public static void main(String[] args) {
        LC0120_Triangle solver = new LC0120_Triangle();
        List<List<Integer>> triangle = new ArrayList<>();
        triangle.add(Arrays.asList(2));
        triangle.add(Arrays.asList(3, 4));
        triangle.add(Arrays.asList(6, 5, 7));
        triangle.add(Arrays.asList(4, 1, 8, 3));

        System.out.println("Min total: " + solver.minimumTotal(triangle)); // Expected: 11 (2 + 3 + 5 + 1)
    }
}
