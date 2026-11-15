/**
 * Problem: 29. Divide Two Integers
 * Difficulty: Medium
 * Category: Math, Bit Manipulation
 *
 * Algorithm:
 * Exponential search using bitwise left-shifts: double the divisor (divisor << 1)
 * until it exceeds dividend, subtract, and accumulate shifted quotient count.
 * Handle overflow cases (Integer.MIN_VALUE / -1 = Integer.MAX_VALUE).
 *
 * Time Complexity: O(log^2(N)) or O(32)
 * Space Complexity: O(1)
 */
public class LC0029_DivideTwoIntegers {

    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        boolean negative = (dividend < 0) ^ (divisor < 0);
        long dvd = Math.abs((long) dividend);
        long dvs = Math.abs((long) divisor);
        long quotient = 0;

        while (dvd >= dvs) {
            long temp = dvs;
            long multiple = 1;
            while (dvd >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }
            dvd -= temp;
            quotient += multiple;
        }

        return (int) (negative ? -quotient : quotient);
    }

    public static void main(String[] args) {
        LC0029_DivideTwoIntegers solver = new LC0029_DivideTwoIntegers();
        assert solver.divide(10, 3) == 3;
        assert solver.divide(7, -3) == -2;
        System.out.println("LC0029_DivideTwoIntegers passed all tests!");
    }
}
