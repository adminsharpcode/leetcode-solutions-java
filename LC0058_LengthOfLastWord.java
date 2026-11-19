/**
 * Problem: 58. Length of Last Word
 * Difficulty: Easy
 * Category: String
 *
 * Algorithm:
 * Reverse scan: skip trailing spaces, then count characters until next space.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0058_LengthOfLastWord {

    public int lengthOfLastWord(String s) {
        int length = 0;
        int i = s.length() - 1;

        while (i >= 0 && s.charAt(i) == ' ') {
            i--;
        }

        while (i >= 0 && s.charAt(i) != ' ') {
            length++;
            i--;
        }
        return length;
    }

    public static void main(String[] args) {
        LC0058_LengthOfLastWord solver = new LC0058_LengthOfLastWord();
        assert solver.lengthOfLastWord("Hello World") == 5;
        assert solver.lengthOfLastWord("   fly me   to   the moon  ") == 4;
        System.out.println("LC0058_LengthOfLastWord passed all tests!");
    }
}
