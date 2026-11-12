import java.util.ArrayList;
import java.util.List;

/**
 * LeetCode 17: Letter Combinations of a Phone Number
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 *
 * Approach: Backtracking with Digit-to-Letter Mapping
 * Time Complexity: O(4^N)
 * Space Complexity: O(N)
 */
public class LC0017_LetterCombinationsOfAPhoneNumber {

    private static final String[] MAPPINGS = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.isEmpty()) {
            return result;
        }

        backtrack(digits, 0, new StringBuilder(), result);
        return result;
    }

    private void backtrack(String digits, int index, StringBuilder sb, List<String> result) {
        if (index == digits.length()) {
            result.add(sb.toString());
            return;
        }

        String letters = MAPPINGS[digits.charAt(index) - '0'];
        for (int i = 0; i < letters.length(); i++) {
            sb.append(letters.charAt(i));
            backtrack(digits, index + 1, sb, result);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    public static void main(String[] args) {
        LC0017_LetterCombinationsOfAPhoneNumber solver =
            new LC0017_LetterCombinationsOfAPhoneNumber();
        System.out.println("Combinations for 23: " + solver.letterCombinations("23"));
        // Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    }
}
