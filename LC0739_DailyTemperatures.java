import java.util.*;

/**
 * Problem: 739. Daily Temperatures
 * Difficulty: Medium
 * Category: Array, Stack, Monotonic Stack
 *
 * Algorithm:
 * Monotonic decreasing stack storing indices.
 * When current temp > stack.peek() temp, pop and distance is cur_idx - popped_idx.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0739_DailyTemperatures {

    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] res = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
                int prev = stack.pop();
                res[prev] = i - prev;
            }
            stack.push(i);
        }
        return res;
    }

    public static void main(String[] args) {
        LC0739_DailyTemperatures sol = new LC0739_DailyTemperatures();
        int[] temps = {73, 74, 75, 71, 69, 72, 76, 73};
        System.out.println(Arrays.toString(sol.dailyTemperatures(temps))); // [1, 1, 4, 2, 1, 1, 0, 0]
    }
}
