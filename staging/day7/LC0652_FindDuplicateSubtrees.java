import java.util.*;

/**
 * Problem: 652. Find Duplicate Subtrees
 * Difficulty: Medium
 * Category: Hash Table, Tree, Depth-First Search, Binary Tree
 *
 * Algorithm:
 * Post-order serialization string for each subtree.
 * HashMap tracks frequency of serialized representations; collect duplicate root nodes.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0652_FindDuplicateSubtrees {

    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    private Map<String, Integer> count = new HashMap<>();
    private List<TreeNode> res = new ArrayList<>();

    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        count.clear();
        res.clear();
        serialize(root);
        return res;
    }

    private String serialize(TreeNode node) {
        if (node == null) return "#";
        String key = node.val + "," + serialize(node.left) + "," + serialize(node.right);
        count.merge(key, 1, Integer::sum);
        if (count.get(key) == 2) {
            res.add(node);
        }
        return key;
    }

    public static void main(String[] args) {
        LC0652_FindDuplicateSubtrees sol = new LC0652_FindDuplicateSubtrees();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.right.left = new TreeNode(2);
        root.right.left.left = new TreeNode(4);
        List<TreeNode> dups = sol.findDuplicateSubtrees(root);
        System.out.println("Duplicate subtrees count: " + dups.size()); // 2
    }
}
