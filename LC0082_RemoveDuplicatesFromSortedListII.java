/**
 * Problem: 82. Remove Duplicates from Sorted List II
 * Difficulty: Medium
 * Category: Linked List, Two Pointers
 *
 * Algorithm:
 * Use a sentinel/dummy head. When current node has a duplicate value ahead,
 * skip all contiguous nodes with that value.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0082_RemoveDuplicatesFromSortedListII {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        while (head != null) {
            if (head.next != null && head.val == head.next.val) {
                while (head.next != null && head.val == head.next.val) {
                    head = head.next;
                }
                prev.next = head.next;
            } else {
                prev = prev.next;
            }
            head = head.next;
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        LC0082_RemoveDuplicatesFromSortedListII solver = new LC0082_RemoveDuplicatesFromSortedListII();
        ListNode h = new ListNode(1);
        h.next = new ListNode(2);
        h.next.next = new ListNode(2);
        h.next.next.next = new ListNode(3);
        ListNode res = solver.deleteDuplicates(h);
        assert res.val == 1 && res.next.val == 3 && res.next.next == null;
        System.out.println("LC0082_RemoveDuplicatesFromSortedListII passed all tests!");
    }
}
