/**
 * Problem: 12. Integer to Roman
 * Difficulty: Medium
 * Category: Hash Table, Math, String
 *
 * Algorithm:
 * Greedy value extraction using ordered symbol/value tables.
 *
 * Time Complexity: O(1) bounded by 3999
 * Space Complexity: O(1)
 */
public class LC0012_IntegerToRoman {

    private static final int[] VALUES = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    private static final String[] SYMBOLS = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    public String intToRoman(int num) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < VALUES.length && num > 0; i++) {
            while (num >= VALUES[i]) {
                num -= VALUES[i];
                sb.append(SYMBOLS[i]);
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        LC0012_IntegerToRoman solver = new LC0012_IntegerToRoman();
        assert solver.intToRoman(3749).equals("MMMDCCXLIX");
        assert solver.intToRoman(58).equals("LVIII");
        System.out.println("LC0012_IntegerToRoman passed all tests!");
    }
}
