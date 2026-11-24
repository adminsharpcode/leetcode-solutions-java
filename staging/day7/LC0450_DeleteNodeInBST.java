public class LC0450_DeleteNodeInBST {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (key < root.val) root.left = deleteNode(root.left, key);
        else if (key > root.val) root.right = deleteNode(root.right, key);
        else {
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            TreeNode min = root.right;
            while (min.left != null) min = min.left;
            root.val = min.val;
            root.right = deleteNode(root.right, min.val);
        }
        return root;
    }
    public static void main(String[] args) {
        LC0450_DeleteNodeInBST sol = new LC0450_DeleteNodeInBST();
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(3); root.right = new TreeNode(6);
        root.left.left = new TreeNode(2); root.left.right = new TreeNode(4);
        root.right.right = new TreeNode(7);
        TreeNode res = sol.deleteNode(root, 3);
        System.out.println(res.left.val); // 4 or 2 depending on impl
    }
}
