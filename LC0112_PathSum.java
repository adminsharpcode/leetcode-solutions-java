/**
 * Problem: 112. Path Sum
 * Difficulty: Easy
 * Category: Tree, Depth-First Search, Binary Tree
 *
 * Algorithm:
 * DFS: Subtract current root value from targetSum. If at a leaf, check if remainder is 0.
 * Otherwise, recurse on left and right children.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(H) where H is tree height
 */
public class LC0112_PathSum {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        if (root.left == null && root.right == null) {
            return root.val == targetSum;
        }
        return hasPathSum(root.left, targetSum - root.val) ||
               hasPathSum(root.right, targetSum - root.val);
    }

    public static void main(String[] args) {
        LC0112_PathSum solver = new LC0112_PathSum();
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(4);
        root.right = new TreeNode(8);
        root.left.left = new TreeNode(11);
        root.left.left.left = new TreeNode(7);
        root.left.left.right = new TreeNode(2);
        assert solver.hasPathSum(root, 22);
        assert !solver.hasPathSum(root, 100);
        System.out.println("LC0112_PathSum passed all tests!");
    }
}
