import java.util.Arrays;

/**
 * LeetCode 26: Remove Duplicates from Sorted Array
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
 *
 * Approach: Two Pointers (Slow & Fast Index)
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0026_RemoveDuplicatesFromSortedArray {

    public int removeDuplicates(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int writeIndex = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[writeIndex] = nums[i];
                writeIndex++;
            }
        }
        return writeIndex;
    }

    public static void main(String[] args) {
        LC0026_RemoveDuplicatesFromSortedArray solver = new LC0026_RemoveDuplicatesFromSortedArray();
        int[] nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        int k = solver.removeDuplicates(nums);
        System.out.println("Unique count: " + k); // Expected: 5
        System.out.println("Modified array: " + Arrays.toString(Arrays.copyOf(nums, k))); // [0, 1, 2, 3, 4]
    }
}
