/**
 * LeetCode 206: Reverse Linked List
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/reverse-linked-list/
 *
 * Approach: In-Place Iterative 3-Pointer Reversal
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0206_ReverseLinkedList {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }

        return prev;
    }

    public static void main(String[] args) {
        LC0206_ReverseLinkedList solver = new LC0206_ReverseLinkedList();
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        ListNode reversed = solver.reverseList(head);

        System.out.print("Reversed: ");
        while (reversed != null) {
            System.out.print(reversed.val + (reversed.next != null ? " -> " : ""));
            reversed = reversed.next;
        }
        System.out.println(); // Expected: 5 -> 4 -> 3 -> 2 -> 1
    }
}
