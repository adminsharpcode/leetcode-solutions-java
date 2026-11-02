/**
 * LeetCode 153: Find Minimum in Rotated Sorted Array
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
 *
 * Approach: Binary Search comparing mid with right boundary
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */
public class LC0153_FindMinimumInRotatedSortedArray {

    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[right]) {
                // Minimum is strictly in the right subarray
                left = mid + 1;
            } else {
                // Minimum is at mid or in the left subarray
                right = mid;
            }
        }

        return nums[left];
    }

    public static void main(String[] args) {
        LC0153_FindMinimumInRotatedSortedArray solver = new LC0153_FindMinimumInRotatedSortedArray();

        int[] nums1 = {3, 4, 5, 1, 2};
        System.out.println("Min 1: " + solver.findMin(nums1)); // Expected: 1

        int[] nums2 = {4, 5, 6, 7, 0, 1, 2};
        System.out.println("Min 2: " + solver.findMin(nums2)); // Expected: 0

        int[] nums3 = {11, 13, 15, 17};
        System.out.println("Min 3: " + solver.findMin(nums3)); // Expected: 11
    }
}
