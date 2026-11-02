/**
 * LeetCode 33: Search in Rotated Sorted Array
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
 *
 * Approach: Modified Binary Search checking sorted half
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */
public class LC0033_SearchInRotatedSortedArray {

    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;

            // Check if left half is normally sorted
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else { // Right half is sorted
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        LC0033_SearchInRotatedSortedArray solver = new LC0033_SearchInRotatedSortedArray();
        int[] nums = {4, 5, 6, 7, 0, 1, 2};
        System.out.println("Index of 0: " + solver.search(nums, 0)); // Expected: 4
        System.out.println("Index of 3: " + solver.search(nums, 3)); // Expected: -1
    }
}
