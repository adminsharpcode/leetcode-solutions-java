/**
 * LeetCode 64: Minimum Path Sum
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/minimum-path-sum/
 *
 * Approach: In-Place 2D Dynamic Programming
 * Time Complexity: O(M * N)
 * Space Complexity: O(1) in-place
 */
public class LC0064_MinimumPathSum {

    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        // Initialize first row
        for (int j = 1; j < n; j++) {
            grid[0][j] += grid[0][j - 1];
        }

        // Initialize first column
        for (int i = 1; i < m; i++) {
            grid[i][0] += grid[i - 1][0];
        }

        // Fill remaining table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
            }
        }

        return grid[m - 1][n - 1];
    }

    public static void main(String[] args) {
        LC0064_MinimumPathSum solver = new LC0064_MinimumPathSum();
        int[][] grid = {
            {1, 3, 1},
            {1, 5, 1},
            {4, 2, 1}
        };
        System.out.println("Min path sum: " + solver.minPathSum(grid)); // Expected: 7 (1 -> 3 -> 1 -> 1 -> 1)
    }
}
