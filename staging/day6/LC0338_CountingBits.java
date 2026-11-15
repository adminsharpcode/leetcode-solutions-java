import java.util.Arrays;

/**
 * Problem: 338. Counting Bits
 * Difficulty: Easy
 * Category: Dynamic Programming, Bit Manipulation
 *
 * Algorithm:
 * DP transition: dp[i] = dp[i >> 1] + (i & 1).
 * The number of set bits in i equals set bits in (i / 2) plus lowest bit.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1) auxiliary (excluding output array)
 */
public class LC0338_CountingBits {

    public int[] countBits(int n) {
        int[] ans = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            ans[i] = ans[i >> 1] + (i & 1);
        }
        return ans;
    }

    public static void main(String[] args) {
        LC0338_CountingBits solver = new LC0338_CountingBits();
        int[] res = solver.countBits(5);
        assert Arrays.equals(res, new int[]{0, 1, 1, 2, 1, 2});
        System.out.println("LC0338_CountingBits passed all tests!");
    }
}
