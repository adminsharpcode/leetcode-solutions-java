import java.util.Arrays;

/**
 * LeetCode 435: Non-overlapping Intervals
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/non-overlapping-intervals/
 *
 * Approach: Greedy Activity Selection (Sort by End Time)
 * Time Complexity: O(N log N)
 * Space Complexity: O(1)
 */
public class LC0435_NonOverlappingIntervals {

    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }

        // Sort by end time ascending
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));

        int removedCount = 0;
        int lastEnd = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < lastEnd) {
                // Overlap detected: greedily discard the one ending later
                removedCount++;
            } else {
                lastEnd = intervals[i][1];
            }
        }

        return removedCount;
    }

    public static void main(String[] args) {
        LC0435_NonOverlappingIntervals solver = new LC0435_NonOverlappingIntervals();
        int[][] intervals = {{1, 2}, {2, 3}, {3, 4}, {1, 3}};
        System.out.println("Intervals to remove: " + solver.eraseOverlapIntervals(intervals)); // Expected: 1
    }
}
