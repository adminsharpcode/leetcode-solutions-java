import java.util.*;

/**
 * Problem: 260. Single Number III
 * Difficulty: Medium
 * Category: Array, Bit Manipulation
 *
 * Algorithm:
 * XOR sum of all elements = a ^ b.
 * Find lowest set bit diff = xor & (-xor) which differs between a and b.
 * Partition array into two buckets by diff bit and XOR each bucket to find a and b.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0260_SingleNumberIII {

    public int[] singleNumber(int[] nums) {
        int xor = 0;
        for (int n : nums) xor ^= n;

        int diff = xor & (-xor);
        int a = 0;
        for (int n : nums) {
            if ((n & diff) != 0) a ^= n;
        }
        return new int[]{a, xor ^ a};
    }

    public static void main(String[] args) {
        LC0260_SingleNumberIII sol = new LC0260_SingleNumberIII();
        System.out.println(Arrays.toString(sol.singleNumber(new int[]{1, 2, 1, 3, 2, 5}))); // [3, 5]
    }
}
