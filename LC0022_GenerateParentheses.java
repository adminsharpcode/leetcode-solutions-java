import java.util.ArrayList;
import java.util.List;

/**
 * LeetCode 22: Generate Parentheses
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/generate-parentheses/
 *
 * Approach: Backtracking with state pruning
 * Time Complexity: O(4^N / sqrt(N)) (N-th Catalan number)
 * Space Complexity: O(N)
 */
public class LC0022_GenerateParentheses {

    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result, new StringBuilder(), 0, 0, n);
        return result;
    }

    private void backtrack(List<String> result, StringBuilder sb, int open, int close, int max) {
        if (sb.length() == max * 2) {
            result.add(sb.toString());
            return;
        }

        if (open < max) {
            sb.append('(');
            backtrack(result, sb, open + 1, close, max);
            sb.deleteCharAt(sb.length() - 1);
        }

        if (close < open) {
            sb.append(')');
            backtrack(result, sb, open, close + 1, max);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    public static void main(String[] args) {
        LC0022_GenerateParentheses solver = new LC0022_GenerateParentheses();
        int n = 3;
        List<String> combinations = solver.generateParenthesis(n);
        System.out.println("Result for n=3: " + combinations);
        // Expected: ["((()))","(()())","(())()","()(())","()()()"]
    }
}
