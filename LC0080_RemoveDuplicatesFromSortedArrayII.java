import java.util.Arrays;

/**
 * Problem: 80. Remove Duplicates from Sorted Array II
 * Difficulty: Medium
 * Category: Array, Two Pointers
 *
 * Algorithm:
 * Maintain index k. An element can be placed if k < 2 or nums[i] > nums[k - 2].
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0080_RemoveDuplicatesFromSortedArrayII {

    public int removeDuplicates(int[] nums) {
        if (nums.length <= 2) return nums.length;

        int k = 2;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] != nums[k - 2]) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }

    public static void main(String[] args) {
        LC0080_RemoveDuplicatesFromSortedArrayII solver = new LC0080_RemoveDuplicatesFromSortedArrayII();
        int[] nums = {1, 1, 1, 2, 2, 3};
        int k = solver.removeDuplicates(nums);
        assert k == 5;
        System.out.println("LC0080_RemoveDuplicatesFromSortedArrayII passed all tests!");
    }
}
