/**
 * Problem: 567. Permutation in String
 * Difficulty: Medium
 * Category: Hash Table, Two Pointers, String, Sliding Window
 *
 * Algorithm:
 * Fixed-size sliding window of length s1.length() over s2.
 * Maintain 26-char frequency difference or match counter.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0567_PermutationInString {

    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;

        int[] count1 = new int[26];
        int[] count2 = new int[26];

        for (int i = 0; i < s1.length(); i++) {
            count1[s1.charAt(i) - 'a']++;
            count2[s2.charAt(i) - 'a']++;
        }

        if (matches(count1, count2)) return true;

        for (int i = s1.length(); i < s2.length(); i++) {
            count2[s2.charAt(i) - 'a']++;
            count2[s2.charAt(i - s1.length()) - 'a']--;
            if (matches(count1, count2)) return true;
        }
        return false;
    }

    private boolean matches(int[] c1, int[] c2) {
        for (int i = 0; i < 26; i++) {
            if (c1[i] != c2[i]) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        LC0567_PermutationInString sol = new LC0567_PermutationInString();
        System.out.println(sol.checkInclusion("ab", "eidbaooo")); // true
        System.out.println(sol.checkInclusion("ab", "eidboaoo")); // false
    }
}
