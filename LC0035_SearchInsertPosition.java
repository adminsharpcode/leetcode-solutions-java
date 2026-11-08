/**
 * LeetCode 35: Search Insert Position
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/search-insert-position/
 *
 * Approach: Standard Binary Search lower bound
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */
public class LC0035_SearchInsertPosition {

    public int searchInsert(int[] nums, int target) {
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

        return left;
    }

    public static void main(String[] args) {
        LC0035_SearchInsertPosition solver = new LC0035_SearchInsertPosition();
        int[] nums = {1, 3, 5, 6};
        System.out.println("Insert 5: " + solver.searchInsert(nums, 5)); // Expected: 2
        System.out.println("Insert 2: " + solver.searchInsert(nums, 2)); // Expected: 1
        System.out.println("Insert 7: " + solver.searchInsert(nums, 7)); // Expected: 4
    }
}
