import java.util.*;

/**
 * Problem: 212. Word Search II
 * Difficulty: Hard
 * Category: Array, String, Backtracking, Trie, Matrix
 *
 * Algorithm:
 * Build Trie from word list. DFS board matching letters along Trie path.
 * In-place grid marking prevents duplicate visits during single search.
 *
 * Time Complexity: O(M * N * 4^(max_word_len))
 * Space Complexity: O(Trie nodes)
 */
public class LC0212_WordSearchII {

    static class Trie {
        Trie[] ch = new Trie[26];
        String word;
    }

    public List<String> findWords(char[][] board, String[] words) {
        Trie root = new Trie();
        for (String w : words) {
            Trie cur = root;
            for (char c : w.toCharArray()) {
                if (cur.ch[c - 'a'] == null) cur.ch[c - 'a'] = new Trie();
                cur = cur.ch[c - 'a'];
            }
            cur.word = w;
        }

        List<String> res = new ArrayList<>();
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                dfs(board, i, j, root, res);
            }
        }
        return res;
    }

    private void dfs(char[][] b, int r, int c, Trie node, List<String> res) {
        if (r < 0 || r >= b.length || c < 0 || c >= b[0].length || b[r][c] == '#') return;
        char orig = b[r][c];
        if (node.ch[orig - 'a'] == null) return;

        node = node.ch[orig - 'a'];
        if (node.word != null) {
            res.add(node.word);
            node.word = null;
        }

        b[r][c] = '#';
        dfs(b, r + 1, c, node, res);
        dfs(b, r - 1, c, node, res);
        dfs(b, r, c + 1, node, res);
        dfs(b, r, c - 1, node, res);
        b[r][c] = orig;
    }

    public static void main(String[] args) {
        LC0212_WordSearchII sol = new LC0212_WordSearchII();
        char[][] board = {
            {'o','a','a','n'},
            {'e','t','a','e'},
            {'i','h','k','r'},
            {'i','f','l','v'}
        };
        System.out.println(sol.findWords(board, new String[]{"oath","pea","eat","rain"})); // [oath, eat]
    }
}
