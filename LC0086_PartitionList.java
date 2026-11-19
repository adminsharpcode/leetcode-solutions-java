/**
 * Problem: 86. Partition List
 * Difficulty: Medium
 * Category: Linked List, Two Pointers
 *
 * Algorithm:
 * Maintain two separate sublists (before and after), appending nodes based on val < x.
 * Connect before list tail to after list head.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0086_PartitionList {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public ListNode partition(ListNode head, int x) {
        ListNode beforeHead = new ListNode(0);
        ListNode afterHead = new ListNode(0);
        ListNode before = beforeHead;
        ListNode after = afterHead;

        while (head != null) {
            if (head.val < x) {
                before.next = head;
                before = before.next;
            } else {
                after.next = head;
                after = after.next;
            }
            head = head.next;
        }

        after.next = null;
        before.next = afterHead.next;
        return beforeHead.next;
    }

    public static void main(String[] args) {
        LC0086_PartitionList solver = new LC0086_PartitionList();
        ListNode h = new ListNode(1);
        h.next = new ListNode(4);
        h.next.next = new ListNode(3);
        h.next.next.next = new ListNode(2);
        ListNode res = solver.partition(h, 3);
        assert res.val == 1 && res.next.val == 2;
        System.out.println("LC0086_PartitionList passed all tests!");
    }
}
