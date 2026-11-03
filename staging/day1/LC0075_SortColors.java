import java.util.Arrays;

/**
 * LeetCode 75: Sort Colors
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/sort-colors/
 *
 * Approach: Dutch National Flag Algorithm (3-way Partitioning)
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0075_SortColors {

    public void sortColors(int[] nums) {
        int low = 0;
        int mid = 0;
        int high = nums.length - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums, low, mid);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                swap(nums, mid, high);
                high--;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public static void main(String[] args) {
        LC0075_SortColors solver = new LC0075_SortColors();
        int[] nums = {2, 0, 2, 1, 1, 0};
        solver.sortColors(nums);
        System.out.println("Sorted colors: " + Arrays.toString(nums)); // Expected: [0, 0, 1, 1, 2, 2]
    }
}
