import java.util.ArrayList;
import java.util.List;

/**
 * Problem: 6. Zigzag Conversion
 * Difficulty: Medium
 * Category: String
 *
 * Algorithm:
 * Simulate writing across numRows string builders, tracking direction (goingDown).
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0006_ZigzagConversion {

    public String convert(String s, int numRows) {
        if (numRows == 1 || s.length() <= numRows) return s;

        List<StringBuilder> rows = new ArrayList<>();
        for (int i = 0; i < numRows; i++) rows.add(new StringBuilder());

        int curRow = 0;
        boolean goingDown = false;

        for (char c : s.toCharArray()) {
            rows.get(curRow).append(c);
            if (curRow == 0 || curRow == numRows - 1) {
                goingDown = !goingDown;
            }
            curRow += goingDown ? 1 : -1;
        }

        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) result.append(row);
        return result.toString();
    }

    public static void main(String[] args) {
        LC0006_ZigzagConversion solver = new LC0006_ZigzagConversion();
        assert solver.convert("PAYPALISHIRING", 3).equals("PAHNAPLSIIGYIR");
        System.out.println("LC0006_ZigzagConversion passed all tests!");
    }
}
