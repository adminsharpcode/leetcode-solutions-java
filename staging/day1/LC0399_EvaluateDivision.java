import java.util.*;
public class LC0399_EvaluateDivision {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> graph = new HashMap<>();
        for (int i = 0; i < equations.size(); i++) {
            String a = equations.get(i).get(0), b = equations.get(i).get(1);
            graph.computeIfAbsent(a, k -> new HashMap<>()).put(b, values[i]);
            graph.computeIfAbsent(b, k -> new HashMap<>()).put(a, 1.0 / values[i]);
        }
        double[] res = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            String src = queries.get(i).get(0), dst = queries.get(i).get(1);
            res[i] = dfs(graph, src, dst, new HashSet<>());
        }
        return res;
    }
    private double dfs(Map<String, Map<String, Double>> g, String src, String dst, Set<String> visited) {
        if (!g.containsKey(src) || !g.containsKey(dst)) return -1.0;
        if (src.equals(dst)) return 1.0;
        visited.add(src);
        for (Map.Entry<String, Double> e : g.get(src).entrySet()) {
            if (!visited.contains(e.getKey())) {
                double res = dfs(g, e.getKey(), dst, visited);
                if (res != -1.0) return res * e.getValue();
            }
        }
        return -1.0;
    }
    public static void main(String[] args) {
        LC0399_EvaluateDivision sol = new LC0399_EvaluateDivision();
        List<List<String>> eq = Arrays.asList(Arrays.asList("a","b"), Arrays.asList("b","c"));
        double[] vals = {2.0, 3.0};
        List<List<String>> q = Arrays.asList(Arrays.asList("a","c"), Arrays.asList("b","a"));
        System.out.println(Arrays.toString(sol.calcEquation(eq, vals, q))); // [6.0, 0.5]
    }
}
