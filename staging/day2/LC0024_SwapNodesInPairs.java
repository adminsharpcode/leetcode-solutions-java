/**
 * LeetCode 24: Swap Nodes in Pairs
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/swap-nodes-in-pairs/
 *
 * Approach: Iterative pointer manipulation with dummy node
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0024_SwapNodesInPairs {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;

        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = prev.next.next;

            // Swapping pointers
            first.next = second.next;
            second.next = first;
            prev.next = second;

            prev = first;
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        LC0024_SwapNodesInPairs solver = new LC0024_SwapNodesInPairs();
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
        ListNode swapped = solver.swapPairs(head);
        System.out.print("Swapped: ");
        while (swapped != null) {
            System.out.print(swapped.val + " ");
            swapped = swapped.next;
        }
        System.out.println(); // Expected: 2 1 4 3
    }
}
