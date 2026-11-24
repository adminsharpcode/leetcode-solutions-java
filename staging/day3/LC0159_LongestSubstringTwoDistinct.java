import java.util.*;

/**
 * Problem: 159. Longest Substring with At Most Two Distinct Characters
 * Difficulty: Medium
 * Category: Hash Table, String, Sliding Window
 *
 * Algorithm:
 * Sliding window maintaining character frequency map.
 * Expand right pointer; shrink left pointer whenever map.size() > 2.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0159_LongestSubstringTwoDistinct {

    public int lengthOfLongestSubstringTwoDistinct(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int left = 0, maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            map.merge(s.charAt(right), 1, Integer::sum);
            while (map.size() > 2) {
                char lc = s.charAt(left++);
                map.put(lc, map.get(lc) - 1);
                if (map.get(lc) == 0) map.remove(lc);
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }

    public static void main(String[] args) {
        LC0159_LongestSubstringTwoDistinct sol = new LC0159_LongestSubstringTwoDistinct();
        System.out.println(sol.lengthOfLongestSubstringTwoDistinct("eceba")); // 3 ("ece")
    }
}
