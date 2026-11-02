import java.util.HashMap;
import java.util.Map;

/**
 * LeetCode 76: Minimum Window Substring
 * Difficulty: Hard
 * Link: https://leetcode.com/problems/minimum-window-substring/
 *
 * Approach: Sliding Window with Frequency Map
 * Time Complexity: O(S + T)
 * Space Complexity: O(S + T)
 */
public class LC0076_MinimumWindowSubstring {

    public String minWindow(String s, String t) {
        if (s == null || t == null || s.length() < t.length()) return "";

        Map<Character, Integer> dictT = new HashMap<>();
        for (char c : t.toCharArray()) {
            dictT.put(c, dictT.getOrDefault(c, 0) + 1);
        }

        int required = dictT.size();
        int left = 0, right = 0;
        int formed = 0;

        Map<Character, Integer> windowCounts = new HashMap<>();
        int[] ans = {-1, 0, 0}; // len, left, right

        while (right < s.length()) {
            char c = s.charAt(right);
            windowCounts.put(c, windowCounts.getOrDefault(c, 0) + 1);

            if (dictT.containsKey(c) && windowCounts.get(c).intValue() == dictT.get(c).intValue()) {
                formed++;
            }

            while (left <= right && formed == required) {
                c = s.charAt(left);
                if (ans[0] == -1 || (right - left + 1) < ans[0]) {
                    ans[0] = right - left + 1;
                    ans[1] = left;
                    ans[2] = right;
                }

                windowCounts.put(c, windowCounts.get(c) - 1);
                if (dictT.containsKey(c) && windowCounts.get(c).intValue() < dictT.get(c).intValue()) {
                    formed--;
                }
                left++;
            }
            right++;
        }

        return ans[0] == -1 ? "" : s.substring(ans[1], ans[2] + 1);
    }

    public static void main(String[] args) {
        LC0076_MinimumWindowSubstring solver = new LC0076_MinimumWindowSubstring();
        System.out.println("Result: " + solver.minWindow("ADOBECODEBANC", "ABC")); // Expected: "BANC"
    }
}
