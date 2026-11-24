/**
 * Problem: 130. Surrounded Regions
 * Difficulty: Medium
 * Category: Depth-First Search, Breadth-First Search, Matrix
 *
 * Algorithm:
 * Boundary DFS traversal: all 'O' cells connected to border cannot be captured.
 * Traverse from all border cells, mark visited 'O' as temporary 'S'.
 * Flip all remaining 'O' to 'X' (captured), flip 'S' back to 'O'.
 *
 * Time Complexity: O(M * N)
 * Space Complexity: O(M * N) recursion stack
 */
public class LC0130_SurroundedRegions {

    public void solve(char[][] board) {
        if (board == null || board.length == 0) return;
        int m = board.length, n = board[0].length;

        for (int i = 0; i < m; i++) {
            dfs(board, i, 0, m, n);
            dfs(board, i, n - 1, m, n);
        }
        for (int j = 0; j < n; j++) {
            dfs(board, 0, j, m, n);
            dfs(board, m - 1, j, m, n);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                else if (board[i][j] == 'S') board[i][j] = 'O';
            }
        }
    }

    private void dfs(char[][] b, int r, int c, int m, int n) {
        if (r < 0 || r >= m || c < 0 || c >= n || b[r][c] != 'O') return;
        b[r][c] = 'S';
        dfs(b, r + 1, c, m, n);
        dfs(b, r - 1, c, m, n);
        dfs(b, r, c + 1, m, n);
        dfs(b, r, c - 1, m, n);
    }

    public static void main(String[] args) {
        LC0130_SurroundedRegions sol = new LC0130_SurroundedRegions();
        char[][] board = {
            {'X','X','X','X'},
            {'X','O','O','X'},
            {'X','X','O','X'},
            {'X','O','X','X'}
        };
        sol.solve(board);
        for (char[] row : board) System.out.println(new String(row));
    }
}
