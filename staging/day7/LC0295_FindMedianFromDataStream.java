import java.util.Collections;
import java.util.PriorityQueue;

/**
 * Problem: 295. Find Median from Data Stream
 * Difficulty: Hard
 * Category: Two Heaps, Design, Data Stream
 *
 * Algorithm:
 * Two Heaps:
 * - maxHeap stores lower half of numbers.
 * - minHeap stores upper half of numbers.
 * Balance heaps so maxHeap has equal or 1 more element than minHeap.
 * Median is either maxHeap.peek() or average of peek from both heaps.
 *
 * Time Complexity: addNum: O(log N), findMedian: O(1)
 * Space Complexity: O(N)
 */
public class LC0295_FindMedianFromDataStream {

    private PriorityQueue<Integer> maxHeap;
    private PriorityQueue<Integer> minHeap;

    public LC0295_FindMedianFromDataStream() {
        maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        minHeap = new PriorityQueue<>();
    }

    public void addNum(int num) {
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.offer(num);
        } else {
            minHeap.offer(num);
        }

        // Rebalance
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.offer(maxHeap.poll());
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.offer(minHeap.poll());
        }
    }

    public double findMedian() {
        if (maxHeap.size() > minHeap.size()) {
            return (double) maxHeap.peek();
        } else {
            return (maxHeap.peek() + minHeap.peek()) / 2.0;
        }
    }

    public static void main(String[] args) {
        LC0295_FindMedianFromDataStream finder = new LC0295_FindMedianFromDataStream();
        finder.addNum(1);
        finder.addNum(2);
        assert finder.findMedian() == 1.5;
        finder.addNum(3);
        assert finder.findMedian() == 2.0;
        System.out.println("LC0295_FindMedianFromDataStream passed all tests!");
    }
}
