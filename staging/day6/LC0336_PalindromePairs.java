import java.util.*;
public class LC0336_PalindromePairs {
    public List<List<Integer>> palindromePairs(String[] words) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < words.length; i++) map.put(words[i], i);
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j <= words[i].length(); j++) {
                String prefix = words[i].substring(0, j), suffix = words[i].substring(j);
                if (isPalin(prefix)) {
                    String revSuffix = new StringBuilder(suffix).reverse().toString();
                    Integer idx = map.get(revSuffix);
                    if (idx != null && idx != i) res.add(Arrays.asList(idx, i));
                }
                if (j > 0 && isPalin(suffix)) {
                    String revPrefix = new StringBuilder(prefix).reverse().toString();
                    Integer idx = map.get(revPrefix);
                    if (idx != null && idx != i) res.add(Arrays.asList(i, idx));
                }
            }
        }
        return res;
    }
    private boolean isPalin(String s) { int l=0,r=s.length()-1; while(l<r) if(s.charAt(l++)!=s.charAt(r--)) return false; return true; }
    public static void main(String[] args) {
        LC0336_PalindromePairs sol = new LC0336_PalindromePairs();
        System.out.println(sol.palindromePairs(new String[]{"abcd","dcba","lls","s","sssll"})); // [[0,1],[1,0],[3,2],[2,4]]
    }
}
