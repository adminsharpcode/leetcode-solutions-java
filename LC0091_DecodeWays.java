/**
 * LeetCode 91: Decode Ways
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/decode-ways/
 *
 * Approach: 1D Constant Space Dynamic Programming
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0091_DecodeWays {

    public int numDecodings(String s) {
        if (s == null || s.isEmpty() || s.charAt(0) == '0') {
            return 0;
        }

        int prev2 = 1; // dp[i - 2]
        int prev1 = 1; // dp[i - 1]

        for (int i = 1; i < s.length(); i++) {
            int current = 0;
            int singleDigit = s.charAt(i) - '0';
            int twoDigits = Integer.parseInt(s.substring(i - 1, i + 1));

            if (singleDigit >= 1) {
                current += prev1;
            }
            if (twoDigits >= 10 && twoDigits <= 26) {
                current += prev2;
            }

            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }

    public static void main(String[] args) {
        LC0091_DecodeWays solver = new LC0091_DecodeWays();
        System.out.println("Decodings '12': " + solver.numDecodings("12")); // Expected: 2 ("AB", "L")
        System.out.println("Decodings '226': " + solver.numDecodings("226")); // Expected: 3
    }
}
