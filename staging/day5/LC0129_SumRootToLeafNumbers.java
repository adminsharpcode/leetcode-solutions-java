/**
 * Problem: 129. Sum Root to Leaf Numbers
 * Difficulty: Medium
 * Category: Tree, Depth-First Search, Binary Tree
 *
 * Algorithm:
 * DFS: Carry running number cur = cur * 10 + node.val down each branch.
 * Sum running numbers at leaf nodes.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(H)
 */
public class LC0129_SumRootToLeafNumbers {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int currentSum) {
        if (node == null) return 0;
        currentSum = currentSum * 10 + node.val;

        if (node.left == null && node.right == null) {
            return currentSum;
        }

        return dfs(node.left, currentSum) + dfs(node.right, currentSum);
    }

    public static void main(String[] args) {
        LC0129_SumRootToLeafNumbers solver = new LC0129_SumRootToLeafNumbers();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        assert solver.sumNumbers(root) == 25; // 12 + 13
        System.out.println("LC0129_SumRootToLeafNumbers passed all tests!");
    }
}
