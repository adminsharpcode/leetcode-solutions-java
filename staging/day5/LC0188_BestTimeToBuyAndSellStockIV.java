import java.util.*;

/**
 * Problem: 188. Best Time to Buy and Sell Stock IV
 * Difficulty: Hard
 * Category: Array, Dynamic Programming
 *
 * Algorithm:
 * State arrays buy[k] and sell[k].
 * If k >= n / 2, equivalent to unlimited transactions (greedy peak-valley).
 *
 * Time Complexity: O(k * N)
 * Space Complexity: O(k)
 */
public class LC0188_BestTimeToBuyAndSellStockIV {

    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if (n == 0 || k == 0) return 0;

        if (k >= n / 2) {
            int profit = 0;
            for (int i = 1; i < n; i++) {
                if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
            }
            return profit;
        }

        int[] buy = new int[k];
        int[] sell = new int[k];
        Arrays.fill(buy, Integer.MIN_VALUE);

        for (int p : prices) {
            for (int i = 0; i < k; i++) {
                buy[i] = Math.max(buy[i], (i == 0 ? 0 : sell[i - 1]) - p);
                sell[i] = Math.max(sell[i], buy[i] + p);
            }
        }
        return sell[k - 1];
    }

    public static void main(String[] args) {
        LC0188_BestTimeToBuyAndSellStockIV sol = new LC0188_BestTimeToBuyAndSellStockIV();
        System.out.println(sol.maxProfit(2, new int[]{2, 4, 1, 7})); // 9
    }
}
