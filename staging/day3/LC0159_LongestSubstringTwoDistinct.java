import java.util.*;
public class LC0159_LongestSubstringTwoDistinct {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int l = 0, max = 0;
        for (int r = 0; r < s.length(); r++) {
            map.merge(s.charAt(r), 1, Integer::sum);
            while (map.size() > 2) {
                char lc = s.charAt(l++);
                map.put(lc, map.get(lc) - 1);
                if (map.get(lc) == 0) map.remove(lc);
            }
            max = Math.max(max, r - l + 1);
        }
        return max;
    }
    public static void main(String[] args) {
        LC0159_LongestSubstringTwoDistinct sol = new LC0159_LongestSubstringTwoDistinct();
        System.out.println(sol.lengthOfLongestSubstringTwoDistinct("eceba")); // 3
        System.out.println(sol.lengthOfLongestSubstringTwoDistinct("ccaabbb")); // 5
    }
}
