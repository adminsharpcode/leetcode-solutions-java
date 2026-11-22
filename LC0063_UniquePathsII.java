/**
 * Problem: 63. Unique Paths II
 * Difficulty: Medium
 * Category: Array, Dynamic Programming, Matrix
 *
 * Algorithm:
 * 1D DP array: dp[j] represents number of paths to cell (i, j).
 * If obstacle at (i, j), dp[j] = 0. Otherwise dp[j] += dp[j - 1].
 *
 * Time Complexity: O(M * N)
 * Space Complexity: O(N)
 */
public class LC0063_UniquePathsII {

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid == null || obstacleGrid[0][0] == 1) return 0;

        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[] dp = new int[n];
        dp[0] = 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0;
                } else if (j > 0) {
                    dp[j] += dp[j - 1];
                }
            }
        }
        return dp[n - 1];
    }

    public static void main(String[] args) {
        LC0063_UniquePathsII solver = new LC0063_UniquePathsII();
        int[][] grid = {
            {0, 0, 0},
            {0, 1, 0},
            {0, 0, 0}
        };
        assert solver.uniquePathsWithObstacles(grid) == 2;
        System.out.println("LC0063_UniquePathsII passed all tests!");
    }
}
