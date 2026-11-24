/**
 * Problem: 115. Distinct Subsequences
 * Difficulty: Hard
 * Category: String, Dynamic Programming
 *
 * Algorithm:
 * dp[i][j] = count of distinct subsequences of s[0..i-1] matching t[0..j-1].
 * If s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j].
 * Else: dp[i][j] = dp[i-1][j].
 *
 * Time Complexity: O(M * N)
 * Space Complexity: O(M * N)
 */
public class LC0115_DistinctSubsequences {

    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        long[][] dp = new long[m + 1][n + 1];

        for (int i = 0; i <= m; i++) dp[i][0] = 1;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = dp[i - 1][j];
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    dp[i][j] += dp[i - 1][j - 1];
                }
            }
        }
        return (int) dp[m][n];
    }

    public static void main(String[] args) {
        LC0115_DistinctSubsequences sol = new LC0115_DistinctSubsequences();
        System.out.println(sol.numDistinct("rabbbit", "rabbit")); // 3
    }
}
