/**
 * LeetCode 11: Container With Most Water
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/container-with-most-water/
 *
 * Approach: Two Pointers Greedy
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0011_ContainerWithMostWater {

    public int maxArea(int[] height) {
        int maxArea = 0;
        int left = 0;
        int right = height.length - 1;

        while (left < right) {
            int width = right - left;
            int h = Math.min(height[left], height[right]);
            maxArea = Math.max(maxArea, width * h);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }

    public static void main(String[] args) {
        LC0011_ContainerWithMostWater solver = new LC0011_ContainerWithMostWater();
        int[] h = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        System.out.println("Max Area: " + solver.maxArea(h)); // Expected: 49
    }
}
