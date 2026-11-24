/**
 * Problem: 421. Maximum XOR of Two Numbers in an Array
 * Difficulty: Medium
 * Category: Array, Hash Table, Bit Manipulation, Trie
 *
 * Algorithm:
 * Bitwise Trie storing 32-bit binary representations.
 * For each number, greedily follow opposite bit branch to maximize XOR product.
 *
 * Time Complexity: O(32 * N) = O(N)
 * Space Complexity: O(32 * N) = O(N)
 */
public class LC0421_MaximumXOR {

    static class TrieNode {
        TrieNode[] ch = new TrieNode[2];
    }

    public int findMaximumXOR(int[] nums) {
        TrieNode root = new TrieNode();

        for (int n : nums) {
            TrieNode cur = root;
            for (int i = 31; i >= 0; i--) {
                int bit = (n >> i) & 1;
                if (cur.ch[bit] == null) cur.ch[bit] = new TrieNode();
                cur = cur.ch[bit];
            }
        }

        int maxXor = 0;
        for (int n : nums) {
            TrieNode cur = root;
            int xor = 0;
            for (int i = 31; i >= 0; i--) {
                int bit = (n >> i) & 1;
                int want = 1 - bit;
                if (cur.ch[want] != null) {
                    xor |= (1 << i);
                    cur = cur.ch[want];
                } else {
                    cur = cur.ch[bit];
                }
            }
            maxXor = Math.max(maxXor, xor);
        }
        return maxXor;
    }

    public static void main(String[] args) {
        LC0421_MaximumXOR sol = new LC0421_MaximumXOR();
        System.out.println(sol.findMaximumXOR(new int[]{3, 10, 5, 25, 2, 8})); // 28
    }
}
