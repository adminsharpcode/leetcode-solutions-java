import java.util.*;
public class LC0394_DecodeString {
    public String decodeString(String s) {
        Deque<Integer> countStack = new ArrayDeque<>();
        Deque<StringBuilder> strStack = new ArrayDeque<>();
        StringBuilder current = new StringBuilder();
        int k = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) { k = k * 10 + (c - '0'); }
            else if (c == '[') { countStack.push(k); k = 0; strStack.push(current); current = new StringBuilder(); }
            else if (c == ']') { StringBuilder tmp = current; current = strStack.pop(); int times = countStack.pop(); while (times-- > 0) current.append(tmp); }
            else current.append(c);
        }
        return current.toString();
    }
    public static void main(String[] args) {
        LC0394_DecodeString sol = new LC0394_DecodeString();
        System.out.println(sol.decodeString("3[a]2[bc]")); // aaabcbc
        System.out.println(sol.decodeString("3[a2[c]]")); // accaccacc
    }
}
