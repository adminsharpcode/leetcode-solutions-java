import java.util.*;

/**
 * Problem: 399. Evaluate Division
 * Difficulty: Medium
 * Category: Graph, Depth-First Search, Breadth-First Search, Union Find
 *
 * Algorithm:
 * Model variables as graph nodes. Edge (u -> v) has weight val, (v -> u) has 1/val.
 * For each query (src, dst), perform DFS/BFS to find path product.
 *
 * Time Complexity: O(Q * (V + E))
 * Space Complexity: O(V + E)
 */
public class LC0399_EvaluateDivision {

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> graph = new HashMap<>();

        for (int i = 0; i < equations.size(); i++) {
            String u = equations.get(i).get(0);
            String v = equations.get(i).get(1);
            double val = values[i];

            graph.computeIfAbsent(u, k -> new HashMap<>()).put(v, val);
            graph.computeIfAbsent(v, k -> new HashMap<>()).put(u, 1.0 / val);
        }

        double[] res = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            String src = queries.get(i).get(0);
            String dst = queries.get(i).get(1);
            res[i] = dfs(graph, src, dst, new HashSet<>());
        }
        return res;
    }

    private double dfs(Map<String, Map<String, Double>> g, String cur, String target, Set<String> visited) {
        if (!g.containsKey(cur) || !g.containsKey(target)) return -1.0;
        if (cur.equals(target)) return 1.0;

        visited.add(cur);
        for (Map.Entry<String, Double> neighbor : g.get(cur).entrySet()) {
            if (!visited.contains(neighbor.getKey())) {
                double sub = dfs(g, neighbor.getKey(), target, visited);
                if (sub != -1.0) return sub * neighbor.getValue();
            }
        }
        return -1.0;
    }

    public static void main(String[] args) {
        LC0399_EvaluateDivision sol = new LC0399_EvaluateDivision();
        List<List<String>> eq = Arrays.asList(Arrays.asList("a","b"), Arrays.asList("b","c"));
        double[] vals = {2.0, 3.0};
        List<List<String>> queries = Arrays.asList(Arrays.asList("a","c"), Arrays.asList("b","a"));
        System.out.println(Arrays.toString(sol.calcEquation(eq, vals, queries))); // [6.0, 0.5]
    }
}
