public class LC0538_ConvertBSTToGreaterTree {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    int sum = 0;
    public TreeNode convertBST(TreeNode root) {
        if (root != null) {
            convertBST(root.right);
            sum += root.val;
            root.val = sum;
            convertBST(root.left);
        }
        return root;
    }
    public static void main(String[] args) {
        LC0538_ConvertBSTToGreaterTree sol = new LC0538_ConvertBSTToGreaterTree();
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(1); root.right = new TreeNode(6);
        TreeNode res = sol.convertBST(root);
        System.out.println(res.val); // 10
    }
}
