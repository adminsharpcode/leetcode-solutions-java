import java.util.*;
public class LC0472_ConcatenatedWords {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Set<String> wordSet = new HashSet<>(Arrays.asList(words));
        List<String> res = new ArrayList<>();
        for (String word : words) {
            int n = word.length();
            boolean[] dp = new boolean[n + 1];
            dp[0] = true;
            for (int i = 1; i <= n; i++)
                for (int j = 0; j < i; j++)
                    if (dp[j] && wordSet.contains(word.substring(j, i)) && !(j == 0 && i == n)) { dp[i] = true; break; }
            if (dp[n]) res.add(word);
        }
        return res;
    }
    public static void main(String[] args) {
        LC0472_ConcatenatedWords sol = new LC0472_ConcatenatedWords();
        System.out.println(sol.findAllConcatenatedWordsInADict(new String[]{"cat","cats","catsdogcats","dog","dogcatsdog","hippodogcats","rat"}));
    }
}
