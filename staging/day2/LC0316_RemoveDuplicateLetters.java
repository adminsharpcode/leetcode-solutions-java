import java.util.*;
public class LC0316_RemoveDuplicateLetters {
    public String removeDuplicateLetters(String s) {
        int[] count = new int[26];
        boolean[] inStack = new boolean[26];
        for (char c : s.toCharArray()) count[c - 'a']++;
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            count[c - 'a']--;
            if (inStack[c - 'a']) continue;
            while (!stack.isEmpty() && stack.peek() > c && count[stack.peek() - 'a'] > 0) {
                inStack[stack.pop() - 'a'] = false;
            }
            stack.push(c);
            inStack[c - 'a'] = true;
        }
        StringBuilder sb = new StringBuilder();
        for (char c : stack) sb.append(c);
        return sb.reverse().toString();
    }
    public static void main(String[] args) {
        LC0316_RemoveDuplicateLetters sol = new LC0316_RemoveDuplicateLetters();
        System.out.println(sol.removeDuplicateLetters("bcabc")); // abc
        System.out.println(sol.removeDuplicateLetters("cbacdcbc")); // acdb
    }
}
