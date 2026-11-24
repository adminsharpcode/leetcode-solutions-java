public class LC0309_BestTimeCooldown {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) return 0;
        int held = -prices[0], sold = 0, rest = 0;
        for (int i = 1; i < prices.length; i++) {
            int prevHeld = held, prevSold = sold, prevRest = rest;
            held = Math.max(prevHeld, prevRest - prices[i]);
            sold = prevHeld + prices[i];
            rest = Math.max(prevRest, prevSold);
        }
        return Math.max(sold, rest);
    }
    public static void main(String[] args) {
        LC0309_BestTimeCooldown sol = new LC0309_BestTimeCooldown();
        System.out.println(sol.maxProfit(new int[]{1,2,3,0,2})); // 3
    }
}
