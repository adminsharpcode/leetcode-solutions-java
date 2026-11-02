import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * LeetCode 139: Word Break
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/word-break/
 *
 * Approach: 1D Dynamic Programming with HashSet
 * Time Complexity: O(N^3) (string substring hashing)
 * Space Complexity: O(N + M)
 */
public class LC0139_WordBreak {

    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> set = new HashSet<>(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && set.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.length()];
    }

    public static void main(String[] args) {
        LC0139_WordBreak solver = new LC0139_WordBreak();
        System.out.println("leetcode -> " + solver.wordBreak("leetcode", Arrays.asList("leet", "code"))); // Expected: true
        System.out.println("catsandog -> " + solver.wordBreak("catsandog", Arrays.asList("cats", "dog", "sand", "and", "cat"))); // Expected: false
    }
}
