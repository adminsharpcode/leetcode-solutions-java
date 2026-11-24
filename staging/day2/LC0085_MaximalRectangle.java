import java.util.*;

/**
 * Problem: 85. Maximal Rectangle
 * Difficulty: Hard
 * Category: Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
 *
 * Algorithm:
 * Maintain running histogram heights row by row.
 * For each row, calculate largest rectangle in histogram via Monotonic Stack in O(N).
 *
 * Time Complexity: O(M * N)
 * Space Complexity: O(N)
 */
public class LC0085_MaximalRectangle {

    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0) return 0;
        int cols = matrix[0].length;
        int[] heights = new int[cols];
        int maxArea = 0;

        for (char[] row : matrix) {
            for (int j = 0; j < cols; j++) {
                heights[j] = row[j] == '1' ? heights[j] + 1 : 0;
            }
            maxArea = Math.max(maxArea, largestHistogram(heights));
        }
        return maxArea;
    }

    private int largestHistogram(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int max = 0;
        for (int i = 0; i <= heights.length; i++) {
            int h = (i == heights.length) ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > h) {
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                max = Math.max(max, height * width);
            }
            stack.push(i);
        }
        return max;
    }

    public static void main(String[] args) {
        LC0085_MaximalRectangle sol = new LC0085_MaximalRectangle();
        char[][] mat = {
            {'1','0','1','0','0'},
            {'1','0','1','1','1'},
            {'1','1','1','1','1'},
            {'1','0','0','1','0'}
        };
        System.out.println("Maximal Rectangle: " + sol.maximalRectangle(mat)); // 6
    }
}
