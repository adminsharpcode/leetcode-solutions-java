import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;

/**
 * LeetCode 210: Course Schedule II
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/course-schedule-ii/
 *
 * Approach: Topological Sort via Kahn's Algorithm (BFS with In-Degrees)
 * Time Complexity: O(V + E)
 * Space Complexity: O(V + E)
 */
public class LC0210_CourseScheduleII {

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] inDegree = new int[numCourses];

        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] pre : prerequisites) {
            adj.get(pre[1]).add(pre[0]);
            inDegree[pre[0]]++;
        }

        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }

        int[] order = new int[numCourses];
        int index = 0;

        while (!queue.isEmpty()) {
            int course = queue.poll();
            order[index++] = course;

            for (int next : adj.get(course)) {
                inDegree[next]--;
                if (inDegree[next] == 0) {
                    queue.offer(next);
                }
            }
        }

        return (index == numCourses) ? order : new int[]{};
    }

    public static void main(String[] args) {
        LC0210_CourseScheduleII solver = new LC0210_CourseScheduleII();
        int[][] prereqs = {{1, 0}, {2, 0}, {3, 1}, {3, 2}};
        System.out.println("Order: " + Arrays.toString(solver.findOrder(4, prereqs)));
        // Expected: [0, 1, 2, 3] or [0, 2, 1, 3]
    }
}
