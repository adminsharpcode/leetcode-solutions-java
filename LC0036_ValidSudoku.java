import java.util.HashSet;
import java.util.Set;

/**
 * Problem: 36. Valid Sudoku
 * Difficulty: Medium
 * Category: Array, Hash Table, Matrix
 *
 * Algorithm:
 * Validate rows, columns, and 3x3 sub-boxes:
 * Encode entries as strings:
 *   - "val in row r"
 *   - "val in col c"
 *   - "val in box (r/3)-(c/3)"
 * If an entry already exists in the set, the board is invalid.
 * Alternatively, bitmask arrays for O(1) space.
 *
 * Time Complexity: O(1) fixed 9x9 board = 81 cells
 * Space Complexity: O(1) fixed 9x9 board
 */
public class LC0036_ValidSudoku {

    public boolean isValidSudoku(char[][] board) {
        int[] rows = new int[9];
        int[] cols = new int[9];
        int[] boxes = new int[9];

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char ch = board[r][c];
                if (ch == '.') continue;

                int digit = ch - '1'; // 0 to 8
                int mask = 1 << digit;

                int boxIdx = (r / 3) * 3 + (c / 3);

                // Check if already seen in row, col, or 3x3 box
                if ((rows[r] & mask) != 0 || (cols[c] & mask) != 0 || (boxes[boxIdx] & mask) != 0) {
                    return false;
                }

                rows[r] |= mask;
                cols[c] |= mask;
                boxes[boxIdx] |= mask;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        LC0036_ValidSudoku solver = new LC0036_ValidSudoku();
        char[][] board = {
            {'5','3','.','.','7','.','.','.','.'},
            {'6','.','.','1','9','5','.','.','.'},
            {'.','9','8','.','.','.','.','6','.'},
            {'8','.','.','.','6','.','.','.','3'},
            {'4','.','.','8','.','3','.','.','1'},
            {'7','.','.','.','2','.','.','.','6'},
            {'.','6','.','.','.','.','2','8','.'},
            {'.','.','.','4','1','9','.','.','5'},
            {'.','.','.','.','8','.','.','7','9'}
        };
        assert solver.isValidSudoku(board) == true;
        System.out.println("LC0036_ValidSudoku passed all tests!");
    }
}
