/**
 * Problem: 231. Power of Two
 * Difficulty: Easy
 * Category: Math, Bit Manipulation, Recursion
 *
 * Algorithm:
 * A positive integer n is a power of 2 iff it has exactly one set bit: (n & (n - 1)) == 0.
 *
 * Time Complexity: O(1)
 * Space Complexity: O(1)
 */
public class LC0231_PowerOfTwo {

    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }

    public static void main(String[] args) {
        LC0231_PowerOfTwo sol = new LC0231_PowerOfTwo();
        System.out.println(sol.isPowerOfTwo(16)); // true
        System.out.println(sol.isPowerOfTwo(3));  // false
    }
}
