import java.util.Arrays;

/**
 * LeetCode 34: Find First and Last Position of Element in Sorted Array
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
 *
 * Approach: Double Binary Search (Left Boundary and Right Boundary)
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */
public class LC0034_FindFirstAndLastPositionOfElementInSortedArray {

    public int[] searchRange(int[] nums, int target) {
        int[] result = {-1, -1};
        result[0] = findBound(nums, target, true);
        if (result[0] != -1) {
            result[1] = findBound(nums, target, false);
        }
        return result;
    }

    private int findBound(int[] nums, int target, boolean isFirst) {
        int left = 0;
        int right = nums.length - 1;
        int bound = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                bound = mid;
                if (isFirst) {
                    right = mid - 1; // Seek leftmost occurrence
                } else {
                    left = mid + 1;  // Seek rightmost occurrence
                }
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return bound;
    }

    public static void main(String[] args) {
        LC0034_FindFirstAndLastPositionOfElementInSortedArray solver =
            new LC0034_FindFirstAndLastPositionOfElementInSortedArray();
        int[] nums = {5, 7, 7, 8, 8, 10};
        System.out.println("Range for 8: " + Arrays.toString(solver.searchRange(nums, 8))); // Expected: [3, 4]
        System.out.println("Range for 6: " + Arrays.toString(solver.searchRange(nums, 6))); // Expected: [-1, -1]
    }
}
