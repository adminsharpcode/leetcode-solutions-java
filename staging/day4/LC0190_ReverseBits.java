public class LC0190_ReverseBits {
    public int reverseBits(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            res = (res << 1) | (n & 1);
            n >>= 1;
        }
        return res;
    }
    public static void main(String[] args) {
        LC0190_ReverseBits sol = new LC0190_ReverseBits();
        System.out.println(Integer.toBinaryString(sol.reverseBits(43261596))); // 964176192
    }
}
