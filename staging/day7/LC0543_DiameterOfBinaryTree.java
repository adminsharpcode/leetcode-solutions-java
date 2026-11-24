/**
 * Problem: 543. Diameter of Binary Tree
 * Difficulty: Easy
 * Category: Tree, Depth-First Search, Binary Tree
 *
 * Algorithm:
 * Post-order DFS computing max depth of left and right subtrees.
 * Diameter at each node is left_depth + right_depth.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(H)
 */
public class LC0543_DiameterOfBinaryTree {

    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    private int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        maxDiameter = 0;
        depth(root);
        return maxDiameter;
    }

    private int depth(TreeNode node) {
        if (node == null) return 0;
        int l = depth(node.left);
        int r = depth(node.right);
        maxDiameter = Math.max(maxDiameter, l + r);
        return 1 + Math.max(l, r);
    }

    public static void main(String[] args) {
        LC0543_DiameterOfBinaryTree sol = new LC0543_DiameterOfBinaryTree();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        System.out.println("Diameter: " + sol.diameterOfBinaryTree(root)); // 2
    }
}
