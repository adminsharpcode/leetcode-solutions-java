import java.util.PriorityQueue;

/**
 * LeetCode 215: Kth Largest Element in an Array
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
 *
 * Approach: Min-Heap of size K
 * Time Complexity: O(N log K)
 * Space Complexity: O(K)
 */
public class LC0215_KthLargestElementInAnArray {

    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);
        for (int num : nums) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        return minHeap.peek();
    }

    public static void main(String[] args) {
        LC0215_KthLargestElementInAnArray solver = new LC0215_KthLargestElementInAnArray();
        int[] nums = {3, 2, 1, 5, 6, 4};
        System.out.println("2nd largest: " + solver.findKthLargest(nums, 2)); // Expected: 5
    }
}
