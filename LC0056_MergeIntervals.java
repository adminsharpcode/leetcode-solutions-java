import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * LeetCode 56: Merge Intervals
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/merge-intervals/
 *
 * Approach: Sorting by Start Time + Greedy Merge
 * Time Complexity: O(N log N)
 * Space Complexity: O(N)
 */
public class LC0056_MergeIntervals {

    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) return intervals;

        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> merged = new ArrayList<>();

        int[] current = intervals[0];
        merged.add(current);

        for (int i = 1; i < intervals.length; i++) {
            int[] interval = intervals[i];
            if (interval[0] <= current[1]) { // Overlap detected
                current[1] = Math.max(current[1], interval[1]);
            } else {
                current = interval;
                merged.add(current);
            }
        }

        return merged.toArray(new int[merged.size()][]);
    }

    public static void main(String[] args) {
        LC0056_MergeIntervals solver = new LC0056_MergeIntervals();
        int[][] intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
        int[][] res = solver.merge(intervals);
        System.out.println("Merged Intervals: " + Arrays.deepToString(res)); // Expected: [[1,6],[8,10],[15,18]]
    }
}
