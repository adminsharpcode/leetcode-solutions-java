/**
 * LeetCode 200: Number of Islands
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/number-of-islands/
 *
 * Approach: Depth-First Search (DFS) Grid Traversal (Flood Fill)
 * Time Complexity: O(M * N)
 * Space Complexity: O(M * N) worst-case recursion stack
 */
public class LC0200_NumberOfIslands {

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int islands = 0;

        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == '1') {
                    islands++;
                    dfs(grid, r, c);
                }
            }
        }

        return islands;
    }

    private void dfs(char[][] grid, int r, int c) {
        if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] != '1') {
            return;
        }
        grid[r][c] = '0'; // Sink island
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }

    public static void main(String[] args) {
        LC0200_NumberOfIslands solver = new LC0200_NumberOfIslands();
        char[][] grid = {
            {'1', '1', '0', '0', '0'},
            {'1', '1', '0', '0', '0'},
            {'0', '0', '1', '0', '0'},
            {'0', '0', '0', '1', '1'}
        };
        System.out.println("Number of Islands: " + solver.numIslands(grid)); // Expected: 3
    }
}
