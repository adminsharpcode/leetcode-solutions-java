/**
 * Problem: 108. Convert Sorted Array to Binary Search Tree
 * Difficulty: Easy
 * Category: Tree, Binary Search Tree, Binary Tree, Divide and Conquer
 *
 * Algorithm:
 * Recursively pick the middle element of the array slice as root, constructing left
 * and right subtrees from left and right halves respectively to maintain height-balance.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(log N) recursion stack
 */
public class LC0108_ConvertSortedArrayToBST {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums == null || nums.length == 0) return null;
        return build(nums, 0, nums.length - 1);
    }

    private TreeNode build(int[] nums, int left, int right) {
        if (left > right) return null;
        int mid = left + (right - left) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = build(nums, left, mid - 1);
        root.right = build(nums, mid + 1, right);
        return root;
    }

    public static void main(String[] args) {
        LC0108_ConvertSortedArrayToBST solver = new LC0108_ConvertSortedArrayToBST();
        int[] nums = {-10, -3, 0, 5, 9};
        TreeNode root = solver.sortedArrayToBST(nums);
        assert root != null && root.val == 0;
        System.out.println("LC0108_ConvertSortedArrayToBST passed all tests!");
    }
}
