import java.util.*;

/**
 * Problem: 310. Minimum Height Trees
 * Difficulty: Medium
 * Category: Tree, Breadth-First Search, Graph, Topological Sort
 *
 * Algorithm:
 * Prune leaves inward level by level until 1 or 2 nodes remain (the centroid(s)).
 * Start with all nodes having degree 1, strip leaves until remaining <= 2.
 *
 * Time Complexity: O(V + E)
 * Space Complexity: O(V + E)
 */
public class LC0310_MinimumHeightTrees {

    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) return Collections.singletonList(0);

        List<Set<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new HashSet<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        List<Integer> leaves = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (adj.get(i).size() == 1) leaves.add(i);
        }

        int remaining = n;
        while (remaining > 2) {
            remaining -= leaves.size();
            List<Integer> newLeaves = new ArrayList<>();
            for (int leaf : leaves) {
                int neighbor = adj.get(leaf).iterator().next();
                adj.get(neighbor).remove(leaf);
                if (adj.get(neighbor).size() == 1) newLeaves.add(neighbor);
            }
            leaves = newLeaves;
        }
        return leaves;
    }

    public static void main(String[] args) {
        LC0310_MinimumHeightTrees sol = new LC0310_MinimumHeightTrees();
        int[][] edges = {{1,0}, {1,2}, {1,3}};
        System.out.println("MHT roots: " + sol.findMinHeightTrees(4, edges)); // [1]
    }
}
