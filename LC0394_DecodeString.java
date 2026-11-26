import java.util.*;

/**
 * Problem: 394. Decode String
 * Difficulty: Medium
 * Category: String, Stack, Recursion
 *
 * Algorithm:
 * Two stacks: one for counts k, one for intermediate StringBuilders.
 * On '[', push current string and multiplier. On ']', pop multiplier and repeat buffer.
 *
 * Time Complexity: O(maxK * N)
 * Space Complexity: O(N)
 */
public class LC0394_DecodeString {

    public String decodeString(String s) {
        Deque<Integer> countStack = new ArrayDeque<>();
        Deque<StringBuilder> strStack = new ArrayDeque<>();
        StringBuilder current = new StringBuilder();
        int k = 0;

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                k = k * 10 + (c - '0');
            } else if (c == '[') {
                countStack.push(k);
                strStack.push(current);
                current = new StringBuilder();
                k = 0;
            } else if (c == ']') {
                StringBuilder decoded = current;
                current = strStack.pop();
                int repeat = countStack.pop();
                while (repeat-- > 0) current.append(decoded);
            } else {
                current.append(c);
            }
        }
        return current.toString();
    }

    public static void main(String[] args) {
        LC0394_DecodeString sol = new LC0394_DecodeString();
        System.out.println(sol.decodeString("3[a]2[bc]")); // aaabcbc
        System.out.println(sol.decodeString("3[a2[c]]"));  // accaccacc
    }
}
