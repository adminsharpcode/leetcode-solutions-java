import java.util.*;
public class LC0632_SmallestRange {
    public int[] smallestRange(List<List<Integer>> nums) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < nums.size(); i++) {
            pq.offer(new int[]{nums.get(i).get(0), i, 0});
            max = Math.max(max, nums.get(i).get(0));
        }
        int[] res = {pq.peek()[0], max};
        while (true) {
            int[] cur = pq.poll();
            int val = cur[0], row = cur[1], col = cur[2];
            if (col + 1 >= nums.get(row).size()) break;
            int next = nums.get(row).get(col + 1);
            pq.offer(new int[]{next, row, col + 1});
            max = Math.max(max, next);
            if (max - pq.peek()[0] < res[1] - res[0]) res = new int[]{pq.peek()[0], max};
        }
        return res;
    }
    public static void main(String[] args) {
        LC0632_SmallestRange sol = new LC0632_SmallestRange();
        List<List<Integer>> nums = Arrays.asList(Arrays.asList(4,10,15,24,26),Arrays.asList(0,9,12,20),Arrays.asList(5,18,22,30));
        System.out.println(Arrays.toString(sol.smallestRange(nums))); // [20, 24]
    }
}
