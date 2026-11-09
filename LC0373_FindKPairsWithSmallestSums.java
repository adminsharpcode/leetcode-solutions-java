import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

/**
 * LeetCode 373: Find K Pairs with Smallest Sums
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
 *
 * Approach: PriorityQueue Min-Heap with index coordinate tracking
 * Time Complexity: O(K log(min(N, K)))
 * Space Complexity: O(min(N, K))
 */
public class LC0373_FindKPairsWithSmallestSums {

    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums1 == null || nums2 == null || nums1.length == 0 || nums2.length == 0 || k <= 0) {
            return result;
        }

        // Heap elements: [sum, indexInNums1, indexInNums2]
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        // Push pairs of (nums1[i], nums2[0])
        for (int i = 0; i < Math.min(nums1.length, k); i++) {
            minHeap.offer(new int[]{nums1[i] + nums2[0], i, 0});
        }

        while (k > 0 && !minHeap.isEmpty()) {
            int[] curr = minHeap.poll();
            int i = curr[1];
            int j = curr[2];

            result.add(Arrays.asList(nums1[i], nums2[j]));
            k--;

            if (j + 1 < nums2.length) {
                minHeap.offer(new int[]{nums1[i] + nums2[j + 1], i, j + 1});
            }
        }

        return result;
    }

    public static void main(String[] args) {
        LC0373_FindKPairsWithSmallestSums solver = new LC0373_FindKPairsWithSmallestSums();
        int[] nums1 = {1, 7, 11};
        int[] nums2 = {2, 4, 6};
        System.out.println("Result: " + solver.kSmallestPairs(nums1, nums2, 3));
        // Expected: [[1, 2], [1, 4], [1, 6]]
    }
}
