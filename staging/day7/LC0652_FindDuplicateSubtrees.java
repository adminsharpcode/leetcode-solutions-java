import java.util.*;
public class LC0652_FindDuplicateSubtrees {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    Map<String, Integer> count = new HashMap<>();
    List<TreeNode> res = new ArrayList<>();
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        serialize(root); return res;
    }
    private String serialize(TreeNode node) {
        if (node == null) return "#";
        String key = node.val + "," + serialize(node.left) + "," + serialize(node.right);
        count.merge(key, 1, Integer::sum);
        if (count.get(key) == 2) res.add(node);
        return key;
    }
    public static void main(String[] args) {
        LC0652_FindDuplicateSubtrees sol = new LC0652_FindDuplicateSubtrees();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2); root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.right.left = new TreeNode(2); root.right.right = new TreeNode(4);
        root.right.left.left = new TreeNode(4);
        List<TreeNode> dups = sol.findDuplicateSubtrees(root);
        for (TreeNode n : dups) System.out.print(n.val + " "); // 2 4
    }
}
