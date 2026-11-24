import java.util.*;

/**
 * Problem: 472. Concatenated Words
 * Difficulty: Hard
 * Category: Array, String, Dynamic Programming, Depth-First Search, Trie
 *
 * Algorithm:
 * HashSet word dictionary. For each word, test if formable from >= 2 shorter words via 1D DP.
 *
 * Time Complexity: O(N * L^2)
 * Space Complexity: O(N * L)
 */
public class LC0472_ConcatenatedWords {

    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Set<String> set = new HashSet<>(Arrays.asList(words));
        List<String> res = new ArrayList<>();

        for (String w : words) {
            int len = w.length();
            if (len == 0) continue;
            boolean[] dp = new boolean[len + 1];
            dp[0] = true;

            for (int i = 1; i <= len; i++) {
                for (int j = 0; j < i; j++) {
                    if (dp[j] && set.contains(w.substring(j, i)) && !(j == 0 && i == len)) {
                        dp[i] = true;
                        break;
                    }
                }
            }
            if (dp[len]) res.add(w);
        }
        return res;
    }

    public static void main(String[] args) {
        LC0472_ConcatenatedWords sol = new LC0472_ConcatenatedWords();
        String[] words = {"cat","cats","catsdogcats","dog","dogcatsdog","hippodogcats","rat"};
        System.out.println(sol.findAllConcatenatedWordsInADict(words));
    }
}
