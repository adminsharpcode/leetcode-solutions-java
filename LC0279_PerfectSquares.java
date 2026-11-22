import java.util.Arrays;

/**
 * Problem: 279. Perfect Squares
 * Difficulty: Medium
 * Category: Math, Dynamic Programming, Breadth-First Search
 *
 * Algorithm:
 * DP: dp[i] = min(dp[i - j * j] + 1) for all j * j <= i.
 * Base case dp[0] = 0.
 *
 * Time Complexity: O(N * sqrt(N))
 * Space Complexity: O(N)
 */
public class LC0279_PerfectSquares {

    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j * j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        LC0279_PerfectSquares solver = new LC0279_PerfectSquares();
        assert solver.numSquares(12) == 3; // 4 + 4 + 4
        assert solver.numSquares(13) == 2; // 4 + 9
        System.out.println("LC0279_PerfectSquares passed all tests!");
    }
}
