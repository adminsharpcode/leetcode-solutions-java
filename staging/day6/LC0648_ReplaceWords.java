import java.util.*;

/**
 * Problem: 648. Replace Words
 * Difficulty: Medium
 * Category: Array, Hash Table, String, Trie
 *
 * Algorithm:
 * Insert dictionary roots into Trie. For each sentence word, find shortest matching root.
 *
 * Time Complexity: O(Dict chars + Sentence chars)
 * Space Complexity: O(Dict chars)
 */
public class LC0648_ReplaceWords {

    static class Trie {
        Trie[] ch = new Trie[26];
        String rootWord;
    }

    public String replaceWords(List<String> dictionary, String sentence) {
        Trie root = new Trie();
        for (String word : dictionary) {
            Trie cur = root;
            for (char c : word.toCharArray()) {
                if (cur.ch[c - 'a'] == null) cur.ch[c - 'a'] = new Trie();
                cur = cur.ch[c - 'a'];
            }
            cur.rootWord = word;
        }

        StringBuilder sb = new StringBuilder();
        for (String word : sentence.split(" ")) {
            Trie cur = root;
            String replacement = null;
            for (char c : word.toCharArray()) {
                if (cur.ch[c - 'a'] == null || cur.rootWord != null) {
                    replacement = cur.rootWord;
                    break;
                }
                cur = cur.ch[c - 'a'];
            }
            if (replacement == null) replacement = word;
            if (sb.length() > 0) sb.append(' ');
            sb.append(replacement);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        LC0648_ReplaceWords sol = new LC0648_ReplaceWords();
        System.out.println(sol.replaceWords(Arrays.asList("cat","bat","rat"), "the cattle was rattled by the battery"));
    }
}
