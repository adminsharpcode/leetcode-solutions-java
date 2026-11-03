import java.util.HashSet;
import java.util.Set;

/**
 * LeetCode 128: Longest Consecutive Sequence
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/longest-consecutive-sequence/
 *
 * Approach: Hash Set with sequence start detection
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0128_LongestConsecutiveSequence {

    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        int maxLength = 0;
        for (int num : set) {
            // Only initiate counting if `num` is the start of a consecutive run
            if (!set.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                while (set.contains(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }

                maxLength = Math.max(maxLength, currentStreak);
            }
        }

        return maxLength;
    }

    public static void main(String[] args) {
        LC0128_LongestConsecutiveSequence solver = new LC0128_LongestConsecutiveSequence();
        int[] nums = {100, 4, 200, 1, 3, 2};
        System.out.println("Longest streak: " + solver.longestConsecutive(nums)); // Expected: 4 (1, 2, 3, 4)
    }
}
