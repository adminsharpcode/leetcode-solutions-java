import java.util.Arrays;

/**
 * LeetCode 189: Rotate Array
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/rotate-array/
 *
 * Approach: Array Reversal in 3 passes
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0189_RotateArray {

    public void rotate(int[] nums, int k) {
        if (nums == null || nums.length == 0) {
            return;
        }

        k = k % nums.length;
        // Step 1: Reverse entire array
        reverse(nums, 0, nums.length - 1);
        // Step 2: Reverse first k elements
        reverse(nums, 0, k - 1);
        // Step 3: Reverse remaining n - k elements
        reverse(nums, k, nums.length - 1);
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }

    public static void main(String[] args) {
        LC0189_RotateArray solver = new LC0189_RotateArray();
        int[] nums = {1, 2, 3, 4, 5, 6, 7};
        solver.rotate(nums, 3);
        System.out.println("Rotated: " + Arrays.toString(nums)); // Expected: [5, 6, 7, 1, 2, 3, 4]
    }
}
