/**
 * LeetCode 142: Linked List Cycle II
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/linked-list-cycle-ii/
 *
 * Approach: Floyd's Cycle-Finding Algorithm (Meeting point + Origin walk)
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0142_LinkedListCycleII {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                // Cycle detected: advance pointer from head and slow simultaneously
                ListNode ptr = head;
                while (ptr != slow) {
                    ptr = ptr.next;
                    slow = slow.next;
                }
                return ptr;
            }
        }

        return null;
    }

    public static void main(String[] args) {
        LC0142_LinkedListCycleII solver = new LC0142_LinkedListCycleII();
        ListNode n1 = new ListNode(3);
        ListNode n2 = new ListNode(2);
        ListNode n3 = new ListNode(0);
        ListNode n4 = new ListNode(-4);
        n1.next = n2;
        n2.next = n3;
        n3.next = n4;
        n4.next = n2; // Cycle at n2

        ListNode entry = solver.detectCycle(n1);
        System.out.println("Cycle entry node val: " + (entry != null ? entry.val : "null")); // Expected: 2
    }
}
