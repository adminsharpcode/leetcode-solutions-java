/**
 * Problem: 162. Find Peak Element
 * Difficulty: Medium
 * Category: Array, Binary Search
 *
 * Algorithm:
 * Binary search: if nums[mid] < nums[mid + 1], a peak must exist in the right half.
 * Otherwise, a peak exists in the left half including mid.
 *
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */
public class LC0162_FindPeakElement {

    public int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    public static void main(String[] args) {
        LC0162_FindPeakElement solver = new LC0162_FindPeakElement();
        int[] nums = {1, 2, 3, 1};
        assert solver.findPeakElement(nums) == 2;
        System.out.println("LC0162_FindPeakElement passed all tests!");
    }
}
