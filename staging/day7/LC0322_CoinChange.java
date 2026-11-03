import java.util.Arrays;

/**
 * LeetCode 322: Coin Change
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/coin-change/
 *
 * Approach: Bottom-up 1D Dynamic Programming (Unbounded Knapsack)
 * Time Complexity: O(Amount * Coins.length)
 * Space Complexity: O(Amount)
 */
public class LC0322_CoinChange {

    public int coinChange(int[] coins, int amount) {
        int max = amount + 1;
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, max);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }

    public static void main(String[] args) {
        LC0322_CoinChange solver = new LC0322_CoinChange();
        int[] coins = {1, 2, 5};
        System.out.println("Min coins for 11: " + solver.coinChange(coins, 11)); // Expected: 3 (5 + 5 + 1)
    }
}
