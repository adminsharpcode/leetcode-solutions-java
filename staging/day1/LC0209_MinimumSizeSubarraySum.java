/**
 * Problem: 209. Minimum Size Subarray Sum
 * Difficulty: Medium
 * Category: Array, Binary Search, Sliding Window
 *
 * Algorithm:
 * Sliding window: expand right pointer until sum >= target, then shrink left pointer
 * while maintaining sum >= target, tracking the minimum window length.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0209_MinimumSizeSubarraySum {

    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int sum = 0;
        int minLen = Integer.MAX_VALUE;

        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];

            while (sum >= target) {
                minLen = Math.min(minLen, right - left + 1);
                sum -= nums[left++];
            }
        }
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }

    public static void main(String[] args) {
        LC0209_MinimumSizeSubarraySum solver = new LC0209_MinimumSizeSubarraySum();
        int[] nums = {2, 3, 1, 2, 4, 3};
        assert solver.minSubArrayLen(7, nums) == 2;
        System.out.println("LC0209_MinimumSizeSubarraySum passed all tests!");
    }
}
