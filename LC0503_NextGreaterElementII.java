import java.util.*;

/**
 * Problem: 503. Next Greater Element II
 * Difficulty: Medium
 * Category: Array, Stack, Monotonic Stack
 *
 * Algorithm:
 * Circular array: simulate 2 * N iterations using index modulo n.
 * Monotonic decreasing index stack resolves next greater circular element.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0503_NextGreaterElementII {

    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        Arrays.fill(res, -1);
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < 2 * n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i % n]) {
                res[stack.pop()] = nums[i % n];
            }
            if (i < n) stack.push(i);
        }
        return res;
    }

    public static void main(String[] args) {
        LC0503_NextGreaterElementII sol = new LC0503_NextGreaterElementII();
        System.out.println(Arrays.toString(sol.nextGreaterElements(new int[]{1, 2, 1}))); // [2, -1, 2]
    }
}
