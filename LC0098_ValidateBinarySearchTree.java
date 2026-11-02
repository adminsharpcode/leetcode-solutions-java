/**
 * LeetCode 98: Validate Binary Search Tree
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/validate-binary-search-tree/
 *
 * Approach: Recursive DFS with Range Boundaries
 * Time Complexity: O(N)
 * Space Complexity: O(H) call stack height
 */
public class LC0098_ValidateBinarySearchTree {

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

    public boolean isValidBST(TreeNode root) {
        return validate(root, null, null);
    }

    private boolean validate(TreeNode node, Long low, Long high) {
        if (node == null) return true;
        if ((low != null && node.val <= low) || (high != null && node.val >= high)) {
            return false;
        }
        return validate(node.left, low, (long) node.val) && validate(node.right, (long) node.val, high);
    }

    public static void main(String[] args) {
        LC0098_ValidateBinarySearchTree solver = new LC0098_ValidateBinarySearchTree();
        TreeNode root = new TreeNode(2, new TreeNode(1), new TreeNode(3));
        System.out.println("Is valid BST: " + solver.isValidBST(root)); // Expected: true
    }
}
