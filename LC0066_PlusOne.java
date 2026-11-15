import java.util.Arrays;

/**
 * Problem: 66. Plus One
 * Difficulty: Easy
 * Category: Array, Math
 *
 * Algorithm:
 * Iterate from right to left:
 * 1. If digit < 9, increment and return immediately.
 * 2. If digit == 9, set to 0 and carry continues.
 * 3. If loop finishes, all digits were 9 (e.g. 999 -> 1000). Create array of size n+1, set index 0 to 1.
 *
 * Time Complexity: O(N) where N is number of digits
 * Space Complexity: O(1) in-place (or O(N) only if all digits are 9)
 */
public class LC0066_PlusOne {

    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        // All digits were 9, e.g. 99 -> 100
        int[] result = new int[n + 1];
        result[0] = 1;
        return result;
    }

    public static void main(String[] args) {
        LC0066_PlusOne solver = new LC0066_PlusOne();
        assert Arrays.equals(solver.plusOne(new int[]{1, 2, 3}), new int[]{1, 2, 4});
        assert Arrays.equals(solver.plusOne(new int[]{4, 3, 2, 1}), new int[]{4, 3, 2, 2});
        assert Arrays.equals(solver.plusOne(new int[]{9}), new int[]{1, 0});
        assert Arrays.equals(solver.plusOne(new int[]{9, 9, 9}), new int[]{1, 0, 0, 0});
        System.out.println("LC0066_PlusOne passed all tests!");
    }
}
