/**
 * LeetCode 208: Implement Trie (Prefix Tree)
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/implement-trie-prefix-tree/
 *
 * Approach: 26-ary Trie Node Tree
 * Time Complexity: O(L) for insert, search, and startsWith (L = word length)
 * Space Complexity: O(Total inserted characters * 26)
 */
public class LC0208_ImplementTrie {

    private static class TrieNode {
        TrieNode[] children;
        boolean isEndOfWord;

        public TrieNode() {
            children = new TrieNode[26];
            isEndOfWord = false;
        }
    }

    private final TrieNode root;

    public LC0208_ImplementTrie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode curr = root;
        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - 'a';
            if (curr.children[idx] == null) {
                curr.children[idx] = new TrieNode();
            }
            curr = curr.children[idx];
        }
        curr.isEndOfWord = true;
    }

    public boolean search(String word) {
        TrieNode node = findPrefixNode(word);
        return node != null && node.isEndOfWord;
    }

    public boolean startsWith(String prefix) {
        return findPrefixNode(prefix) != null;
    }

    private TrieNode findPrefixNode(String prefix) {
        TrieNode curr = root;
        for (int i = 0; i < prefix.length(); i++) {
            int idx = prefix.charAt(i) - 'a';
            if (curr.children[idx] == null) {
                return null;
            }
            curr = curr.children[idx];
        }
        return curr;
    }

    public static void main(String[] args) {
        LC0208_ImplementTrie trie = new LC0208_ImplementTrie();
        trie.insert("apple");

        System.out.println("Search 'apple': " + trie.search("apple"));     // Expected: true
        System.out.println("Search 'app': " + trie.search("app"));         // Expected: false
        System.out.println("StartsWith 'app': " + trie.startsWith("app")); // Expected: true

        trie.insert("app");
        System.out.println("Search 'app' after insert: " + trie.search("app")); // Expected: true
    }
}
