import java.util.ArrayList;
import java.util.List;

/**
 * LeetCode 54: Spiral Matrix
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/spiral-matrix/
 *
 * Approach: Boundary Simulation (4 pointers)
 * Time Complexity: O(M * N)
 * Space Complexity: O(1)
 */
public class LC0054_SpiralMatrix {

    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return result;
        }

        int top = 0;
        int bottom = matrix.length - 1;
        int left = 0;
        int right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            // Traverse from left to right across top boundary
            for (int col = left; col <= right; col++) {
                result.add(matrix[top][col]);
            }
            top++;

            // Traverse downwards along right boundary
            for (int row = top; row <= bottom; row++) {
                result.add(matrix[row][right]);
            }
            right--;

            // Check if horizontal traversal remains
            if (top <= bottom) {
                for (int col = right; col >= left; col--) {
                    result.add(matrix[bottom][col]);
                }
                bottom--;
            }

            // Check if vertical traversal remains
            if (left <= right) {
                for (int row = bottom; row >= top; row--) {
                    result.add(matrix[row][left]);
                }
                left++;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        LC0054_SpiralMatrix solver = new LC0054_SpiralMatrix();
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        List<Integer> res = solver.spiralOrder(matrix);
        System.out.println("Spiral Order: " + res); // Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    }
}
