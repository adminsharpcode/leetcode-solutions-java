/**
 * Problem: 45. Jump Game II
 * Difficulty: Medium
 * Category: Array, Dynamic Programming, Greedy
 *
 * Algorithm:
 * Greedy BFS-like intervals: Maintain the current jump's reach boundary (curEnd)
 * and the farthest reach achievable from any position visited so far (farthest).
 * When reaching curEnd, increment jump count and update curEnd = farthest.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0045_JumpGameII {

    public int jump(int[] nums) {
        if (nums == null || nums.length <= 1) return 0;

        int jumps = 0;
        int curEnd = 0;
        int farthest = 0;

        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (i == curEnd) {
                jumps++;
                curEnd = farthest;
                if (curEnd >= nums.length - 1) break;
            }
        }
        return jumps;
    }

    public static void main(String[] args) {
        LC0045_JumpGameII solver = new LC0045_JumpGameII();
        int[] nums = {2, 3, 1, 1, 4};
        assert solver.jump(nums) == 2;
        System.out.println("LC0045_JumpGameII passed all tests!");
    }
}
