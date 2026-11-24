public class LC0191_NumberOf1Bits {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) { count += n & 1; n >>>= 1; }
        return count;
    }
    public static void main(String[] args) {
        LC0191_NumberOf1Bits sol = new LC0191_NumberOf1Bits();
        System.out.println(sol.hammingWeight(11)); // 3
        System.out.println(sol.hammingWeight(128)); // 1
    }
}
