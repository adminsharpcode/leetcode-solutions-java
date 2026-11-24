/**
 * Problem: 450. Delete Node in a BST
 * Difficulty: Medium
 * Category: Tree, Binary Search Tree, Binary Tree
 *
 * Algorithm:
 * Locate target node via BST property.
 * If 0 or 1 child, return existing child. If 2 children, swap with inorder successor and delete successor.
 *
 * Time Complexity: O(H) where H is tree height
 * Space Complexity: O(H) recursion stack
 */
public class LC0450_DeleteNodeInBST {

    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;

        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else {
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;

            TreeNode successor = root.right;
            while (successor.left != null) successor = successor.left;
            root.val = successor.val;
            root.right = deleteNode(root.right, successor.val);
        }
        return root;
    }

    public static void main(String[] args) {
        LC0450_DeleteNodeInBST sol = new LC0450_DeleteNodeInBST();
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(3);
        root.right = new TreeNode(6);
        TreeNode res = sol.deleteNode(root, 3);
        System.out.println("New left child: " + (res.left != null ? res.left.val : "null"));
    }
}
