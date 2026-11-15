/**
 * Problem: 14. Longest Common Prefix
 * Difficulty: Easy
 * Category: Strings
 *
 * Algorithm:
 * 1. Start with the first string as the prefix candidate.
 * 2. Compare with each string in the array, shortening prefix until it matches the beginning of the string.
 * 3. If prefix becomes empty, return "".
 *
 * Time Complexity: O(S) where S is the sum of all characters in strings
 * Space Complexity: O(1)
 */
public class LC0014_LongestCommonPrefix {

    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++) {
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }
        }
        return prefix;
    }

    public static void main(String[] args) {
        LC0014_LongestCommonPrefix solver = new LC0014_LongestCommonPrefix();
        String[] test1 = {"flower", "flow", "flight"};
        assert solver.longestCommonPrefix(test1).equals("fl");

        String[] test2 = {"dog", "racecar", "car"};
        assert solver.longestCommonPrefix(test2).equals("");

        String[] test3 = {"interspecies", "interstellar", "interstate"};
        assert solver.longestCommonPrefix(test3).equals("inters");

        System.out.println("LC0014_LongestCommonPrefix passed all tests!");
    }
}
