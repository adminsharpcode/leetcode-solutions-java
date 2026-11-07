/**
 * LeetCode 61: Rotate List
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/rotate-list/
 *
 * Approach: Connect list to circular ring and break at new tail
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0061_RotateList {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) {
            return head;
        }

        // Compute length and locate the tail node
        int length = 1;
        ListNode tail = head;
        while (tail.next != null) {
            tail = tail.next;
            length++;
        }

        k = k % length;
        if (k == 0) {
            return head;
        }

        // Form a circular linked list
        tail.next = head;

        // Find the new tail at position (length - k)
        int stepsToNewTail = length - k;
        ListNode newTail = head;
        for (int i = 1; i < stepsToNewTail; i++) {
            newTail = newTail.next;
        }

        ListNode newHead = newTail.next;
        newTail.next = null;

        return newHead;
    }

    public static void main(String[] args) {
        LC0061_RotateList solver = new LC0061_RotateList();
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        ListNode rotated = solver.rotateRight(head, 2);
        System.out.print("Rotated: ");
        while (rotated != null) {
            System.out.print(rotated.val + " ");
            rotated = rotated.next;
        }
        System.out.println(); // Expected: 4 5 1 2 3
    }
}
