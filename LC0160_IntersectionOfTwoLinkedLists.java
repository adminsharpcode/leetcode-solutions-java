/**
 * Problem: 160. Intersection of Two Linked Lists
 * Difficulty: Easy
 * Category: Linked List, Two Pointers
 *
 * Algorithm:
 * Two pointers traversing A then B, and B then A. Both travel exactly len(A) + len(B),
 * intersecting at the shared node or reaching null simultaneously.
 *
 * Time Complexity: O(N + M)
 * Space Complexity: O(1)
 */
public class LC0160_IntersectionOfTwoLinkedLists {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;

        ListNode pA = headA;
        ListNode pB = headB;

        while (pA != pB) {
            pA = (pA == null) ? headB : pA.next;
            pB = (pB == null) ? headA : pB.next;
        }
        return pA;
    }

    public static void main(String[] args) {
        LC0160_IntersectionOfTwoLinkedLists solver = new LC0160_IntersectionOfTwoLinkedLists();
        ListNode common = new ListNode(8);
        ListNode a = new ListNode(4);
        a.next = common;
        ListNode b = new ListNode(5);
        b.next = common;
        assert solver.getIntersectionNode(a, b) == common;
        System.out.println("LC0160_IntersectionOfTwoLinkedLists passed all tests!");
    }
}
