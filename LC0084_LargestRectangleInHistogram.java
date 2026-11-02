import java.util.ArrayDeque;
import java.util.Deque;

/**
 * LeetCode 84: Largest Rectangle in Histogram
 * Difficulty: Hard
 * Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
 *
 * Approach: Monotonic Increasing Stack
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0084_LargestRectangleInHistogram {

    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        Deque<Integer> stack = new ArrayDeque<>();
        int maxArea = 0;

        for (int i = 0; i <= n; i++) {
            int currentHeight = (i == n) ? 0 : heights[i];

            while (!stack.isEmpty() && currentHeight < heights[stack.peek()]) {
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            stack.push(i);
        }

        return maxArea;
    }

    public static void main(String[] args) {
        LC0084_LargestRectangleInHistogram solver = new LC0084_LargestRectangleInHistogram();

        int[] heights1 = {2, 1, 5, 6, 2, 3};
        System.out.println("Max Area 1: " + solver.largestRectangleArea(heights1)); // Expected: 10

        int[] heights2 = {2, 4};
        System.out.println("Max Area 2: " + solver.largestRectangleArea(heights2)); // Expected: 4
    }
}
