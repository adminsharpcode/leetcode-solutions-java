/**
 * LeetCode 424: Longest Repeating Character Replacement
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/longest-repeating-character-replacement/
 *
 * Approach: Sliding Window with Maximum Character Frequency Tracking
 * Time Complexity: O(N)
 * Space Complexity: O(1) (26 uppercase English letters)
 */
public class LC0424_LongestRepeatingCharacterReplacement {

    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int left = 0;
        int maxFrequency = 0;
        int maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            maxFrequency = Math.max(maxFrequency, ++count[s.charAt(right) - 'A']);

            // If window size minus max frequency > k, shrink window
            while ((right - left + 1) - maxFrequency > k) {
                count[s.charAt(left) - 'A']--;
                left++;
            }

            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }

    public static void main(String[] args) {
        LC0424_LongestRepeatingCharacterReplacement solver =
            new LC0424_LongestRepeatingCharacterReplacement();
        System.out.println("Result: " + solver.characterReplacement("AABABBA", 1)); // Expected: 4
    }
}
