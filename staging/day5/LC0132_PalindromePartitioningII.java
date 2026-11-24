/**
 * Problem: 132. Palindrome Partitioning II
 * Difficulty: Hard
 * Category: String, Dynamic Programming
 *
 * Algorithm:
 * Precompute palindrome table pal[i][j] where s[i..j] is palindrome.
 * dp[i] = min cuts for substring s[0..i].
 *
 * Time Complexity: O(N^2)
 * Space Complexity: O(N^2)
 */
public class LC0132_PalindromePartitioningII {

    public int minCut(String s) {
        int n = s.length();
        boolean[][] pal = new boolean[n][n];
        int[] dp = new int[n];

        for (int i = 0; i < n; i++) {
            dp[i] = i;
            for (int j = 0; j <= i; j++) {
                if (s.charAt(j) == s.charAt(i) && (i - j <= 2 || pal[j + 1][i - 1])) {
                    pal[j][i] = true;
                    dp[i] = (j == 0) ? 0 : Math.min(dp[i], dp[j - 1] + 1);
                }
            }
        }
        return dp[n - 1];
    }

    public static void main(String[] args) {
        LC0132_PalindromePartitioningII sol = new LC0132_PalindromePartitioningII();
        System.out.println(sol.minCut("aab")); // 1
    }
}
