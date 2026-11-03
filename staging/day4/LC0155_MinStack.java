import java.util.ArrayDeque;
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
