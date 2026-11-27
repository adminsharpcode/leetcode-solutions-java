import java.util.*;

/**
 * Problem: 30. Substring with Concatenation of All Words
 * Difficulty: Hard
 * Category: Hash Table, String, Sliding Window
 *
 * Algorithm:
 * Word length is fixed L, total words C. Window length is L * C.
 * Slide window in steps of L across L possible starting offsets.
 *
 * Time Complexity: O(N * L)
 * Space Complexity: O(C * L)
 */
public class LC0030_SubstringConcatenation {

    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<>();
        if (s == null || words == null || words.length == 0) return res;

        int wordLen = words[0].length(), wordCount = words.length;
        int totalLen = wordLen * wordCount;
        if (s.length() < totalLen) return res;

        Map<String, Integer> wordFreq = new HashMap<>();
        for (String w : words) wordFreq.merge(w, 1, Integer::sum);

        for (int i = 0; i <= s.length() - totalLen; i++) {
            Map<String, Integer> seen = new HashMap<>();
            int j = 0;
            while (j < wordCount) {
                String sub = s.substring(i + j * wordLen, i + (j + 1) * wordLen);
                if (!wordFreq.containsKey(sub)) break;
                seen.merge(sub, 1, Integer::sum);
                if (seen.get(sub) > wordFreq.get(sub)) break;
                j++;
            }
            if (j == wordCount) res.add(i);
        }
        return res;
    }

    public static void main(String[] args) {
        LC0030_SubstringConcatenation sol = new LC0030_SubstringConcatenation();
        System.out.println(sol.findSubstring("barfoothefoobarman", new String[]{"foo", "bar"})); // [0, 9]
    }
}
