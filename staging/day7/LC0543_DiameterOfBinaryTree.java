public class LC0543_DiameterOfBinaryTree {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    int max = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        depth(root);
        return max;
    }
    private int depth(TreeNode node) {
        if (node == null) return 0;
        int l = depth(node.left), r = depth(node.right);
        max = Math.max(max, l + r);
        return 1 + Math.max(l, r);
    }
    public static void main(String[] args) {
        LC0543_DiameterOfBinaryTree sol = new LC0543_DiameterOfBinaryTree();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2); root.right = new TreeNode(3);
        root.left.left = new TreeNode(4); root.left.right = new TreeNode(5);
        System.out.println(sol.diameterOfBinaryTree(root)); // 3
    }
}
