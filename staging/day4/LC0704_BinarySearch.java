/**
 * Problem: 704. Binary Search
 * Difficulty: Easy
 * Category: Array, Binary Search
 *
 * Algorithm:
 * Standard closed-range [left, right] binary search with overflow-safe midpoint.
 *
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */
public class LC0704_BinarySearch {

    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        LC0704_BinarySearch solver = new LC0704_BinarySearch();
        int[] nums = {-1, 0, 3, 5, 9, 12};
        assert solver.search(nums, 9) == 4;
        assert solver.search(nums, 2) == -1;
        System.out.println("LC0704_BinarySearch passed all tests!");
    }
}
