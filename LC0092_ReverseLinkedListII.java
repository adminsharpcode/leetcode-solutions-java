/**
 * Problem: 92. Reverse Linked List II
 * Difficulty: Medium
 * Category: Linked List
 *
 * Algorithm:
 * Move to node right before left. Iteratively insert each subsequent node
 * up to right between prev and prev.next.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0092_ReverseLinkedListII {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || left == right) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        for (int i = 0; i < left - 1; i++) {
            prev = prev.next;
        }

        ListNode curr = prev.next;
        for (int i = 0; i < right - left; i++) {
            ListNode next = curr.next;
            curr.next = next.next;
            next.next = prev.next;
            prev.next = next;
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        LC0092_ReverseLinkedListII solver = new LC0092_ReverseLinkedListII();
        ListNode h = new ListNode(1);
        h.next = new ListNode(2);
        h.next.next = new ListNode(3);
        h.next.next.next = new ListNode(4);
        ListNode res = solver.reverseBetween(h, 2, 3);
        assert res.next.val == 3 && res.next.next.val == 2;
        System.out.println("LC0092_ReverseLinkedListII passed all tests!");
    }
}
