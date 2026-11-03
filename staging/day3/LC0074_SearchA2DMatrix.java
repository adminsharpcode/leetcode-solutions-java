/**
 * LeetCode 74: Search a 2D Matrix
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/search-a-2d-matrix/
 *
 * Approach: Virtual 1D Flattening + Binary Search
 * Time Complexity: O(log(M * N))
 * Space Complexity: O(1)
 */
public class LC0074_SearchA2DMatrix {

    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int m = matrix.length;
        int n = matrix[0].length;
        int left = 0;
        int right = m * n - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int midVal = matrix[mid / n][mid % n];

            if (midVal == target) {
                return true;
            } else if (midVal < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        LC0074_SearchA2DMatrix solver = new LC0074_SearchA2DMatrix();
        int[][] matrix = {
            {1, 3, 5, 7},
            {10, 11, 16, 20},
            {23, 30, 34, 60}
        };
        System.out.println("Search 3: " + solver.searchMatrix(matrix, 3));   // Expected: true
        System.out.println("Search 13: " + solver.searchMatrix(matrix, 13)); // Expected: false
    }
}
