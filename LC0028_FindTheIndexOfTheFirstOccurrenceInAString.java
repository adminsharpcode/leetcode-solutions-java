/**
 * Problem: 28. Find the Index of the First Occurrence in a String
 * Difficulty: Easy
 * Category: Strings, Two Pointers, String Matching (KMP)
 *
 * Algorithm:
 * Standard Knuth-Morris-Pratt (KMP) linear time pattern matching:
 * 1. Precompute Longest Prefix Suffix (LPS) array for needle.
 * 2. Scan haystack using LPS array to avoid redundant backtracking.
 *
 * Time Complexity: O(N + M) where N = haystack.length(), M = needle.length()
 * Space Complexity: O(M) for LPS array
 */
public class LC0028_FindTheIndexOfTheFirstOccurrenceInAString {

    public int strStr(String haystack, String needle) {
        if (needle.isEmpty()) return 0;
        if (haystack.length() < needle.length()) return -1;

        // Build LPS table
        int[] lps = buildLPS(needle);
        int i = 0; // index for haystack
        int j = 0; // index for needle

        while (i < haystack.length()) {
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
                if (j == needle.length()) {
                    return i - j; // match found
                }
            } else {
                if (j > 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return -1;
    }

    private int[] buildLPS(String needle) {
        int[] lps = new int[needle.length()];
        int len = 0;
        int i = 1;

        while (i < needle.length()) {
            if (needle.charAt(i) == needle.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len > 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }

    public static void main(String[] args) {
        LC0028_FindTheIndexOfTheFirstOccurrenceInAString solver = new LC0028_FindTheIndexOfTheFirstOccurrenceInAString();
        assert solver.strStr("sadbutsad", "sad") == 0;
        assert solver.strStr("leetcode", "leeto") == -1;
        assert solver.strStr("mississippi", "issip") == 4;
        System.out.println("LC0028_FindTheIndexOfTheFirstOccurrenceInAString passed all tests!");
    }
}
