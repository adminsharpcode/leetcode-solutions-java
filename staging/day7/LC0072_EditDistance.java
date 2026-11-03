/**
 * LeetCode 72: Edit Distance
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/edit-distance/
 *
 * Approach: 2D Space-Optimized Dynamic Programming (Levenshtein Distance)
 * Time Complexity: O(M * N)
 * Space Complexity: O(N)
 */
public class LC0072_EditDistance {

    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        int[] dp = new int[n + 1];

        for (int j = 0; j <= n; j++) {
            dp[j] = j;
        }

        for (int i = 1; i <= m; i++) {
            int prevDiagonal = dp[0];
            dp[0] = i;

            for (int j = 1; j <= n; j++) {
                int temp = dp[j];
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[j] = prevDiagonal;
                } else {
                    dp[j] = 1 + Math.min(prevDiagonal, Math.min(dp[j], dp[j - 1]));
                }
                prevDiagonal = temp;
            }
        }

        return dp[n];
    }

    public static void main(String[] args) {
        LC0072_EditDistance solver = new LC0072_EditDistance();
        System.out.println("Dist 'horse' -> 'ros': " + solver.minDistance("horse", "ros")); // Expected: 3
    }
}
