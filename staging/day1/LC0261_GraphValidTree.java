public class LC0261_GraphValidTree {
    int[] parent;
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false;
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int[] e : edges) {
            int a = find(e[0]), b = find(e[1]);
            if (a == b) return false;
            parent[a] = b;
        }
        return true;
    }
    int find(int x) { return parent[x] == x ? x : (parent[x] = find(parent[x])); }
    public static void main(String[] args) {
        LC0261_GraphValidTree sol = new LC0261_GraphValidTree();
        System.out.println(sol.validTree(5, new int[][]{{0,1},{0,2},{0,3},{1,4}})); // true
    }
}
