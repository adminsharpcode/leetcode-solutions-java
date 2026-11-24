/**
 * Problem: 261. Graph Valid Tree
 * Difficulty: Medium
 * Category: Graph, Union Find, Breadth-First Search
 *
 * Algorithm:
 * A graph of N nodes is a valid tree iff it has exactly N - 1 edges and no cycles.
 * Use Union-Find: for each edge (u, v), find roots. If root(u) == root(v), cycle exists.
 *
 * Time Complexity: O(N * alpha(N))
 * Space Complexity: O(N)
 */
public class LC0261_GraphValidTree {

    private int[] parent;

    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false;

        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        for (int[] edge : edges) {
            int rootA = find(edge[0]);
            int rootB = find(edge[1]);
            if (rootA == rootB) return false;
            parent[rootA] = rootB;
        }
        return true;
    }

    private int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    public static void main(String[] args) {
        LC0261_GraphValidTree sol = new LC0261_GraphValidTree();
        int[][] edges = {{0,1}, {0,2}, {0,3}, {1,4}};
        System.out.println("Valid tree: " + sol.validTree(5, edges)); // true
    }
}
