import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Problem: 199. Binary Tree Right Side View
 * Difficulty: Medium
 * Category: Tree, Depth-First Search, Breadth-First Search, Binary Tree
 *
 * Algorithm:
 * BFS level-order traversal: for each depth level, append the last node's value
 * to the output list.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(D) where D is max diameter of tree
 */
public class LC0199_BinaryTreeRightSideView {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                if (i == levelSize - 1) {
                    result.add(node.val);
                }
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        LC0199_BinaryTreeRightSideView solver = new LC0199_BinaryTreeRightSideView();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.right = new TreeNode(5);
        root.right.right = new TreeNode(4);
        List<Integer> res = solver.rightSideView(root);
        assert res.size() == 3 && res.get(0) == 1 && res.get(1) == 3 && res.get(2) == 4;
        System.out.println("LC0199_BinaryTreeRightSideView passed all tests!");
    }
}
