/**
 * LeetCode 100: Same Tree
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/same-tree/
 *
 * Approach: Recursive DFS structural and value comparison
 * Time Complexity: O(N)
 * Space Complexity: O(H) where H is tree height
 */
public class LC0100_SameTree {

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

    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if (p == null || q == null || p.val != q.val) {
            return false;
        }
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

    public static void main(String[] args) {
        LC0100_SameTree solver = new LC0100_SameTree();
        TreeNode t1 = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        TreeNode t2 = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        System.out.println("Same tree: " + solver.isSameTree(t1, t2)); // Expected: true
    }
}
