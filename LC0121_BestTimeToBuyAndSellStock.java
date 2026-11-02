/**
 * LeetCode 121: Best Time to Buy and Sell Stock
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 *
 * Approach: Single Pass One-way Min Tracking (Greedy)
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0121_BestTimeToBuyAndSellStock {

    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }

        return maxProfit;
    }

    public static void main(String[] args) {
        LC0121_BestTimeToBuyAndSellStock solver = new LC0121_BestTimeToBuyAndSellStock();
        int[] prices = {7, 1, 5, 3, 6, 4};
        System.out.println("Max Profit: " + solver.maxProfit(prices)); // Expected: 5 (buy at 1, sell at 6)
    }
}
