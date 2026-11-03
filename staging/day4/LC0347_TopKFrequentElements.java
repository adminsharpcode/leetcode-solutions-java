import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

/**
 * LeetCode 347: Top K Frequent Elements
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/top-k-frequent-elements/
 *
 * Approach: Hash Map Frequency Count + Min-Heap of Size K
 * Time Complexity: O(N log K)
 * Space Complexity: O(N + K)
 */
public class LC0347_TopKFrequentElements {

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Min-heap ordered by frequency ascending
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b) -> freqMap.get(a) - freqMap.get(b));

        for (int num : freqMap.keySet()) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = minHeap.poll();
        }

        return result;
    }

    public static void main(String[] args) {
        LC0347_TopKFrequentElements solver = new LC0347_TopKFrequentElements();
        int[] nums = {1, 1, 1, 2, 2, 3};
        System.out.println("Top 2: " + Arrays.toString(solver.topKFrequent(nums, 2))); // Expected: [2, 1] (or [1, 2])
    }
}
