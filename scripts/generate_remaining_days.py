import os

BASE_DIR = r"E:\LeetCode-Solutions-Java\staging"

DATA = {
    # ---------------- DAY 2: LINKED LISTS ----------------
    "day2": [
        ("LC0024_SwapNodesInPairs.java", """/**
 * LeetCode 24: Swap Nodes in Pairs
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/swap-nodes-in-pairs/
 *
 * Approach: Iterative pointer manipulation with dummy node
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0024_SwapNodesInPairs {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;

        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = prev.next.next;

            // Swapping pointers
            first.next = second.next;
            second.next = first;
            prev.next = second;

            prev = first;
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        LC0024_SwapNodesInPairs solver = new LC0024_SwapNodesInPairs();
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
        ListNode swapped = solver.swapPairs(head);
        System.out.print("Swapped: ");
        while (swapped != null) {
            System.out.print(swapped.val + " ");
            swapped = swapped.next;
        }
        System.out.println(); // Expected: 2 1 4 3
    }
}
"""),
        ("LC0061_RotateList.java", """/**
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
"""),
        ("LC0141_LinkedListCycle.java", """/**
 * LeetCode 141: Linked List Cycle
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/linked-list-cycle/
 *
 * Approach: Floyd's Tortoise and Hare (Fast & Slow Pointers)
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0141_LinkedListCycle {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }

        ListNode slow = head;
        ListNode fast = head.next;

        while (slow != fast) {
            if (fast == null || fast.next == null) {
                return false;
            }
            slow = slow.next;
            fast = fast.next.next;
        }

        return true;
    }

    public static void main(String[] args) {
        LC0141_LinkedListCycle solver = new LC0141_LinkedListCycle();
        ListNode n1 = new ListNode(3);
        ListNode n2 = new ListNode(2);
        ListNode n3 = new ListNode(0);
        ListNode n4 = new ListNode(-4);
        n1.next = n2;
        n2.next = n3;
        n3.next = n4;
        n4.next = n2; // Creates cycle

        System.out.println("Has cycle: " + solver.hasCycle(n1)); // Expected: true
    }
}
"""),
        ("LC0142_LinkedListCycleII.java", """/**
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
"""),
        ("LC0143_ReorderList.java", """/**
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
"""),
        ("LC0234_PalindromeLinkedList.java", """/**
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
"""),
    ],

    # ---------------- DAY 3: BINARY SEARCH & MATRICES ----------------
    "day3": [
        ("LC0034_FindFirstAndLastPositionOfElementInSortedArray.java", """import java.util.Arrays;

/**
 * LeetCode 34: Find First and Last Position of Element in Sorted Array
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
 *
 * Approach: Double Binary Search (Left Boundary and Right Boundary)
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */
public class LC0034_FindFirstAndLastPositionOfElementInSortedArray {

    public int[] searchRange(int[] nums, int target) {
        int[] result = {-1, -1};
        result[0] = findBound(nums, target, true);
        if (result[0] != -1) {
            result[1] = findBound(nums, target, false);
        }
        return result;
    }

    private int findBound(int[] nums, int target, boolean isFirst) {
        int left = 0;
        int right = nums.length - 1;
        int bound = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                bound = mid;
                if (isFirst) {
                    right = mid - 1; // Seek leftmost occurrence
                } else {
                    left = mid + 1;  // Seek rightmost occurrence
                }
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return bound;
    }

    public static void main(String[] args) {
        LC0034_FindFirstAndLastPositionOfElementInSortedArray solver =
            new LC0034_FindFirstAndLastPositionOfElementInSortedArray();
        int[] nums = {5, 7, 7, 8, 8, 10};
        System.out.println("Range for 8: " + Arrays.toString(solver.searchRange(nums, 8))); // Expected: [3, 4]
        System.out.println("Range for 6: " + Arrays.toString(solver.searchRange(nums, 6))); // Expected: [-1, -1]
    }
}
"""),
        ("LC0035_SearchInsertPosition.java", """/**
 * LeetCode 35: Search Insert Position
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/search-insert-position/
 *
 * Approach: Standard Binary Search lower bound
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */
public class LC0035_SearchInsertPosition {

    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return left;
    }

    public static void main(String[] args) {
        LC0035_SearchInsertPosition solver = new LC0035_SearchInsertPosition();
        int[] nums = {1, 3, 5, 6};
        System.out.println("Insert 5: " + solver.searchInsert(nums, 5)); // Expected: 2
        System.out.println("Insert 2: " + solver.searchInsert(nums, 2)); // Expected: 1
        System.out.println("Insert 7: " + solver.searchInsert(nums, 7)); // Expected: 4
    }
}
"""),
        ("LC0048_RotateImage.java", """import java.util.Arrays;

/**
 * LeetCode 48: Rotate Image
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/rotate-image/
 *
 * Approach: Transpose Matrix + Reflect (Reverse Rows)
 * Time Complexity: O(N^2)
 * Space Complexity: O(1) in-place
 */
public class LC0048_RotateImage {

    public void rotate(int[][] matrix) {
        int n = matrix.length;

        // Step 1: Transpose matrix along main diagonal
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // Step 2: Reverse each row horizontally
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - 1 - j];
                matrix[i][n - 1 - j] = temp;
            }
        }
    }

    public static void main(String[] args) {
        LC0048_RotateImage solver = new LC0048_RotateImage();
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        solver.rotate(matrix);
        System.out.println("Rotated matrix: " + Arrays.deepToString(matrix));
        // Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    }
}
"""),
        ("LC0073_SetMatrixZeroes.java", """import java.util.Arrays;

/**
 * LeetCode 73: Set Matrix Zeroes
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/set-matrix-zeroes/
 *
 * Approach: In-Place Marking using First Row and First Column as Flags
 * Time Complexity: O(M * N)
 * Space Complexity: O(1)
 */
public class LC0073_SetMatrixZeroes {

    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        boolean firstColZero = false;

        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                firstColZero = true;
            }
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // Zero out cells based on top and left boundary flags
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // Handle first row
        if (matrix[0][0] == 0) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }

        // Handle first column
        if (firstColZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }

    public static void main(String[] args) {
        LC0073_SetMatrixZeroes solver = new LC0073_SetMatrixZeroes();
        int[][] matrix = {
            {1, 1, 1},
            {1, 0, 1},
            {1, 1, 1}
        };
        solver.setZeroes(matrix);
        System.out.println("Result: " + Arrays.deepToString(matrix));
        // Expected: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    }
}
"""),
        ("LC0074_SearchA2DMatrix.java", """/**
 * LeetCode 74: Search a 2D Matrix
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/search-a-2d-matrix/
 *
 * Approach: Virtual 1D Flattening + Binary Search
 * Time Complexity: O(log(M * N))
 * Space Complexity: O(1)
 */
public class LC0074_SearchA2DMatrix {

    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int m = matrix.length;
        int n = matrix[0].length;
        int left = 0;
        int right = m * n - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int midVal = matrix[mid / n][mid % n];

            if (midVal == target) {
                return true;
            } else if (midVal < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        LC0074_SearchA2DMatrix solver = new LC0074_SearchA2DMatrix();
        int[][] matrix = {
            {1, 3, 5, 7},
            {10, 11, 16, 20},
            {23, 30, 34, 60}
        };
        System.out.println("Search 3: " + solver.searchMatrix(matrix, 3));   // Expected: true
        System.out.println("Search 13: " + solver.searchMatrix(matrix, 13)); // Expected: false
    }
}
"""),
        ("LC0240_SearchA2DMatrixII.java", """/**
 * LeetCode 240: Search a 2D Matrix II
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
 *
 * Approach: Top-Right Corner Pointer Search (Binary Search Tree Elimination)
 * Time Complexity: O(M + N)
 * Space Complexity: O(1)
 */
public class LC0240_SearchA2DMatrixII {

    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int row = 0;
        int col = matrix[0].length - 1;

        while (row < matrix.length && col >= 0) {
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] > target) {
                col--;
            } else {
                row++;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        LC0240_SearchA2DMatrixII solver = new LC0240_SearchA2DMatrixII();
        int[][] matrix = {
            {1, 4, 7, 11, 15},
            {2, 5, 8, 12, 19},
            {3, 6, 9, 16, 22},
            {10, 13, 14, 17, 24},
            {18, 21, 23, 26, 30}
        };
        System.out.println("Search 5: " + solver.searchMatrix(matrix, 5));   // Expected: true
        System.out.println("Search 20: " + solver.searchMatrix(matrix, 20)); // Expected: false
    }
}
"""),
    ],

    # ---------------- DAY 4: STACKS, QUEUES & HEAPS ----------------
    "day4": [
        ("LC0150_EvaluateReversePolishNotation.java", """import java.util.ArrayDeque;
import java.util.Deque;

/**
 * LeetCode 150: Evaluate Reverse Polish Notation
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
 *
 * Approach: Stack-Based Operand Evaluation
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0150_EvaluateReversePolishNotation {

    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();

        for (String token : tokens) {
            if (token.equals("+")) {
                stack.push(stack.pop() + stack.pop());
            } else if (token.equals("-")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a - b);
            } else if (token.equals("*")) {
                stack.push(stack.pop() * stack.pop());
            } else if (token.equals("/")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a / b);
            } else {
                stack.push(Integer.parseInt(token));
            }
        }

        return stack.pop();
    }

    public static void main(String[] args) {
        LC0150_EvaluateReversePolishNotation solver = new LC0150_EvaluateReversePolishNotation();
        String[] tokens = {"2", "1", "+", "3", "*"};
        System.out.println("Result: " + solver.evalRPN(tokens)); // Expected: 9
    }
}
"""),
        ("LC0155_MinStack.java", """import java.util.ArrayDeque;
import java.util.Deque;

/**
 * LeetCode 155: Min Stack
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/min-stack/
 *
 * Approach: Two Stacks (Data Stack & Min Tracking Stack)
 * Time Complexity: O(1) for all operations
 * Space Complexity: O(N)
 */
public class LC0155_MinStack {

    private final Deque<Integer> stack;
    private final Deque<Integer> minStack;

    public LC0155_MinStack() {
        stack = new ArrayDeque<>();
        minStack = new ArrayDeque<>();
    }

    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }

    public void pop() {
        if (!stack.isEmpty()) {
            int removed = stack.pop();
            if (removed == minStack.peek()) {
                minStack.pop();
            }
        }
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }

    public static void main(String[] args) {
        LC0155_MinStack minStack = new LC0155_MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        System.out.println("Min: " + minStack.getMin()); // Expected: -3
        minStack.pop();
        System.out.println("Top: " + minStack.top());    // Expected: 0
        System.out.println("Min: " + minStack.getMin()); // Expected: -2
    }
}
"""),
        ("LC0225_ImplementStackUsingQueues.java", """import java.util.LinkedList;
import java.util.Queue;

/**
 * LeetCode 225: Implement Stack using Queues
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/implement-stack-using-queues/
 *
 * Approach: Single Queue with Cyclic Rotation on Push
 * Time Complexity: push: O(N), pop/top/empty: O(1)
 * Space Complexity: O(N)
 */
public class LC0225_ImplementStackUsingQueues {

    private final Queue<Integer> queue;

    public LC0225_ImplementStackUsingQueues() {
        queue = new LinkedList<>();
    }

    public void push(int x) {
        queue.offer(x);
        int size = queue.size();
        for (int i = 0; i < size - 1; i++) {
            queue.offer(queue.poll());
        }
    }

    public int pop() {
        return queue.poll();
    }

    public int top() {
        return queue.peek();
    }

    public boolean empty() {
        return queue.isEmpty();
    }

    public static void main(String[] args) {
        LC0225_ImplementStackUsingQueues myStack = new LC0225_ImplementStackUsingQueues();
        myStack.push(1);
        myStack.push(2);
        System.out.println("Top: " + myStack.top());   // Expected: 2
        System.out.println("Pop: " + myStack.pop());   // Expected: 2
        System.out.println("Empty: " + myStack.empty()); // Expected: false
    }
}
"""),
        ("LC0232_ImplementQueueUsingStacks.java", """import java.util.ArrayDeque;
import java.util.Deque;

/**
 * LeetCode 232: Implement Queue using Stacks
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/implement-queue-using-stacks/
 *
 * Approach: Two Stacks (In-stack and Out-stack) Amortized O(1)
 * Time Complexity: Amortized O(1) for pop and peek, O(1) for push
 * Space Complexity: O(N)
 */
public class LC0232_ImplementQueueUsingStacks {

    private final Deque<Integer> inStack;
    private final Deque<Integer> outStack;

    public LC0232_ImplementQueueUsingStacks() {
        inStack = new ArrayDeque<>();
        outStack = new ArrayDeque<>();
    }

    public void push(int x) {
        inStack.push(x);
    }

    public int pop() {
        move();
        return outStack.pop();
    }

    public int peek() {
        move();
        return outStack.peek();
    }

    public boolean empty() {
        return inStack.isEmpty() && outStack.isEmpty();
    }

    private void move() {
        if (outStack.isEmpty()) {
            while (!inStack.isEmpty()) {
                outStack.push(inStack.pop());
            }
        }
    }

    public static void main(String[] args) {
        LC0232_ImplementQueueUsingStacks myQueue = new LC0232_ImplementQueueUsingStacks();
        myQueue.push(1);
        myQueue.push(2);
        System.out.println("Peek: " + myQueue.peek());   // Expected: 1
        System.out.println("Pop: " + myQueue.pop());     // Expected: 1
        System.out.println("Empty: " + myQueue.empty()); // Expected: false
    }
}
"""),
        ("LC0347_TopKFrequentElements.java", """import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

/**
 * LeetCode 347: Top K Frequent Elements
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/top-k-frequent-elements/
 *
 * Approach: Hash Map Frequency Count + Min-Heap of Size K
 * Time Complexity: O(N log K)
 * Space Complexity: O(N + K)
 */
public class LC0347_TopKFrequentElements {

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Min-heap ordered by frequency ascending
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b) -> freqMap.get(a) - freqMap.get(b));

        for (int num : freqMap.keySet()) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = minHeap.poll();
        }

        return result;
    }

    public static void main(String[] args) {
        LC0347_TopKFrequentElements solver = new LC0347_TopKFrequentElements();
        int[] nums = {1, 1, 1, 2, 2, 3};
        System.out.println("Top 2: " + Arrays.toString(solver.topKFrequent(nums, 2))); // Expected: [2, 1] (or [1, 2])
    }
}
"""),
        ("LC0373_FindKPairsWithSmallestSums.java", """import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

/**
 * LeetCode 373: Find K Pairs with Smallest Sums
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
 *
 * Approach: PriorityQueue Min-Heap with index coordinate tracking
 * Time Complexity: O(K log(min(N, K)))
 * Space Complexity: O(min(N, K))
 */
public class LC0373_FindKPairsWithSmallestSums {

    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums1 == null || nums2 == null || nums1.length == 0 || nums2.length == 0 || k <= 0) {
            return result;
        }

        // Heap elements: [sum, indexInNums1, indexInNums2]
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        // Push pairs of (nums1[i], nums2[0])
        for (int i = 0; i < Math.min(nums1.length, k); i++) {
            minHeap.offer(new int[]{nums1[i] + nums2[0], i, 0});
        }

        while (k > 0 && !minHeap.isEmpty()) {
            int[] curr = minHeap.poll();
            int i = curr[1];
            int j = curr[2];

            result.add(Arrays.asList(nums1[i], nums2[j]));
            k--;

            if (j + 1 < nums2.length) {
                minHeap.offer(new int[]{nums1[i] + nums2[j + 1], i, j + 1});
            }
        }

        return result;
    }

    public static void main(String[] args) {
        LC0373_FindKPairsWithSmallestSums solver = new LC0373_FindKPairsWithSmallestSums();
        int[] nums1 = {1, 7, 11};
        int[] nums2 = {2, 4, 6};
        System.out.println("Result: " + solver.kSmallestPairs(nums1, nums2, 3));
        // Expected: [[1, 2], [1, 4], [1, 6]]
    }
}
"""),
    ],

    # ---------------- DAY 5: TREES & BST ----------------
    "day5": [
        ("LC0100_SameTree.java", """/**
 * LeetCode 100: Same Tree
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/same-tree/
 *
 * Approach: Recursive DFS structural and value comparison
 * Time Complexity: O(N)
 * Space Complexity: O(H) where H is tree height
 */
public class LC0100_SameTree {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if (p == null || q == null || p.val != q.val) {
            return false;
        }
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

    public static void main(String[] args) {
        LC0100_SameTree solver = new LC0100_SameTree();
        TreeNode t1 = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        TreeNode t2 = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        System.out.println("Same tree: " + solver.isSameTree(t1, t2)); // Expected: true
    }
}
"""),
        ("LC0101_SymmetricTree.java", """/**
 * LeetCode 101: Symmetric Tree
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/symmetric-tree/
 *
 * Approach: Dual Subtree Mirror DFS
 * Time Complexity: O(N)
 * Space Complexity: O(H) where H is tree height
 */
public class LC0101_SymmetricTree {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return isMirror(root.left, root.right);
    }

    private boolean isMirror(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) {
            return true;
        }
        if (t1 == null || t2 == null || t1.val != t2.val) {
            return false;
        }
        return isMirror(t1.left, t2.right) && isMirror(t1.right, t2.left);
    }

    public static void main(String[] args) {
        LC0101_SymmetricTree solver = new LC0101_SymmetricTree();
        TreeNode root = new TreeNode(1,
            new TreeNode(2, new TreeNode(3), new TreeNode(4)),
            new TreeNode(2, new TreeNode(4), new TreeNode(3))
        );
        System.out.println("Is symmetric: " + solver.isSymmetric(root)); // Expected: true
    }
}
"""),
        ("LC0103_BinaryTreeZigzagLevelOrderTraversal.java", """import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

/**
 * LeetCode 103: Binary Tree Zigzag Level Order Traversal
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
 *
 * Approach: Breadth-First Search with alternating Deque insertion
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0103_BinaryTreeZigzagLevelOrderTraversal {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        boolean leftToRight = true;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            LinkedList<Integer> currentLevel = new LinkedList<>();

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();

                if (leftToRight) {
                    currentLevel.addLast(node.val);
                } else {
                    currentLevel.addFirst(node.val);
                }

                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }

            result.add(currentLevel);
            leftToRight = !leftToRight;
        }

        return result;
    }

    public static void main(String[] args) {
        LC0103_BinaryTreeZigzagLevelOrderTraversal solver =
            new LC0103_BinaryTreeZigzagLevelOrderTraversal();
        TreeNode root = new TreeNode(3,
            new TreeNode(9),
            new TreeNode(20, new TreeNode(15), new TreeNode(7))
        );
        System.out.println("Zigzag traversal: " + solver.zigzagLevelOrder(root));
        // Expected: [[3], [20, 9], [15, 7]]
    }
}
"""),
        ("LC0110_BalancedBinaryTree.java", """/**
 * LeetCode 110: Balanced Binary Tree
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/balanced-binary-tree/
 *
 * Approach: Bottom-up Post-Order DFS with early sentinel termination (-1)
 * Time Complexity: O(N)
 * Space Complexity: O(H) where H is tree height
 */
public class LC0110_BalancedBinaryTree {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public boolean isBalanced(TreeNode root) {
        return checkHeight(root) != -1;
    }

    private int checkHeight(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftHeight = checkHeight(root.left);
        if (leftHeight == -1) return -1;

        int rightHeight = checkHeight(root.right);
        if (rightHeight == -1) return -1;

        if (Math.abs(leftHeight - rightHeight) > 1) {
            return -1;
        }

        return 1 + Math.max(leftHeight, rightHeight);
    }

    public static void main(String[] args) {
        LC0110_BalancedBinaryTree solver = new LC0110_BalancedBinaryTree();
        TreeNode root = new TreeNode(3,
            new TreeNode(9),
            new TreeNode(20, new TreeNode(15), new TreeNode(7))
        );
        System.out.println("Is balanced: " + solver.isBalanced(root)); // Expected: true
    }
}
"""),
        ("LC0230_KthSmallestElementInABST.java", """import java.util.ArrayDeque;
import java.util.Deque;

/**
 * LeetCode 230: Kth Smallest Element in a BST
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
 *
 * Approach: Iterative In-Order Traversal with Stack
 * Time Complexity: O(H + K)
 * Space Complexity: O(H) where H is tree height
 */
public class LC0230_KthSmallestElementInABST {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public int kthSmallest(TreeNode root, int k) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode curr = root;

        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }

            curr = stack.pop();
            k--;
            if (k == 0) {
                return curr.val;
            }

            curr = curr.right;
        }

        return -1;
    }

    public static void main(String[] args) {
        LC0230_KthSmallestElementInABST solver = new LC0230_KthSmallestElementInABST();
        TreeNode root = new TreeNode(3,
            new TreeNode(1, null, new TreeNode(2)),
            new TreeNode(4)
        );
        System.out.println("1st smallest: " + solver.kthSmallest(root, 1)); // Expected: 1
    }
}
"""),
        ("LC0236_LowestCommonAncestorOfABinaryTree.java", """/**
 * LeetCode 236: Lowest Common Ancestor of a Binary Tree
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
 *
 * Approach: Post-Order DFS with Subtree Node Discovery
 * Time Complexity: O(N)
 * Space Complexity: O(H) where H is tree height
 */
public class LC0236_LowestCommonAncestorOfABinaryTree {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) {
            return root;
        }

        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);

        if (left != null && right != null) {
            return root;
        }

        return (left != null) ? left : right;
    }

    public static void main(String[] args) {
        LC0236_LowestCommonAncestorOfABinaryTree solver =
            new LC0236_LowestCommonAncestorOfABinaryTree();
        TreeNode root = new TreeNode(3);
        TreeNode p = new TreeNode(5);
        TreeNode q = new TreeNode(1);
        root.left = p;
        root.right = q;

        TreeNode lca = solver.lowestCommonAncestor(root, p, q);
        System.out.println("LCA val: " + lca.val); // Expected: 3
    }
}
"""),
    ],

    # ---------------- DAY 6: BACKTRACKING & 1D/2D DP ----------------
    "day6": [
        ("LC0017_LetterCombinationsOfAPhoneNumber.java", """import java.util.ArrayList;
import java.util.List;

/**
 * LeetCode 17: Letter Combinations of a Phone Number
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 *
 * Approach: Backtracking with Digit-to-Letter Mapping
 * Time Complexity: O(4^N)
 * Space Complexity: O(N)
 */
public class LC0017_LetterCombinationsOfAPhoneNumber {

    private static final String[] MAPPINGS = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.isEmpty()) {
            return result;
        }

        backtrack(digits, 0, new StringBuilder(), result);
        return result;
    }

    private void backtrack(String digits, int index, StringBuilder sb, List<String> result) {
        if (index == digits.length()) {
            result.add(sb.toString());
            return;
        }

        String letters = MAPPINGS[digits.charAt(index) - '0'];
        for (int i = 0; i < letters.length(); i++) {
            sb.append(letters.charAt(i));
            backtrack(digits, index + 1, sb, result);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    public static void main(String[] args) {
        LC0017_LetterCombinationsOfAPhoneNumber solver =
            new LC0017_LetterCombinationsOfAPhoneNumber();
        System.out.println("Combinations for 23: " + solver.letterCombinations("23"));
        // Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    }
}
"""),
        ("LC0039_CombinationSum.java", """import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * LeetCode 39: Combination Sum
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/combination-sum/
 *
 * Approach: Backtracking with unlimited element reuse
 * Time Complexity: O(2^(Target / Min_Candidate))
 * Space Complexity: O(Target / Min_Candidate)
 */
public class LC0039_CombinationSum {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] candidates, int remain, int start, List<Integer> current, List<List<Integer>> result) {
        if (remain == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remain) {
                break; // Candidates are sorted; remaining items exceed target
            }

            current.add(candidates[i]);
            backtrack(candidates, remain - candidates[i], i, current, result);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        LC0039_CombinationSum solver = new LC0039_CombinationSum();
        int[] candidates = {2, 3, 6, 7};
        System.out.println("Target 7: " + solver.combinationSum(candidates, 7));
        // Expected: [[2, 2, 3], [7]]
    }
}
"""),
        ("LC0040_CombinationSumII.java", """import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * LeetCode 40: Combination Sum II
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/combination-sum-ii/
 *
 * Approach: Backtracking with duplicate skipping
 * Time Complexity: O(2^N)
 * Space Complexity: O(N)
 */
public class LC0040_CombinationSumII {

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] candidates, int remain, int start, List<Integer> current, List<List<Integer>> result) {
        if (remain == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remain) {
                break;
            }
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue; // Skip duplicate combinations at same depth
            }

            current.add(candidates[i]);
            backtrack(candidates, remain - candidates[i], i + 1, current, result);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        LC0040_CombinationSumII solver = new LC0040_CombinationSumII();
        int[] candidates = {10, 1, 2, 7, 6, 1, 5};
        System.out.println("Target 8: " + solver.combinationSum2(candidates, 8));
        // Expected: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    }
}
"""),
        ("LC0064_MinimumPathSum.java", """/**
 * LeetCode 64: Minimum Path Sum
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/minimum-path-sum/
 *
 * Approach: In-Place 2D Dynamic Programming
 * Time Complexity: O(M * N)
 * Space Complexity: O(1) in-place
 */
public class LC0064_MinimumPathSum {

    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        // Initialize first row
        for (int j = 1; j < n; j++) {
            grid[0][j] += grid[0][j - 1];
        }

        // Initialize first column
        for (int i = 1; i < m; i++) {
            grid[i][0] += grid[i - 1][0];
        }

        // Fill remaining table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
            }
        }

        return grid[m - 1][n - 1];
    }

    public static void main(String[] args) {
        LC0064_MinimumPathSum solver = new LC0064_MinimumPathSum();
        int[][] grid = {
            {1, 3, 1},
            {1, 5, 1},
            {4, 2, 1}
        };
        System.out.println("Min path sum: " + solver.minPathSum(grid)); // Expected: 7 (1 -> 3 -> 1 -> 1 -> 1)
    }
}
"""),
        ("LC0091_DecodeWays.java", """/**
 * LeetCode 91: Decode Ways
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/decode-ways/
 *
 * Approach: 1D Constant Space Dynamic Programming
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0091_DecodeWays {

    public int numDecodings(String s) {
        if (s == null || s.isEmpty() || s.charAt(0) == '0') {
            return 0;
        }

        int prev2 = 1; // dp[i - 2]
        int prev1 = 1; // dp[i - 1]

        for (int i = 1; i < s.length(); i++) {
            int current = 0;
            int singleDigit = s.charAt(i) - '0';
            int twoDigits = Integer.parseInt(s.substring(i - 1, i + 1));

            if (singleDigit >= 1) {
                current += prev1;
            }
            if (twoDigits >= 10 && twoDigits <= 26) {
                current += prev2;
            }

            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }

    public static void main(String[] args) {
        LC0091_DecodeWays solver = new LC0091_DecodeWays();
        System.out.println("Decodings '12': " + solver.numDecodings("12")); // Expected: 2 ("AB", "L")
        System.out.println("Decodings '226': " + solver.numDecodings("226")); // Expected: 3
    }
}
"""),
        ("LC0120_Triangle.java", """import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * LeetCode 120: Triangle
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/triangle/
 *
 * Approach: Bottom-up 1D Dynamic Programming
 * Time Complexity: O(N^2)
 * Space Complexity: O(N)
 */
public class LC0120_Triangle {

    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[] dp = new int[n];

        // Seed DP table with the bottom row
        for (int j = 0; j < n; j++) {
            dp[j] = triangle.get(n - 1).get(j);
        }

        // Collapse upwards towards the apex
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                dp[j] = triangle.get(i).get(j) + Math.min(dp[j], dp[j + 1]);
            }
        }

        return dp[0];
    }

    public static void main(String[] args) {
        LC0120_Triangle solver = new LC0120_Triangle();
        List<List<Integer>> triangle = new ArrayList<>();
        triangle.add(Arrays.asList(2));
        triangle.add(Arrays.asList(3, 4));
        triangle.add(Arrays.asList(6, 5, 7));
        triangle.add(Arrays.asList(4, 1, 8, 3));

        System.out.println("Min total: " + solver.minimumTotal(triangle)); // Expected: 11 (2 + 3 + 5 + 1)
    }
}
"""),
    ],

    # ---------------- DAY 7: ADVANCED DP, GRAPHS & INTERVALS ----------------
    "day7": [
        ("LC0072_EditDistance.java", """/**
 * LeetCode 72: Edit Distance
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/edit-distance/
 *
 * Approach: 2D Space-Optimized Dynamic Programming (Levenshtein Distance)
 * Time Complexity: O(M * N)
 * Space Complexity: O(N)
 */
public class LC0072_EditDistance {

    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        int[] dp = new int[n + 1];

        for (int j = 0; j <= n; j++) {
            dp[j] = j;
        }

        for (int i = 1; i <= m; i++) {
            int prevDiagonal = dp[0];
            dp[0] = i;

            for (int j = 1; j <= n; j++) {
                int temp = dp[j];
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[j] = prevDiagonal;
                } else {
                    dp[j] = 1 + Math.min(prevDiagonal, Math.min(dp[j], dp[j - 1]));
                }
                prevDiagonal = temp;
            }
        }

        return dp[n];
    }

    public static void main(String[] args) {
        LC0072_EditDistance solver = new LC0072_EditDistance();
        System.out.println("Dist 'horse' -> 'ros': " + solver.minDistance("horse", "ros")); // Expected: 3
    }
}
"""),
        ("LC0210_CourseScheduleII.java", """import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;

/**
 * LeetCode 210: Course Schedule II
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/course-schedule-ii/
 *
 * Approach: Topological Sort via Kahn's Algorithm (BFS with In-Degrees)
 * Time Complexity: O(V + E)
 * Space Complexity: O(V + E)
 */
public class LC0210_CourseScheduleII {

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] inDegree = new int[numCourses];

        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] pre : prerequisites) {
            adj.get(pre[1]).add(pre[0]);
            inDegree[pre[0]]++;
        }

        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }

        int[] order = new int[numCourses];
        int index = 0;

        while (!queue.isEmpty()) {
            int course = queue.poll();
            order[index++] = course;

            for (int next : adj.get(course)) {
                inDegree[next]--;
                if (inDegree[next] == 0) {
                    queue.offer(next);
                }
            }
        }

        return (index == numCourses) ? order : new int[]{};
    }

    public static void main(String[] args) {
        LC0210_CourseScheduleII solver = new LC0210_CourseScheduleII();
        int[][] prereqs = {{1, 0}, {2, 0}, {3, 1}, {3, 2}};
        System.out.println("Order: " + Arrays.toString(solver.findOrder(4, prereqs)));
        // Expected: [0, 1, 2, 3] or [0, 2, 1, 3]
    }
}
"""),
        ("LC0322_CoinChange.java", """import java.util.Arrays;

/**
 * LeetCode 322: Coin Change
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/coin-change/
 *
 * Approach: Bottom-up 1D Dynamic Programming (Unbounded Knapsack)
 * Time Complexity: O(Amount * Coins.length)
 * Space Complexity: O(Amount)
 */
public class LC0322_CoinChange {

    public int coinChange(int[] coins, int amount) {
        int max = amount + 1;
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, max);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }

    public static void main(String[] args) {
        LC0322_CoinChange solver = new LC0322_CoinChange();
        int[] coins = {1, 2, 5};
        System.out.println("Min coins for 11: " + solver.coinChange(coins, 11)); // Expected: 3 (5 + 5 + 1)
    }
}
"""),
        ("LC0416_PartitionEqualSubsetSum.java", """/**
 * LeetCode 416: Partition Equal Subset Sum
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/partition-equal-subset-sum/
 *
 * Approach: 0/1 Knapsack Dynamic Programming with 1D Bitwise/Array Space Optimization
 * Time Complexity: O(N * Target)
 * Space Complexity: O(Target)
 */
public class LC0416_PartitionEqualSubsetSum {

    public boolean canPartition(int[] nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        // An odd total sum can never be divided into two equal integers
        if (totalSum % 2 != 0) {
            return false;
        }

        int target = totalSum / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;

        for (int num : nums) {
            for (int j = target; j >= num; j--) {
                dp[j] = dp[j] || dp[j - num];
            }
        }

        return dp[target];
    }

    public static void main(String[] args) {
        LC0416_PartitionEqualSubsetSum solver = new LC0416_PartitionEqualSubsetSum();
        int[] nums = {1, 5, 11, 5};
        System.out.println("Can partition: " + solver.canPartition(nums)); // Expected: true ([1, 5, 5] and [11])
    }
}
"""),
        ("LC0424_LongestRepeatingCharacterReplacement.java", """/**
 * LeetCode 424: Longest Repeating Character Replacement
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/longest-repeating-character-replacement/
 *
 * Approach: Sliding Window with Maximum Character Frequency Tracking
 * Time Complexity: O(N)
 * Space Complexity: O(1) (26 uppercase English letters)
 */
public class LC0424_LongestRepeatingCharacterReplacement {

    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int left = 0;
        int maxFrequency = 0;
        int maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            maxFrequency = Math.max(maxFrequency, ++count[s.charAt(right) - 'A']);

            // If window size minus max frequency > k, shrink window
            while ((right - left + 1) - maxFrequency > k) {
                count[s.charAt(left) - 'A']--;
                left++;
            }

            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }

    public static void main(String[] args) {
        LC0424_LongestRepeatingCharacterReplacement solver =
            new LC0424_LongestRepeatingCharacterReplacement();
        System.out.println("Result: " + solver.characterReplacement("AABABBA", 1)); // Expected: 4
    }
}
"""),
        ("LC0435_NonOverlappingIntervals.java", """import java.util.Arrays;

/**
 * LeetCode 435: Non-overlapping Intervals
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/non-overlapping-intervals/
 *
 * Approach: Greedy Activity Selection (Sort by End Time)
 * Time Complexity: O(N log N)
 * Space Complexity: O(1)
 */
public class LC0435_NonOverlappingIntervals {

    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }

        // Sort by end time ascending
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));

        int removedCount = 0;
        int lastEnd = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < lastEnd) {
                // Overlap detected: greedily discard the one ending later
                removedCount++;
            } else {
                lastEnd = intervals[i][1];
            }
        }

        return removedCount;
    }

    public static void main(String[] args) {
        LC0435_NonOverlappingIntervals solver = new LC0435_NonOverlappingIntervals();
        int[][] intervals = {{1, 2}, {2, 3}, {3, 4}, {1, 3}};
        System.out.println("Intervals to remove: " + solver.eraseOverlapIntervals(intervals)); // Expected: 1
    }
}
"""),
    ]
}

def main():
    total_written = 0
    for day, files in DATA.items():
        day_dir = os.path.join(BASE_DIR, day)
        os.makedirs(day_dir, exist_ok=True)
        for fname, code in files:
            fpath = os.path.join(day_dir, fname)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(code.strip() + "\n")
            total_written += 1
            print(f"[{day}] Wrote {fname}")

    print(f"Total files written: {total_written}")

if __name__ == "__main__":
    main()
