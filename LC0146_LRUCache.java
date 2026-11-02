import java.util.HashMap;
import java.util.Map;

/**
 * LeetCode 146: LRU Cache
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/lru-cache/
 *
 * Approach: Doubly Linked List + Hash Map
 * Time Complexity: O(1) for both get and put
 * Space Complexity: O(capacity)
 */
public class LC0146_LRUCache {

    static class DNode {
        int key, value;
        DNode prev, next;
        DNode() {}
        DNode(int key, int value) { this.key = key; this.value = value; }
    }

    private final int capacity;
    private final Map<Integer, DNode> cache = new HashMap<>();
    private final DNode head = new DNode();
    private final DNode tail = new DNode();

    public LC0146_LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        DNode node = cache.get(key);
        if (node == null) return -1;
        moveToHead(node);
        return node.value;
    }

    public void put(int key, int value) {
        DNode node = cache.get(key);
        if (node != null) {
            node.value = value;
            moveToHead(node);
        } else {
            DNode newNode = new DNode(key, value);
            cache.put(key, newNode);
            addNode(newNode);

            if (cache.size() > capacity) {
                DNode tailNode = popTail();
                cache.remove(tailNode.key);
            }
        }
    }

    private void addNode(DNode node) {
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    }

    private void removeNode(DNode node) {
        DNode prev = node.prev;
        DNode next = node.next;
        prev.next = next;
        next.prev = prev;
    }

    private void moveToHead(DNode node) {
        removeNode(node);
        addNode(node);
    }

    private DNode popTail() {
        DNode res = tail.prev;
        removeNode(res);
        return res;
    }

    public static void main(String[] args) {
        LC0146_LRUCache lRUCache = new LC0146_LRUCache(2);
        lRUCache.put(1, 1);
        lRUCache.put(2, 2);
        System.out.println("get(1): " + lRUCache.get(1)); // returns 1
        lRUCache.put(3, 3); // evicts key 2
        System.out.println("get(2): " + lRUCache.get(2)); // returns -1 (not found)
        lRUCache.put(4, 4); // evicts key 1
        System.out.println("get(1): " + lRUCache.get(1)); // returns -1 (not found)
        System.out.println("get(3): " + lRUCache.get(3)); // returns 3
        System.out.println("get(4): " + lRUCache.get(4)); // returns 4
    }
}
