public class LC0211_DesignAddSearchWords {
    private TrieNode root = new TrieNode();
    static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd;
    }
    public void addWord(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (cur.children[c - 'a'] == null) cur.children[c - 'a'] = new TrieNode();
            cur = cur.children[c - 'a'];
        }
        cur.isEnd = true;
    }
    public boolean search(String word) { return dfs(root, word, 0); }
    private boolean dfs(TrieNode node, String word, int i) {
        if (node == null) return false;
        if (i == word.length()) return node.isEnd;
        char c = word.charAt(i);
        if (c == '.') { for (TrieNode child : node.children) if (dfs(child, word, i + 1)) return true; return false; }
        return dfs(node.children[c - 'a'], word, i + 1);
    }
    public static void main(String[] args) {
        LC0211_DesignAddSearchWords sol = new LC0211_DesignAddSearchWords();
        sol.addWord("bad"); sol.addWord("dad"); sol.addWord("mad");
        System.out.println(sol.search("pad")); // false
        System.out.println(sol.search("bad")); // true
        System.out.println(sol.search(".ad")); // true
        System.out.println(sol.search("b..")); // true
    }
}
