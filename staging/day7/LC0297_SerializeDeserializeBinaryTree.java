import java.util.*;
public class LC0297_SerializeDeserializeBinaryTree {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    public String serialize(TreeNode root) {
        if (root == null) return "#";
        return root.val + "," + serialize(root.left) + "," + serialize(root.right);
    }
    private int idx;
    public TreeNode deserialize(String data) {
        idx = 0;
        String[] parts = data.split(",");
        return build(parts);
    }
    private TreeNode build(String[] parts) {
        if (idx >= parts.length || parts[idx].equals("#")) { idx++; return null; }
        TreeNode node = new TreeNode(Integer.parseInt(parts[idx++]));
        node.left = build(parts); node.right = build(parts);
        return node;
    }
    public static void main(String[] args) {
        LC0297_SerializeDeserializeBinaryTree sol = new LC0297_SerializeDeserializeBinaryTree();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2); root.right = new TreeNode(3);
        root.right.left = new TreeNode(4); root.right.right = new TreeNode(5);
        String s = sol.serialize(root);
        System.out.println(s); // 1,2,#,#,3,4,#,#,5,#,#
        TreeNode rebuilt = sol.deserialize(s);
        System.out.println(sol.serialize(rebuilt));
    }
}
