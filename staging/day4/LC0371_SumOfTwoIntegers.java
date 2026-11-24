/**
 * Problem: 371. Sum of Two Integers
 * Difficulty: Medium
 * Category: Math, Bit Manipulation
 *
 * Algorithm:
 * Addition without +: sum = a ^ b, carry = (a & b) << 1.
 * Repeat until carry is 0.
 *
 * Time Complexity: O(1) - max 32 iterations
 * Space Complexity: O(1)
 */
public class LC0371_SumOfTwoIntegers {

    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }

    public static void main(String[] args) {
        LC0371_SumOfTwoIntegers sol = new LC0371_SumOfTwoIntegers();
        System.out.println(sol.getSum(1, 2)); // 3
        System.out.println(sol.getSum(2, 3)); // 5
    }
}
