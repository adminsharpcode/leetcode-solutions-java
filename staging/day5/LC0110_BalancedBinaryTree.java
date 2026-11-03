/**
 * LeetCode 110: Balanced Binary Tree
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/balanced-binary-tree/
 *
 * Approach: Bottom-up Post-Order DFS with early sentinel termination (-1)
 * Time Complexity: O(N)
 * Space Complexity: O(H) where H is tree height
 */
public class LC0110_BalancedBinaryTree {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public boolean isBalanced(TreeNode root) {
        return checkHeight(root) != -1;
    }

    private int checkHeight(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftHeight = checkHeight(root.left);
        if (leftHeight == -1) return -1;

        int rightHeight = checkHeight(root.right);
        if (rightHeight == -1) return -1;

        if (Math.abs(leftHeight - rightHeight) > 1) {
            return -1;
        }

        return 1 + Math.max(leftHeight, rightHeight);
    }

    public static void main(String[] args) {
        LC0110_BalancedBinaryTree solver = new LC0110_BalancedBinaryTree();
        TreeNode root = new TreeNode(3,
            new TreeNode(9),
            new TreeNode(20, new TreeNode(15), new TreeNode(7))
        );
        System.out.println("Is balanced: " + solver.isBalanced(root)); // Expected: true
    }
}
