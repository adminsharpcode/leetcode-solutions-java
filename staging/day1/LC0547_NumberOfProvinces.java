/**
 * Problem: 547. Number of Provinces
 * Difficulty: Medium
 * Category: Depth-First Search, Breadth-First Search, Union Find, Graph
 *
 * Algorithm:
 * Disjoint Set Union (DSU) or standard visited DFS over n cities.
 * For each city, if not visited, launch DFS to mark all transitively connected cities.
 * Increment province counter per connected component.
 *
 * Time Complexity: O(N^2)
 * Space Complexity: O(N)
 */
public class LC0547_NumberOfProvinces {

    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(isConnected, visited, i, n);
                count++;
            }
        }
        return count;
    }

    private void dfs(int[][] matrix, boolean[] visited, int i, int n) {
        visited[i] = true;
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 1 && !visited[j]) {
                dfs(matrix, visited, j, n);
            }
        }
    }

    public static void main(String[] args) {
        LC0547_NumberOfProvinces sol = new LC0547_NumberOfProvinces();
        int[][] conn = {{1,1,0},{1,1,0},{0,0,1}};
        System.out.println("Provinces: " + sol.findCircleNum(conn)); // 2
    }
}
