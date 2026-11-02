/**
 * LeetCode 138: Copy List with Random Pointer
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/copy-list-with-random-pointer/
 *
 * Approach: Interweaving Cloned Nodes (O(1) Auxiliary Space)
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0138_CopyListWithRandomPointer {

    public static class Node {
        int val;
        Node next;
        Node random;

        public Node(int val) {
            this.val = val;
            this.next = null;
            this.random = null;
        }
    }

    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }

        // Step 1: Create a copy of each node and interleave it with original list
        Node curr = head;
        while (curr != null) {
            Node copy = new Node(curr.val);
            copy.next = curr.next;
            curr.next = copy;
            curr = copy.next;
        }

        // Step 2: Assign random pointers for the copied nodes
        curr = head;
        while (curr != null) {
            if (curr.random != null) {
                curr.next.random = curr.random.next;
            }
            curr = curr.next.next;
        }

        // Step 3: Unweave the two lists to restore original and extract cloned list
        curr = head;
        Node copiedHead = head.next;
        Node copyCurr = copiedHead;

        while (curr != null) {
            curr.next = curr.next.next;
            copyCurr.next = (copyCurr.next != null) ? copyCurr.next.next : null;
            curr = curr.next;
            copyCurr = copyCurr.next;
        }

        return copiedHead;
    }

    public static void main(String[] args) {
        LC0138_CopyListWithRandomPointer solver = new LC0138_CopyListWithRandomPointer();

        Node n1 = new Node(7);
        Node n2 = new Node(13);
        Node n3 = new Node(11);

        n1.next = n2;
        n2.next = n3;

        n2.random = n1;
        n3.random = n2;

        Node copied = solver.copyRandomList(n1);

        System.out.println("Original N1: " + n1.val + ", Copied N1: " + copied.val);
        System.out.println("Original N2 random: " + n2.random.val + ", Copied N2 random: " + copied.next.random.val);
        System.out.println("Are distinct instances: " + (n1 != copied && n2 != copied.next)); // Expected: true
    }
}
