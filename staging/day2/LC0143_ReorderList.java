/**
 * LeetCode 143: Reorder List
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/reorder-list/
 *
 * Approach: Find Midpoint + Reverse Second Half + Interleave
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0143_ReorderList {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }

        // Step 1: Find middle using fast & slow pointers
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Step 2: Reverse second half of the list
        ListNode second = reverseList(slow.next);
        slow.next = null;

        // Step 3: Merge both halves alternatively
        ListNode first = head;
        while (second != null) {
            ListNode tmp1 = first.next;
            ListNode tmp2 = second.next;

            first.next = second;
            second.next = tmp1;

            first = tmp1;
            second = tmp2;
        }
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
        LC0143_ReorderList solver = new LC0143_ReorderList();
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
        solver.reorderList(head);
        System.out.print("Reordered: ");
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
        System.out.println(); // Expected: 1 4 2 3
    }
}
