/**
 * LeetCode 236: Lowest Common Ancestor of a Binary Tree
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
 *
 * Approach: Post-Order DFS with Subtree Node Discovery
 * Time Complexity: O(N)
 * Space Complexity: O(H) where H is tree height
 */
public class LC0236_LowestCommonAncestorOfABinaryTree {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) {
            return root;
        }

        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);

        if (left != null && right != null) {
            return root;
        }

        return (left != null) ? left : right;
    }

    public static void main(String[] args) {
        LC0236_LowestCommonAncestorOfABinaryTree solver =
            new LC0236_LowestCommonAncestorOfABinaryTree();
        TreeNode root = new TreeNode(3);
        TreeNode p = new TreeNode(5);
        TreeNode q = new TreeNode(1);
        root.left = p;
        root.right = q;

        TreeNode lca = solver.lowestCommonAncestor(root, p, q);
        System.out.println("LCA val: " + lca.val); // Expected: 3
    }
}
