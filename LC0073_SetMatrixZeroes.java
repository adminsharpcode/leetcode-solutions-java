import java.util.Arrays;

/**
 * LeetCode 73: Set Matrix Zeroes
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/set-matrix-zeroes/
 *
 * Approach: In-Place Marking using First Row and First Column as Flags
 * Time Complexity: O(M * N)
 * Space Complexity: O(1)
 */
public class LC0073_SetMatrixZeroes {

    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        boolean firstColZero = false;

        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                firstColZero = true;
            }
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // Zero out cells based on top and left boundary flags
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // Handle first row
        if (matrix[0][0] == 0) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }

        // Handle first column
        if (firstColZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }

    public static void main(String[] args) {
        LC0073_SetMatrixZeroes solver = new LC0073_SetMatrixZeroes();
        int[][] matrix = {
            {1, 1, 1},
            {1, 0, 1},
            {1, 1, 1}
        };
        solver.setZeroes(matrix);
        System.out.println("Result: " + Arrays.deepToString(matrix));
        // Expected: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    }
}
