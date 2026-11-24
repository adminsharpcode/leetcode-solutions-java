/**
 * Problem: 643. Maximum Average Subarray I
 * Difficulty: Easy
 * Category: Array, Sliding Window
 *
 * Algorithm:
 * Maintain sliding window of fixed length k.
 * Compute initial sum of first k elements, slide right by adding incoming and subtracting outgoing.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0643_MaximumAverageSubarrayI {

    public double findMaxAverage(int[] nums, int k) {
        double sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];

        double maxSum = sum;
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            maxSum = Math.max(maxSum, sum);
        }
        return maxSum / k;
    }

    public static void main(String[] args) {
        LC0643_MaximumAverageSubarrayI sol = new LC0643_MaximumAverageSubarrayI();
        System.out.println(sol.findMaxAverage(new int[]{1, 12, -5, -6, 50, 3}, 4)); // 12.75
    }
}
