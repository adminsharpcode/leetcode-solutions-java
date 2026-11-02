/**
 * LeetCode 79: Word Search
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/word-search/
 *
 * Approach: DFS Backtracking with in-place character masking
 * Time Complexity: O(M * N * 3^L) where L is length of word
 * Space Complexity: O(L) recursion stack depth
 */
public class LC0079_WordSearch {

    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word.charAt(0) && dfs(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int r, int c, int index) {
        if (index == word.length()) {
            return true;
        }

        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(index)) {
            return false;
        }

        char temp = board[r][c];
        board[r][c] = '#'; // Mark as visited in-place

        boolean found = dfs(board, word, r + 1, c, index + 1)
                     || dfs(board, word, r - 1, c, index + 1)
                     || dfs(board, word, r, c + 1, index + 1)
                     || dfs(board, word, r, c - 1, index + 1);

        board[r][c] = temp; // Backtrack
        return found;
    }

    public static void main(String[] args) {
        LC0079_WordSearch solver = new LC0079_WordSearch();

        char[][] board = {
            {'A', 'B', 'C', 'E'},
            {'S', 'F', 'C', 'S'},
            {'A', 'D', 'E', 'E'}
        };

        System.out.println("Exists ABCCED: " + solver.exist(board, "ABCCED")); // Expected: true
        System.out.println("Exists SEE: " + solver.exist(board, "SEE"));       // Expected: true
        System.out.println("Exists ABCB: " + solver.exist(board, "ABCB"));     // Expected: false
    }
}
