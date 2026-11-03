import java.util.ArrayDeque;
import java.util.Deque;

/**
 * LeetCode 150: Evaluate Reverse Polish Notation
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
 *
 * Approach: Stack-Based Operand Evaluation
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0150_EvaluateReversePolishNotation {

    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();

        for (String token : tokens) {
            if (token.equals("+")) {
                stack.push(stack.pop() + stack.pop());
            } else if (token.equals("-")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a - b);
            } else if (token.equals("*")) {
                stack.push(stack.pop() * stack.pop());
            } else if (token.equals("/")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a / b);
            } else {
                stack.push(Integer.parseInt(token));
            }
        }

        return stack.pop();
    }

    public static void main(String[] args) {
        LC0150_EvaluateReversePolishNotation solver = new LC0150_EvaluateReversePolishNotation();
        String[] tokens = {"2", "1", "+", "3", "*"};
        System.out.println("Result: " + solver.evalRPN(tokens)); // Expected: 9
    }
}
