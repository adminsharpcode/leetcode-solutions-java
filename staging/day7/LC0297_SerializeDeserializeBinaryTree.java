import java.util.*;

/**
 * Problem: 297. Serialize and Deserialize Binary Tree
 * Difficulty: Hard
 * Category: String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree
 *
 * Algorithm:
 * Preorder DFS traversal with "#" representing null pointers.
 * Deserialization uses recursive index pointer / token queue.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0297_SerializeDeserializeBinaryTree {

    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    public String serialize(TreeNode root) {
        if (root == null) return "#";
        return root.val + "," + serialize(root.left) + "," + serialize(root.right);
    }

    private int idx;

    public TreeNode deserialize(String data) {
        idx = 0;
        String[] tokens = data.split(",");
        return build(tokens);
    }

    private TreeNode build(String[] tokens) {
        if (idx >= tokens.length || tokens[idx].equals("#")) {
            idx++;
            return null;
        }
        TreeNode node = new TreeNode(Integer.parseInt(tokens[idx++]));
        node.left = build(tokens);
        node.right = build(tokens);
        return node;
    }

    public static void main(String[] args) {
        LC0297_SerializeDeserializeBinaryTree sol = new LC0297_SerializeDeserializeBinaryTree();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        String s = sol.serialize(root);
        System.out.println("Serialized: " + s); // 1,2,#,#,3,#,#
        TreeNode res = sol.deserialize(s);
        System.out.println("Re-serialized: " + sol.serialize(res));
    }
}
