import java.util.*;
public class LC0030_SubstringConcatenation {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<>();
        if (s == null || words == null || words.length == 0) return res;
        int wordLen = words[0].length(), wordCount = words.length;
        int totalLen = wordLen * wordCount;
        Map<String, Integer> freq = new HashMap<>();
        for (String w : words) freq.merge(w, 1, Integer::sum);
        for (int i = 0; i <= s.length() - totalLen; i++) {
            Map<String, Integer> seen = new HashMap<>();
            int j = 0;
            while (j < wordCount) {
                String word = s.substring(i + j * wordLen, i + (j + 1) * wordLen);
                if (!freq.containsKey(word)) break;
                seen.merge(word, 1, Integer::sum);
                if (seen.get(word) > freq.get(word)) break;
                j++;
            }
            if (j == wordCount) res.add(i);
        }
        return res;
    }
    public static void main(String[] args) {
        LC0030_SubstringConcatenation sol = new LC0030_SubstringConcatenation();
        System.out.println(sol.findSubstring("barfoothefoobarman", new String[]{"foo","bar"})); // [0, 9]
    }
}
