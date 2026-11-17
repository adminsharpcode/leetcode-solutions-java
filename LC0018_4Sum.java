import java.util.*;

/**
 * Problem: 18. 4Sum
 * Difficulty: Medium
 * Category: Array, Two Pointers, Sorting
 *
 * Algorithm:
 * Sort array, use two outer loops and two pointers for remaining two elements.
 * Use long to avoid integer overflow during 4-sum comparison.
 * Skip duplicates at each stage to avoid duplicate quadruplets.
 *
 * Time Complexity: O(N^3)
 * Space Complexity: O(1) auxiliary (ignoring output list)
 */
public class LC0018_4Sum {

    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums == null || nums.length < 4) return result;

        Arrays.sort(nums);
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                int left = j + 1;
                int right = n - 1;

                while (left < right) {
                    long sum = (long) nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        LC0018_4Sum solver = new LC0018_4Sum();
        int[] nums = {1, 0, -1, 0, -2, 2};
        List<List<Integer>> ans = solver.fourSum(nums, 0);
        assert ans.size() == 3;
        System.out.println("LC0018_4Sum passed all tests!");
    }
}
