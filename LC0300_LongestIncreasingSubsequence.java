import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * LeetCode 300: Longest Increasing Subsequence
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/longest-increasing-subsequence/
 *
 * Approach: Patience Sorting with Binary Search
 * Time Complexity: O(N log N)
 * Space Complexity: O(N)
 */
public class LC0300_LongestIncreasingSubsequence {

    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        List<Integer> tails = new ArrayList<>();

        for (int num : nums) {
            int idx = Collections.binarySearch(tails, num);
            if (idx < 0) {
                idx = -(idx + 1);
            }
            if (idx == tails.size()) {
                tails.add(num);
            } else {
                tails.set(idx, num);
            }
        }

        return tails.size();
    }

    public static void main(String[] args) {
        LC0300_LongestIncreasingSubsequence solver = new LC0300_LongestIncreasingSubsequence();
        int[] nums = {10, 9, 2, 5, 3, 7, 101, 18};
        System.out.println("LIS length: " + solver.lengthOfLIS(nums)); // Expected: 4 [2, 3, 7, 101]
    }
}
