/**
 * LeetCode 104: Maximum Depth of Binary Tree
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
 *
 * Approach: Recursive DFS (Post-order Traversal)
 * Time Complexity: O(N)
 * Space Complexity: O(H) where H is tree height
 */
public class LC0104_MaximumDepthOfBinaryTree {

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

    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        return 1 + Math.max(leftDepth, rightDepth);
    }

    public static void main(String[] args) {
        LC0104_MaximumDepthOfBinaryTree solver = new LC0104_MaximumDepthOfBinaryTree();

        // [3, 9, 20, null, null, 15, 7]
        TreeNode root = new TreeNode(3,
            new TreeNode(9),
            new TreeNode(20, new TreeNode(15), new TreeNode(7))
        );

        System.out.println("Max Depth: " + solver.maxDepth(root)); // Expected: 3
    }
}
