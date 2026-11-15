import java.util.ArrayList;
import java.util.List;

/**
 * Problem: 113. Path Sum II
 * Difficulty: Medium
 * Category: Tree, Backtracking, Depth-First Search, Binary Tree
 *
 * Algorithm:
 * DFS backtracking: collect node values into a current path list.
 * When reaching a leaf where remainder equals node.val, save a copy of path.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(H) recursion stack
 */
public class LC0113_PathSumII {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> currentPath = new ArrayList<>();
        dfs(root, targetSum, currentPath, result);
        return result;
    }

    private void dfs(TreeNode node, int sum, List<Integer> currentPath, List<List<Integer>> result) {
        if (node == null) return;

        currentPath.add(node.val);

        if (node.left == null && node.right == null && sum == node.val) {
            result.add(new ArrayList<>(currentPath));
        } else {
            dfs(node.left, sum - node.val, currentPath, result);
            dfs(node.right, sum - node.val, currentPath, result);
        }

        currentPath.remove(currentPath.size() - 1);
    }

    public static void main(String[] args) {
        LC0113_PathSumII solver = new LC0113_PathSumII();
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(4);
        root.right = new TreeNode(8);
        root.left.left = new TreeNode(11);
        root.left.left.left = new TreeNode(7);
        root.left.left.right = new TreeNode(2);
        List<List<Integer>> paths = solver.pathSum(root, 22);
        assert paths.size() == 1;
        System.out.println("LC0113_PathSumII passed all tests!");
    }
}
