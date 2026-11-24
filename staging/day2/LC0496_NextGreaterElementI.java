import java.util.*;

/**
 * Problem: 496. Next Greater Element I
 * Difficulty: Easy
 * Category: Array, Hash Table, Stack, Monotonic Stack
 *
 * Algorithm:
 * Use monotonic decreasing stack on nums2 to map each element to its next greater element.
 * Lookup answers for nums1 in O(1) via HashMap.
 *
 * Time Complexity: O(nums1.length + nums2.length)
 * Space Complexity: O(nums2.length)
 */
public class LC0496_NextGreaterElementI {

    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap<>();
        Deque<Integer> stack = new ArrayDeque<>();

        for (int num : nums2) {
            while (!stack.isEmpty() && stack.peek() < num) {
                map.put(stack.pop(), num);
            }
            stack.push(num);
        }

        int[] res = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            res[i] = map.getOrDefault(nums1[i], -1);
        }
        return res;
    }

    public static void main(String[] args) {
        LC0496_NextGreaterElementI sol = new LC0496_NextGreaterElementI();
        int[] n1 = {4, 1, 2}, n2 = {1, 3, 4, 2};
        System.out.println(Arrays.toString(sol.nextGreaterElement(n1, n2))); // [-1, 3, -1]
    }
}
