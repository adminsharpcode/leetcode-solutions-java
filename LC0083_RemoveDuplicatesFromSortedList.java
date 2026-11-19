/**
 * Problem: 83. Remove Duplicates from Sorted List
 * Difficulty: Easy
 * Category: Linked List
 *
 * Algorithm:
 * Single pass: compare current node with current.next. If equal, drop next node.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0083_RemoveDuplicatesFromSortedList {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public ListNode deleteDuplicates(ListNode head) {
        ListNode curr = head;
        while (curr != null && curr.next != null) {
            if (curr.val == curr.next.val) {
                curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }
        return head;
    }

    public static void main(String[] args) {
        LC0083_RemoveDuplicatesFromSortedList solver = new LC0083_RemoveDuplicatesFromSortedList();
        ListNode h = new ListNode(1);
        h.next = new ListNode(1);
        h.next.next = new ListNode(2);
        ListNode res = solver.deleteDuplicates(h);
        assert res.val == 1 && res.next.val == 2 && res.next.next == null;
        System.out.println("LC0083_RemoveDuplicatesFromSortedList passed all tests!");
    }
}
