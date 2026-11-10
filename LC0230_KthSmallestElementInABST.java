import java.util.ArrayDeque;
import java.util.Deque;

/**
 * LeetCode 230: Kth Smallest Element in a BST
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
 *
 * Approach: Iterative In-Order Traversal with Stack
 * Time Complexity: O(H + K)
 * Space Complexity: O(H) where H is tree height
 */
public class LC0230_KthSmallestElementInABST {

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

    public int kthSmallest(TreeNode root, int k) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode curr = root;

        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }

            curr = stack.pop();
            k--;
            if (k == 0) {
                return curr.val;
            }

            curr = curr.right;
        }

        return -1;
    }

    public static void main(String[] args) {
        LC0230_KthSmallestElementInABST solver = new LC0230_KthSmallestElementInABST();
        TreeNode root = new TreeNode(3,
            new TreeNode(1, null, new TreeNode(2)),
            new TreeNode(4)
        );
        System.out.println("1st smallest: " + solver.kthSmallest(root, 1)); // Expected: 1
    }
}
