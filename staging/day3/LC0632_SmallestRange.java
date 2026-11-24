import java.util.*;

/**
 * Problem: 632. Smallest Range Covering Elements from K Lists
 * Difficulty: Hard
 * Category: Array, Hash Table, Greedy, Sliding Window, Sorting, Heap
 *
 * Algorithm:
 * Min-heap of size K containing the current element from each list.
 * Track current maximum across the heap. Range is [minHeap.peek(), maxVal].
 * Advance pointer in the list containing the minimum element.
 *
 * Time Complexity: O(N * log K) where N is total elements across all lists
 * Space Complexity: O(K)
 */
public class LC0632_SmallestRange {

    public int[] smallestRange(List<List<Integer>> nums) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < nums.size(); i++) {
            int val = nums.get(i).get(0);
            pq.offer(new int[]{val, i, 0});
            max = Math.max(max, val);
        }

        int[] res = {pq.peek()[0], max};

        while (true) {
            int[] cur = pq.poll();
            int r = cur[1], c = cur[2];
            if (c + 1 >= nums.get(r).size()) break;

            int next = nums.get(r).get(c + 1);
            pq.offer(new int[]{next, r, c + 1});
            max = Math.max(max, next);

            if (max - pq.peek()[0] < res[1] - res[0]) {
                res[0] = pq.peek()[0];
                res[1] = max;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        LC0632_SmallestRange sol = new LC0632_SmallestRange();
        List<List<Integer>> lists = Arrays.asList(
            Arrays.asList(4,10,15,24,26),
            Arrays.asList(0,9,12,20),
            Arrays.asList(5,18,22,30)
        );
        System.out.println(Arrays.toString(sol.smallestRange(lists))); // [20, 24]
    }
}
