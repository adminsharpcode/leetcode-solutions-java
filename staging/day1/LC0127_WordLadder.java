import java.util.*;
public class LC0127_WordLadder {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);
        if (!wordSet.contains(endWord)) return 0;
        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        int level = 1;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String word = queue.poll();
                char[] chars = word.toCharArray();
                for (int j = 0; j < chars.length; j++) {
                    char orig = chars[j];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == orig) continue;
                        chars[j] = c;
                        String next = new String(chars);
                        if (next.equals(endWord)) return level + 1;
                        if (wordSet.remove(next)) queue.offer(next);
                    }
                    chars[j] = orig;
                }
            }
            level++;
        }
        return 0;
    }
    public static void main(String[] args) {
        LC0127_WordLadder sol = new LC0127_WordLadder();
        List<String> wl = Arrays.asList("hot","dot","dog","lot","log","cog");
        System.out.println(sol.ladderLength("hit", "cog", wl)); // 5
    }
}
