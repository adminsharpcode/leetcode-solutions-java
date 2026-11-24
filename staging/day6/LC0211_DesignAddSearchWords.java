/**
 * Problem: 211. Design Add and Search Words Data Structure
 * Difficulty: Medium
 * Category: String, Depth-First Search, Design, Trie
 *
 * Algorithm:
 * Trie node array of 26 letters.
 * Wildcard '.' triggers recursive DFS across all valid non-null child nodes.
 *
 * Time Complexity: Add: O(M), Search: O(26^M) worst-case wildcard, O(M) without dots
 * Space Complexity: O(Total characters in words)
 */
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

    public boolean search(String word) {
        return dfs(root, word, 0);
    }

    private boolean dfs(TrieNode node, String word, int idx) {
        if (node == null) return false;
        if (idx == word.length()) return node.isEnd;

        char c = word.charAt(idx);
        if (c == '.') {
            for (TrieNode child : node.children) {
                if (dfs(child, word, idx + 1)) return true;
            }
            return false;
        }
        return dfs(node.children[c - 'a'], word, idx + 1);
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
