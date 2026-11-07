import java.util.Arrays;

/**
 * LeetCode 167: Two Sum II - Input Array Is Sorted
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
 *
 * Approach: Two Pointers (Left & Right converging)
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0167_TwoSumIIInputArrayIsSorted {

    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        while (left < right) {
            int sum = numbers[left] + numbers[right];

            if (sum == target) {
                // LeetCode 167 uses 1-based indexing
                return new int[]{left + 1, right + 1};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[]{-1, -1};
    }

    public static void main(String[] args) {
        LC0167_TwoSumIIInputArrayIsSorted solver = new LC0167_TwoSumIIInputArrayIsSorted();
        int[] numbers = {2, 7, 11, 15};
        int target = 9;
        System.out.println("Result: " + Arrays.toString(solver.twoSum(numbers, target))); // Expected: [1, 2]
    }
}
