import java.util.*;
public class LC0496_NextGreaterElementI {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap<>();
        Deque<Integer> stack = new ArrayDeque<>();
        for (int n : nums2) {
            while (!stack.isEmpty() && stack.peek() < n) map.put(stack.pop(), n);
            stack.push(n);
        }
        int[] res = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) res[i] = map.getOrDefault(nums1[i], -1);
        return res;
    }
    public static void main(String[] args) {
        LC0496_NextGreaterElementI sol = new LC0496_NextGreaterElementI();
        System.out.println(Arrays.toString(sol.nextGreaterElement(new int[]{4,1,2}, new int[]{1,3,4,2}))); // [-1,3,-1]
    }
}
