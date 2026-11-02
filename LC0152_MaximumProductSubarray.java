/**
 * LeetCode 152: Maximum Product Subarray
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/maximum-product-subarray/
 *
 * Approach: Dynamic Programming tracking running min and max products
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0152_MaximumProductSubarray {

    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int maxProd = nums[0];
        int minProd = nums[0];
        int globalMax = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];

            if (num < 0) {
                int temp = maxProd;
                maxProd = minProd;
                minProd = temp;
            }

            maxProd = Math.max(num, maxProd * num);
            minProd = Math.min(num, minProd * num);

            globalMax = Math.max(globalMax, maxProd);
        }

        return globalMax;
    }

    public static void main(String[] args) {
        LC0152_MaximumProductSubarray solver = new LC0152_MaximumProductSubarray();

        int[] nums1 = {2, 3, -2, 4};
        System.out.println("Max Product 1: " + solver.maxProduct(nums1)); // Expected: 6

        int[] nums2 = {-2, 0, -1};
        System.out.println("Max Product 2: " + solver.maxProduct(nums2)); // Expected: 0
    }
}
