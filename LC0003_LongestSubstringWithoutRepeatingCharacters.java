import java.util.HashMap;
import java.util.Map;

/**
 * LeetCode 3: Longest Substring Without Repeating Characters
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 *
 * Approach: Sliding Window with Hash Map
 * Time Complexity: O(N)
 * Space Complexity: O(min(N, M)) where M is alphabet size
 */
public class LC0003_LongestSubstringWithoutRepeatingCharacters {

    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int maxLen = 0;
        Map<Character, Integer> lastSeen = new HashMap<>();

        for (int left = 0, right = 0; right < n; right++) {
            char c = s.charAt(right);
            if (lastSeen.containsKey(c)) {
                left = Math.max(left, lastSeen.get(c) + 1);
            }
            lastSeen.put(c, right);
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }

    public static void main(String[] args) {
        LC0003_LongestSubstringWithoutRepeatingCharacters solver = new LC0003_LongestSubstringWithoutRepeatingCharacters();
        System.out.println("abcabcbb: " + solver.lengthOfLongestSubstring("abcabcbb")); // Expected: 3
        System.out.println("bbbbb: " + solver.lengthOfLongestSubstring("bbbbb"));       // Expected: 1
        System.out.println("pwwkew: " + solver.lengthOfLongestSubstring("pwwkew"));     // Expected: 3
    }
}
