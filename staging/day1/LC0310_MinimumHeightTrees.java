import java.util.*;
public class LC0310_MinimumHeightTrees {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) return Collections.singletonList(0);
        List<Set<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new HashSet<>());
        for (int[] e : edges) { adj.get(e[0]).add(e[1]); adj.get(e[1]).add(e[0]); }
        List<Integer> leaves = new ArrayList<>();
        for (int i = 0; i < n; i++) if (adj.get(i).size() == 1) leaves.add(i);
        int remaining = n;
        while (remaining > 2) {
            remaining -= leaves.size();
            List<Integer> next = new ArrayList<>();
            for (int leaf : leaves) {
                int nb = adj.get(leaf).iterator().next();
                adj.get(nb).remove(leaf);
                if (adj.get(nb).size() == 1) next.add(nb);
            }
            leaves = next;
        }
        return leaves;
    }
    public static void main(String[] args) {
        LC0310_MinimumHeightTrees sol = new LC0310_MinimumHeightTrees();
        System.out.println(sol.findMinHeightTrees(4, new int[][]{{1,0},{1,2},{1,3}})); // [1]
    }
}
