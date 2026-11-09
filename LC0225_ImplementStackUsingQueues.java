import java.util.LinkedList;
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
