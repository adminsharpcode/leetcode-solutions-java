public class LC0371_SumOfTwoIntegers {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }
    public static void main(String[] args) {
        LC0371_SumOfTwoIntegers sol = new LC0371_SumOfTwoIntegers();
        System.out.println(sol.getSum(1, 2)); // 3
        System.out.println(sol.getSum(2, 3)); // 5
    }
}
