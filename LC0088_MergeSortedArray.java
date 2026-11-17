import java.util.Arrays;

/**
 * Problem: 88. Merge Sorted Array
 * Difficulty: Easy
 * Category: Array, Two Pointers, Sorting
 *
 * Algorithm:
 * 3-Pointer reverse filling from the end of nums1 to prevent overwriting existing elements.
 *
 * Time Complexity: O(M + N)
 * Space Complexity: O(1)
 */
public class LC0088_MergeSortedArray {

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1;
        int p2 = n - 1;
        int p = m + n - 1;

        while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2]) {
                nums1[p--] = nums1[p1--];
            } else {
                nums1[p--] = nums2[p2--];
            }
        }

        while (p2 >= 0) {
            nums1[p--] = nums2[p2--];
        }
    }

    public static void main(String[] args) {
        LC0088_MergeSortedArray solver = new LC0088_MergeSortedArray();
        int[] nums1 = {1, 2, 3, 0, 0, 0};
        int[] nums2 = {2, 5, 6};
        solver.merge(nums1, 3, nums2, 3);
        assert Arrays.equals(nums1, new int[]{1, 2, 2, 3, 5, 6});
        System.out.println("LC0088_MergeSortedArray passed all tests!");
    }
}
