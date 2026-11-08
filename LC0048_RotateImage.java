import java.util.Arrays;

/**
 * LeetCode 48: Rotate Image
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/rotate-image/
 *
 * Approach: Transpose Matrix + Reflect (Reverse Rows)
 * Time Complexity: O(N^2)
 * Space Complexity: O(1) in-place
 */
public class LC0048_RotateImage {

    public void rotate(int[][] matrix) {
        int n = matrix.length;

        // Step 1: Transpose matrix along main diagonal
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // Step 2: Reverse each row horizontally
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - 1 - j];
                matrix[i][n - 1 - j] = temp;
            }
        }
    }

    public static void main(String[] args) {
        LC0048_RotateImage solver = new LC0048_RotateImage();
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        solver.rotate(matrix);
        System.out.println("Rotated matrix: " + Arrays.deepToString(matrix));
        // Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    }
}
