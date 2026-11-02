import java.util.Arrays;

/**
 * LeetCode 238: Product of Array Except Self
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/product-of-array-except-self/
 *
 * Approach: Prefix & Suffix running products in O(1) auxiliary space
 * Time Complexity: O(N)
 * Space Complexity: O(1) auxiliary space (output array does not count toward memory)
 */
public class LC0238_ProductOfArrayExceptSelf {

    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];

        // Step 1: Compute prefix products in-place in result array
        result[0] = 1;
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }

        // Step 2: Compute suffix product on the fly and multiply with prefix
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= suffix;
            suffix *= nums[i];
        }

        return result;
    }

    public static void main(String[] args) {
        LC0238_ProductOfArrayExceptSelf solver = new LC0238_ProductOfArrayExceptSelf();

        int[] nums1 = {1, 2, 3, 4};
        System.out.println("Result 1: " + Arrays.toString(solver.productExceptSelf(nums1))); // Expected: [24, 12, 8, 6]

        int[] nums2 = {-1, 1, 0, -3, 3};
        System.out.println("Result 2: " + Arrays.toString(solver.productExceptSelf(nums2))); // Expected: [0, 0, 9, 0, 0]
    }
}
