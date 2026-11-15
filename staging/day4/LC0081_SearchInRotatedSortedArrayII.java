/**
 * Problem: 81. Search in Rotated Sorted Array II
 * Difficulty: Medium
 * Category: Array, Binary Search
 *
 * Algorithm:
 * Rotated binary search with duplicates: when nums[left] == nums[mid] == nums[right],
 * shrink bounds (left++, right--); otherwise identify sorted half.
 *
 * Time Complexity: O(log N) average, O(N) worst-case with all duplicates
 * Space Complexity: O(1)
 */
public class LC0081_SearchInRotatedSortedArrayII {

    public boolean search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) return true;

            if (nums[left] == nums[mid] && nums[mid] == nums[right]) {
                left++;
                right--;
            } else if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        LC0081_SearchInRotatedSortedArrayII solver = new LC0081_SearchInRotatedSortedArrayII();
        int[] nums = {2, 5, 6, 0, 0, 1, 2};
        assert solver.search(nums, 0);
        assert !solver.search(nums, 3);
        System.out.println("LC0081_SearchInRotatedSortedArrayII passed all tests!");
    }
}
