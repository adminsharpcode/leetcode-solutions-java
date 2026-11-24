import java.util.*;
public class LC0085_MaximalRectangle {
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0) return 0;
        int n = matrix[0].length, max = 0;
        int[] heights = new int[n];
        for (char[] row : matrix) {
            for (int j = 0; j < n; j++)
                heights[j] = row[j] == '1' ? heights[j] + 1 : 0;
            max = Math.max(max, largestRect(heights));
        }
        return max;
    }
    private int largestRect(int[] h) {
        Deque<Integer> stack = new ArrayDeque<>();
        int max = 0;
        for (int i = 0; i <= h.length; i++) {
            int cur = (i == h.length) ? 0 : h[i];
            while (!stack.isEmpty() && h[stack.peek()] > cur) {
                int height = h[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                max = Math.max(max, height * width);
            }
            stack.push(i);
        }
        return max;
    }
    public static void main(String[] args) {
        LC0085_MaximalRectangle sol = new LC0085_MaximalRectangle();
        char[][] m = {{'1','0','1','0','0'},{'1','0','1','1','1'},{'1','1','1','1','1'},{'1','0','0','1','0'}};
        System.out.println(sol.maximalRectangle(m)); // 6
    }
}
