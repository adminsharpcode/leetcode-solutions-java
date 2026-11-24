/**
 * Problem: 191. Number of 1 Bits
 * Difficulty: Easy
 * Category: Divide and Conquer, Bit Manipulation
 *
 * Algorithm:
 * Brian Kernighan's Algorithm: n = n & (n - 1) flips the lowest set bit to 0.
 *
 * Time Complexity: O(k) where k is the number of 1-bits (<= 32)
 * Space Complexity: O(1)
 */
public class LC0191_NumberOf1Bits {

    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        LC0191_NumberOf1Bits sol = new LC0191_NumberOf1Bits();
        System.out.println(sol.hammingWeight(11));  // 3
        System.out.println(sol.hammingWeight(128)); // 1
    }
}
