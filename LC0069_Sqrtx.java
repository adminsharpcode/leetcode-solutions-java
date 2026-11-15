/**
 * Problem: 69. Sqrt(x)
 * Difficulty: Easy
 * Category: Math, Binary Search
 *
 * Algorithm:
 * Binary Search on the range [1, x / 2] (or [0, x]):
 * Use division (mid <= x / mid) to prevent 32-bit integer overflow.
 *
 * Time Complexity: O(log x)
 * Space Complexity: O(1)
 */
public class LC0069_Sqrtx {

    public int mySqrt(int x) {
        if (x < 2) return x;

        int left = 1;
        int right = x / 2;
        int ans = 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // mid * mid <= x, using division to prevent overflow
            if (mid <= x / mid) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        LC0069_Sqrtx solver = new LC0069_Sqrtx();
        assert solver.mySqrt(4) == 2;
        assert solver.mySqrt(8) == 2;
        assert solver.mySqrt(0) == 0;
        assert solver.mySqrt(1) == 1;
        assert solver.mySqrt(2147395599) == 46339;
        assert solver.mySqrt(Integer.MAX_VALUE) == 46340;
        System.out.println("LC0069_Sqrtx passed all tests!");
    }
}
