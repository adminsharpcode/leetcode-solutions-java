public class LC0572_SubtreeOfAnotherTree {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
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
        root.left = new TreeNode(4); root.right = new TreeNode(5);
        root.left.left = new TreeNode(1); root.left.right = new TreeNode(2);
        TreeNode sub = new TreeNode(4);
        sub.left = new TreeNode(1); sub.right = new TreeNode(2);
        System.out.println(sol.isSubtree(root, sub)); // true
    }
}
