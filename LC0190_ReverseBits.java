/**
 * Problem: 190. Reverse Bits
 * Difficulty: Easy
 * Category: Divide and Conquer, Bit Manipulation
 *
 * Algorithm:
 * Iterate 32 times: shift result left, append least significant bit of n, shift n right.
 *
 * Time Complexity: O(1) - exactly 32 bit operations
 * Space Complexity: O(1)
 */
public class LC0190_ReverseBits {

    public int reverseBits(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            res = (res << 1) | (n & 1);
            n >>= 1;
        }
        return res;
    }

    public static void main(String[] args) {
        LC0190_ReverseBits sol = new LC0190_ReverseBits();
        System.out.println(sol.reverseBits(43261596)); // 964176192
    }
}
