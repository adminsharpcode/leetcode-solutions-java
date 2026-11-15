import java.util.*;

/**
 * Problem: 57. Insert Interval
 * Difficulty: Medium
 * Category: Array, Intervals
 *
 * Algorithm:
 * 1. Add all intervals ending before newInterval starts.
 * 2. Merge all overlapping intervals with newInterval.
 * 3. Add all remaining intervals.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N) for output
 */
public class LC0057_InsertInterval {

    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        int i = 0;
        int n = intervals.length;

        // 1. Non-overlapping before
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.add(intervals[i++]);
        }

        // 2. Overlapping: merge
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.add(newInterval);

        // 3. Non-overlapping after
        while (i < n) {
            result.add(intervals[i++]);
        }

        return result.toArray(new int[result.size()][]);
    }

    public static void main(String[] args) {
        LC0057_InsertInterval solver = new LC0057_InsertInterval();
        int[][] intervals = {{1, 3}, {6, 9}};
        int[] newInterval = {2, 5};
        int[][] res = solver.insert(intervals, newInterval);
        assert res.length == 2;
        assert res[0][0] == 1 && res[0][1] == 5;
        System.out.println("LC0057_InsertInterval passed all tests!");
    }
}
