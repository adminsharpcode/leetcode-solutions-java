/**
 * Problem: 268. Missing Number
 * Difficulty: Easy
 * Category: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
 *
 * Algorithm:
 * Expected sum from 0..n is n * (n + 1) / 2.
 * Missing number = expected_sum - actual_sum.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0268_MissingNumber {

    public int missingNumber(int[] nums) {
        int n = nums.length;
        int expected = n * (n + 1) / 2;
        for (int num : nums) expected -= num;
        return expected;
    }

    public static void main(String[] args) {
        LC0268_MissingNumber sol = new LC0268_MissingNumber();
        System.out.println(sol.missingNumber(new int[]{3, 0, 1})); // 2
        System.out.println(sol.missingNumber(new int[]{0, 1}));    // 2
    }
}
