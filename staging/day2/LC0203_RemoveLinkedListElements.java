/**
 * Problem: 203. Remove Linked List Elements
 * Difficulty: Easy
 * Category: Linked List, Recursion
 *
 * Algorithm:
 * Sentinel/dummy node allows uniform deletion even when target is at head.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0203_RemoveLinkedListElements {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy;

        while (curr.next != null) {
            if (curr.next.val == val) {
                curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        LC0203_RemoveLinkedListElements solver = new LC0203_RemoveLinkedListElements();
        ListNode h = new ListNode(1);
        h.next = new ListNode(2);
        h.next.next = new ListNode(6);
        h.next.next.next = new ListNode(3);
        ListNode res = solver.removeElements(h, 6);
        assert res.next.next.val == 3;
        System.out.println("LC0203_RemoveLinkedListElements passed all tests!");
    }
}
