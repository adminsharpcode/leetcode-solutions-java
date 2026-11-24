/**
 * Problem: 309. Best Time to Buy and Sell Stock with Cooldown
 * Difficulty: Medium
 * Category: Array, Dynamic Programming
 *
 * Algorithm:
 * Three states: held, sold (must rest tomorrow), rest.
 * Transitions: held = max(held, rest - price), sold = held + price, rest = max(rest, sold_prev).
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0309_BestTimeCooldown {

    public int maxProfit(int[] prices) {
        if (prices == null || prices.length < 2) return 0;

        int held = -prices[0], sold = 0, rest = 0;
        for (int i = 1; i < prices.length; i++) {
            int prevHeld = held;
            int prevSold = sold;
            int prevRest = rest;

            held = Math.max(prevHeld, prevRest - prices[i]);
            sold = prevHeld + prices[i];
            rest = Math.max(prevRest, prevSold);
        }
        return Math.max(sold, rest);
    }

    public static void main(String[] args) {
        LC0309_BestTimeCooldown sol = new LC0309_BestTimeCooldown();
        System.out.println(sol.maxProfit(new int[]{1, 2, 3, 0, 2})); // 3
    }
}
