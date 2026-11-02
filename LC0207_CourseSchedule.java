import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

/**
 * LeetCode 207: Course Schedule
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/course-schedule/
 *
 * Approach: Topological Sort using Kahn's Algorithm (BFS with In-Degrees)
 * Time Complexity: O(V + E)
 * Space Complexity: O(V + E)
 */
public class LC0207_CourseSchedule {

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] inDegree = new int[numCourses];

        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] pre : prerequisites) {
            int course = pre[0];
            int prerequisite = pre[1];
            adj.get(prerequisite).add(course);
            inDegree[course]++;
        }

        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }

        int processedCourses = 0;
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            processedCourses++;

            for (int neighbor : adj.get(curr)) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        return processedCourses == numCourses;
    }

    public static void main(String[] args) {
        LC0207_CourseSchedule solver = new LC0207_CourseSchedule();

        int[][] prereqs1 = {{1, 0}};
        System.out.println("Can finish 1: " + solver.canFinish(2, prereqs1)); // Expected: true

        int[][] prereqs2 = {{1, 0}, {0, 1}};
        System.out.println("Can finish 2: " + solver.canFinish(2, prereqs2)); // Expected: false
    }
}
