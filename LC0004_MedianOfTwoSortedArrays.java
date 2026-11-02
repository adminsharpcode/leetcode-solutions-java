/**
 * LeetCode 4: Median of Two Sorted Arrays
 * Difficulty: Hard
 * Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
 *
 * Approach: Binary Search Partition on shorter array
 * Time Complexity: O(log(min(M, N)))
 * Space Complexity: O(1)
 */
public class LC0004_MedianOfTwoSortedArrays {

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.length;
        int n = nums2.length;
        int low = 0, high = m;

        while (low <= high) {
            int partitionX = (low + high) / 2;
            int partitionY = (m + n + 1) / 2 - partitionX;

            int maxLeftX = (partitionX == 0) ? Integer.MIN_VALUE : nums1[partitionX - 1];
            int minRightX = (partitionX == m) ? Integer.MAX_VALUE : nums1[partitionX];

            int maxLeftY = (partitionY == 0) ? Integer.MIN_VALUE : nums2[partitionY - 1];
            int minRightY = (partitionY == n) ? Integer.MAX_VALUE : nums2[partitionY];

            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                if ((m + n) % 2 == 0) {
                    return ((double) Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2.0;
                } else {
                    return (double) Math.max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                high = partitionX - 1;
            } else {
                low = partitionX + 1;
            }
        }

        throw new IllegalArgumentException("Input arrays not sorted.");
    }

    public static void main(String[] args) {
        LC0004_MedianOfTwoSortedArrays solver = new LC0004_MedianOfTwoSortedArrays();
        int[] nums1 = {1, 3};
        int[] nums2 = {2};
        System.out.println("Median: " + solver.findMedianSortedArrays(nums1, nums2)); // Expected: 2.0

        int[] a = {1, 2};
        int[] b = {3, 4};
        System.out.println("Median: " + solver.findMedianSortedArrays(a, b)); // Expected: 2.5
    }
}
