/**
 * Problem: 8. String to Integer (atoi)
 * Difficulty: Medium
 * Category: Strings, Math
 *
 * Algorithm:
 * 1. Discard leading whitespaces.
 * 2. Check for optional '+' or '-' sign.
 * 3. Read subsequent digits until first non-digit character.
 * 4. Clamp result within 32-bit signed integer range: [-2^31, 2^31 - 1].
 *
 * Time Complexity: O(N) where N is length of string
 * Space Complexity: O(1)
 */
public class LC0008_StringToIntegerAtoi {

    public int myAtoi(String s) {
        if (s == null || s.isEmpty()) return 0;

        int i = 0;
        int n = s.length();

        // 1. Skip leading whitespace
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }
        if (i == n) return 0;

        // 2. Check sign
        int sign = 1;
        char firstChar = s.charAt(i);
        if (firstChar == '+') {
            i++;
        } else if (firstChar == '-') {
            sign = -1;
            i++;
        }

        // 3. Convert digits with overflow detection
        int result = 0;
        int threshold = Integer.MAX_VALUE / 10;
        int remThreshold = Integer.MAX_VALUE % 10;

        while (i < n && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';

            // Check overflow before updating result
            if (result > threshold || (result == threshold && digit > remThreshold)) {
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }

            result = result * 10 + digit;
            i++;
        }

        return sign * result;
    }

    public static void main(String[] args) {
        LC0008_StringToIntegerAtoi solver = new LC0008_StringToIntegerAtoi();
        assert solver.myAtoi("42") == 42;
        assert solver.myAtoi("   -042") == -42;
        assert solver.myAtoi("1337c0d3") == 1337;
        assert solver.myAtoi("0-1") == 0;
        assert solver.myAtoi("words and 987") == 0;
        assert solver.myAtoi("-91283472332") == Integer.MIN_VALUE;
        System.out.println("LC0008_StringToIntegerAtoi passed all tests!");
    }
}
