import java.util.ArrayDeque;
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
