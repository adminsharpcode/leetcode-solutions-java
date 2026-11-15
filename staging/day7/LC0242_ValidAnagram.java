/**
 * Problem: 242. Valid Anagram
 * Difficulty: Easy
 * Category: Hash Table, String, Sorting
 *
 * Algorithm:
 * Frequency array of size 26 for lowercase English letters.
 * Increment for s, decrement for t; all counts must end at zero.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1) (fixed 26-element array)
 */
public class LC0242_ValidAnagram {

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        for (int c : count) {
            if (c != 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        LC0242_ValidAnagram solver = new LC0242_ValidAnagram();
        assert solver.isAnagram("anagram", "nagaram");
        assert !solver.isAnagram("rat", "car");
        System.out.println("LC0242_ValidAnagram passed all tests!");
    }
}
