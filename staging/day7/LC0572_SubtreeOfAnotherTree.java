/**
 * Problem: 572. Subtree of Another Tree
 * Difficulty: Easy
 * Category: Tree, Depth-First Search, String Matching, Binary Tree, Hash Function
 *
 * Algorithm:
 * Check if current tree is identical to subRoot via isSame(root, subRoot).
 * If not, recurse on left and right children.
 *
 * Time Complexity: O(M * N)
 * Space Complexity: O(H)
 */
public class LC0572_SubtreeOfAnotherTree {

    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) return false;
        if (isSame(root, subRoot)) return true;
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    private boolean isSame(TreeNode a, TreeNode b) {
        if (a == null && b == null) return true;
        if (a == null || b == null) return false;
        return a.val == b.val && isSame(a.left, b.left) && isSame(a.right, b.right);
    }

    public static void main(String[] args) {
        LC0572_SubtreeOfAnotherTree sol = new LC0572_SubtreeOfAnotherTree();
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(4);
        root.right = new TreeNode(5);
        TreeNode sub = new TreeNode(4);
        System.out.println("Is subtree: " + sol.isSubtree(root, sub)); // true
    }
}
