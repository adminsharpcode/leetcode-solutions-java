/**
 * Problem: 538. Convert BST to Greater Tree
 * Difficulty: Medium
 * Category: Tree, Depth-First Search, Binary Search Tree, Binary Tree
 *
 * Algorithm:
 * Reverse in-order traversal: Right -> Root -> Left.
 * Accumulate running sum and assign to current node.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(H)
 */
public class LC0538_ConvertBSTToGreaterTree {

    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    private int sum = 0;

    public TreeNode convertBST(TreeNode root) {
        if (root != null) {
            convertBST(root.right);
            sum += root.val;
            root.val = sum;
            convertBST(root.left);
        }
        return root;
    }

    public static void main(String[] args) {
        LC0538_ConvertBSTToGreaterTree sol = new LC0538_ConvertBSTToGreaterTree();
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(1);
        root.right = new TreeNode(6);
        TreeNode res = sol.convertBST(root);
        System.out.println("Root new val: " + res.val); // 10
    }
}
