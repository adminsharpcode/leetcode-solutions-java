import java.util.LinkedList;
import java.util.Queue;

/**
 * Problem: 111. Minimum Depth of Binary Tree
 * Difficulty: Easy
 * Category: Tree, Depth-First Search, Breadth-First Search, Binary Tree
 *
 * Algorithm:
 * BFS level-order traversal: the very first leaf node encountered is guaranteed
 * to be at the minimum depth.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0111_MinimumDepthOfBinaryTree {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    public int minDepth(TreeNode root) {
        if (root == null) return 0;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int depth = 1;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode curr = queue.poll();
                if (curr.left == null && curr.right == null) {
                    return depth;
                }
                if (curr.left != null) queue.offer(curr.left);
                if (curr.right != null) queue.offer(curr.right);
            }
            depth++;
        }
        return depth;
    }

    public static void main(String[] args) {
        LC0111_MinimumDepthOfBinaryTree solver = new LC0111_MinimumDepthOfBinaryTree();
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        assert solver.minDepth(root) == 2;
        System.out.println("LC0111_MinimumDepthOfBinaryTree passed all tests!");
    }
}
