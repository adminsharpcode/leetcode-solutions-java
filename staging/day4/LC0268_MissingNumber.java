public class LC0268_MissingNumber {
    public int missingNumber(int[] nums) {
        int n = nums.length, sum = n * (n + 1) / 2;
        for (int x : nums) sum -= x;
        return sum;
    }
    public static void main(String[] args) {
        LC0268_MissingNumber sol = new LC0268_MissingNumber();
        System.out.println(sol.missingNumber(new int[]{3,0,1})); // 2
        System.out.println(sol.missingNumber(new int[]{0,1})); // 2
    }
}
