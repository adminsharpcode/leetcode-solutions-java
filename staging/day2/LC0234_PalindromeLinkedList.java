/**
 * LeetCode 234: Palindrome Linked List
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/palindrome-linked-list/
 *
 * Approach: Find Middle + Reverse Second Half + Element Comparison
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0234_PalindromeLinkedList {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) {
            return true;
        }

        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode secondHalf = reverseList(slow.next);
        ListNode firstHalf = head;

        boolean isPalin = true;
        ListNode curr = secondHalf;
        while (curr != null) {
            if (firstHalf.val != curr.val) {
                isPalin = false;
                break;
            }
            firstHalf = firstHalf.next;
            curr = curr.next;
        }

        return isPalin;
    }

    private ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    public static void main(String[] args) {
        LC0234_PalindromeLinkedList solver = new LC0234_PalindromeLinkedList();
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(1))));
        System.out.println("Is palindrome: " + solver.isPalindrome(head)); // Expected: true
    }
}
