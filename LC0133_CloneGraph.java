import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * LeetCode 133: Clone Graph
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/clone-graph/
 *
 * Approach: Depth-First Search (DFS) with Visited Map
 * Time Complexity: O(V + E)
 * Space Complexity: O(V)
 */
public class LC0133_CloneGraph {

    public static class Node {
        public int val;
        public List<Node> neighbors;
        public Node() {
            val = 0;
            neighbors = new ArrayList<>();
        }
        public Node(int _val) {
            val = _val;
            neighbors = new ArrayList<>();
        }
        public Node(int _val, ArrayList<Node> _neighbors) {
            val = _val;
            neighbors = _neighbors;
        }
    }

    private Map<Node, Node> visited = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) return null;
        if (visited.containsKey(node)) return visited.get(node);

        Node cloneNode = new Node(node.val, new ArrayList<>());
        visited.put(node, cloneNode);

        for (Node neighbor : node.neighbors) {
            cloneNode.neighbors.add(cloneGraph(neighbor));
        }

        return cloneNode;
    }

    public static void main(String[] args) {
        LC0133_CloneGraph solver = new LC0133_CloneGraph();
        Node n1 = new Node(1);
        Node n2 = new Node(2);
        n1.neighbors.add(n2);
        n2.neighbors.add(n1);

        Node cloned = solver.cloneGraph(n1);
        System.out.println("Cloned root val: " + cloned.val);
        System.out.println("Neighbor val: " + cloned.neighbors.get(0).val);
    }
}
