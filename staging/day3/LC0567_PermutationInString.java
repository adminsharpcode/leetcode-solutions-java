public class LC0567_PermutationInString {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;
        int[] freq = new int[26];
        for (char c : s1.toCharArray()) freq[c - 'a']++;
        int l = 0, matches = 0;
        int[] window = new int[26];
        for (int r = 0; r < s2.length(); r++) {
            window[s2.charAt(r) - 'a']++;
            if (window[s2.charAt(r) - 'a'] == freq[s2.charAt(r) - 'a']) matches++;
            if (r >= s1.length()) {
                if (window[s2.charAt(l) - 'a'] == freq[s2.charAt(l) - 'a']) matches--;
                window[s2.charAt(l++) - 'a']--;
            }
            if (matches == 26) return true;
        }
        return false;
    }
    public static void main(String[] args) {
        LC0567_PermutationInString sol = new LC0567_PermutationInString();
        System.out.println(sol.checkInclusion("ab", "eidbaooo")); // true
        System.out.println(sol.checkInclusion("ab", "eidboaoo")); // false
    }
}
