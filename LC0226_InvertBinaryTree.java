/**
 * LeetCode 226: Invert Binary Tree
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/invert-binary-tree/
 *
 * Approach: Recursive DFS Subtree Inversion
 * Time Complexity: O(N)
 * Space Complexity: O(H) where H is tree height
 */
public class LC0226_InvertBinaryTree {

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

    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }

        TreeNode temp = root.left;
        root.left = invertTree(root.right);
        root.right = invertTree(temp);

        return root;
    }

    public static void main(String[] args) {
        LC0226_InvertBinaryTree solver = new LC0226_InvertBinaryTree();

        // Tree: [4, 2, 7, 1, 3, 6, 9]
        TreeNode root = new TreeNode(4,
            new TreeNode(2, new TreeNode(1), new TreeNode(3)),
            new TreeNode(7, new TreeNode(6), new TreeNode(9))
        );

        TreeNode inverted = solver.invertTree(root);
        System.out.println("Inverted root: " + inverted.val); // Expected: 4
        System.out.println("Left child: " + inverted.left.val); // Expected: 7
        System.out.println("Right child: " + inverted.right.val); // Expected: 2
    }
}
