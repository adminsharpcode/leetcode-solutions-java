import java.util.ArrayDeque;
import java.util.Deque;

/**
 * LeetCode 20: Valid Parentheses
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/valid-parentheses/
 *
 * Approach: Stack / ArrayDeque
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0020_ValidParentheses {

    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(')');
            } else if (c == '{') {
                stack.push('}');
            } else if (c == '[') {
                stack.push(']');
            } else if (stack.isEmpty() || stack.pop() != c) {
                return false;
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        LC0020_ValidParentheses solver = new LC0020_ValidParentheses();
        System.out.println("()[]{}: " + solver.isValid("()[]{}")); // Expected: true
        System.out.println("(]: " + solver.isValid("(]"));         // Expected: false
        System.out.println("([)]: " + solver.isValid("([)]"));     // Expected: false
    }
}
