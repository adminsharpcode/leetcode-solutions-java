import java.util.*;

/**
 * Problem: 239. Sliding Window Maximum
 * Difficulty: Hard
 * Category: Array, Queue, Sliding Window, Heap, Monotonic Queue
 *
 * Algorithm:
 * Monotonic decreasing deque storing indices.
 * Remove indices falling out of window [i - k + 1, i].
 * Maintain strictly decreasing order in deque; first element is always window max.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(k)
 */
public class LC0239_SlidingWindowMaximum {

    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] res = new int[n - k + 1];
        Deque<Integer> dq = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            while (!dq.isEmpty() && dq.peekFirst() < i - k + 1) dq.pollFirst();
            while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i]) dq.pollLast();

            dq.offerLast(i);
            if (i >= k - 1) {
                res[i - k + 1] = nums[dq.peekFirst()];
            }
        }
        return res;
    }

    public static void main(String[] args) {
        LC0239_SlidingWindowMaximum sol = new LC0239_SlidingWindowMaximum();
        int[] nums = {1, 3, -1, -3, 5, 3, 6, 7};
        System.out.println(Arrays.toString(sol.maxSlidingWindow(nums, 3))); // [3,3,5,5,6,7]
    }
}
