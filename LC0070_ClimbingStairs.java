/**
 * LeetCode 70: Climbing Stairs
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/climbing-stairs/
 *
 * Approach: Dynamic Programming with Constant Space (Fibonacci)
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0070_ClimbingStairs {

    public int climbStairs(int n) {
        if (n <= 2) return n;
        int first = 1;
        int second = 2;

        for (int i = 3; i <= n; i++) {
            int third = first + second;
            first = second;
            second = third;
        }

        return second;
    }

    public static void main(String[] args) {
        LC0070_ClimbingStairs solver = new LC0070_ClimbingStairs();
        System.out.println("N=2 -> " + solver.climbStairs(2)); // Expected: 2
        System.out.println("N=5 -> " + solver.climbStairs(5)); // Expected: 8
    }
}
