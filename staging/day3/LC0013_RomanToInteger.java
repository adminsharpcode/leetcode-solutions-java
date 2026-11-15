import java.util.HashMap;
import java.util.Map;

/**
 * Problem: 13. Roman to Integer
 * Difficulty: Easy
 * Category: Hash Table, Math, String
 *
 * Algorithm:
 * Left-to-right scan: if current value < next value, subtract current value; otherwise add.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0013_RomanToInteger {

    public int romanToInt(String s) {
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        int total = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            int val = map.get(s.charAt(i));
            if (i < n - 1 && val < map.get(s.charAt(i + 1))) {
                total -= val;
            } else {
                total += val;
            }
        }
        return total;
    }

    public static void main(String[] args) {
        LC0013_RomanToInteger solver = new LC0013_RomanToInteger();
        assert solver.romanToInt("III") == 3;
        assert solver.romanToInt("LVIII") == 58;
        assert solver.romanToInt("MCMXCIV") == 1994;
        System.out.println("LC0013_RomanToInteger passed all tests!");
    }
}
