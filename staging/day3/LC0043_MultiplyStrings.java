/**
 * Problem: 43. Multiply Strings
 * Difficulty: Medium
 * Category: Math, String, Simulation
 *
 * Algorithm:
 * Grade-school multiplication: result of num1[i] * num2[j] sits at indices [i + j, i + j + 1].
 *
 * Time Complexity: O(N * M)
 * Space Complexity: O(N + M)
 */
public class LC0043_MultiplyStrings {

    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) return "0";

        int n = num1.length();
        int m = num2.length();
        int[] pos = new int[n + m];

        for (int i = n - 1; i >= 0; i--) {
            int d1 = num1.charAt(i) - '0';
            for (int j = m - 1; j >= 0; j--) {
                int d2 = num2.charAt(j) - '0';
                int mul = d1 * d2;
                int p1 = i + j;
                int p2 = i + j + 1;
                int sum = mul + pos[p2];

                pos[p2] = sum % 10;
                pos[p1] += sum / 10;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int p : pos) {
            if (!(sb.length() == 0 && p == 0)) {
                sb.append(p);
            }
        }
        return sb.length() == 0 ? "0" : sb.toString();
    }

    public static void main(String[] args) {
        LC0043_MultiplyStrings solver = new LC0043_MultiplyStrings();
        assert solver.multiply("2", "3").equals("6");
        assert solver.multiply("123", "456").equals("56088");
        System.out.println("LC0043_MultiplyStrings passed all tests!");
    }
}
