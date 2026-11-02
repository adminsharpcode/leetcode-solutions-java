import java.util.HashMap;
import java.util.Map;

/**
 * LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
 *
 * Approach: Divide & Conquer with Hash Map index lookup
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0105_ConstructBinaryTreeFromPreorderAndInorderTraversal {

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

    private int preorderIndex;
    private Map<Integer, Integer> inorderIndexMap;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        preorderIndex = 0;
        inorderIndexMap = new HashMap<>();

        for (int i = 0; i < inorder.length; i++) {
            inorderIndexMap.put(inorder[i], i);
        }

        return build(preorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int left, int right) {
        if (left > right) {
            return null;
        }

        int rootVal = preorder[preorderIndex++];
        TreeNode root = new TreeNode(rootVal);

        int mid = inorderIndexMap.get(rootVal);

        root.left = build(preorder, left, mid - 1);
        root.right = build(preorder, mid + 1, right);

        return root;
    }

    public static void main(String[] args) {
        LC0105_ConstructBinaryTreeFromPreorderAndInorderTraversal solver =
            new LC0105_ConstructBinaryTreeFromPreorderAndInorderTraversal();

        int[] preorder = {3, 9, 20, 15, 7};
        int[] inorder = {9, 3, 15, 20, 7};

        TreeNode root = solver.buildTree(preorder, inorder);
        System.out.println("Root val: " + root.val); // Expected: 3
        System.out.println("Left child: " + root.left.val); // Expected: 9
        System.out.println("Right child: " + root.right.val); // Expected: 20
    }
}
