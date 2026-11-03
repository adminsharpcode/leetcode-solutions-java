/**
 * LeetCode 240: Search a 2D Matrix II
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
 *
 * Approach: Top-Right Corner Pointer Search (Binary Search Tree Elimination)
 * Time Complexity: O(M + N)
 * Space Complexity: O(1)
 */
public class LC0240_SearchA2DMatrixII {

    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int row = 0;
        int col = matrix[0].length - 1;

        while (row < matrix.length && col >= 0) {
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] > target) {
                col--;
            } else {
                row++;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        LC0240_SearchA2DMatrixII solver = new LC0240_SearchA2DMatrixII();
        int[][] matrix = {
            {1, 4, 7, 11, 15},
            {2, 5, 8, 12, 19},
            {3, 6, 9, 16, 22},
            {10, 13, 14, 17, 24},
            {18, 21, 23, 26, 30}
        };
        System.out.println("Search 5: " + solver.searchMatrix(matrix, 5));   // Expected: true
        System.out.println("Search 20: " + solver.searchMatrix(matrix, 20)); // Expected: false
    }
}
