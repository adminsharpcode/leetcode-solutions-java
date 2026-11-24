"""
build_full_week3_suite.py
Complete generator for Week 3 (42 LeetCode Java problems across 7 days)
+ Intelligent Auto-Detector & Runner scripts.
"""

import os
import sys

ROOT = r"E:\LeetCode-Solutions-Java"

PROBLEMS = {
    # -------------------------------------------------------------
    # Day 1: Graphs & BFS / Union Find
    # -------------------------------------------------------------
    1: [
        ("LC0127_WordLadder.java", "LC0127 Word Ladder", """import java.util.*;

/**
 * Problem: 127. Word Ladder
 * Difficulty: Hard
 * Category: Breadth-First Search, Hash Table, String
 *
 * Algorithm:
 * Bidirectional or standard BFS level-by-level queue.
 * Convert wordList to HashSet for O(1) removals.
 * For each word, mutate every character 'a'-'z' and check membership.
 *
 * Time Complexity: O(M^2 * N) where M is word length and N is word list size
 * Space Complexity: O(M * N)
 */
public class LC0127_WordLadder {

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);
        if (!wordSet.contains(endWord)) return 0;

        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        int level = 1;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String word = queue.poll();
                char[] chars = word.toCharArray();

                for (int j = 0; j < chars.length; j++) {
                    char orig = chars[j];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == orig) continue;
                        chars[j] = c;
                        String next = new String(chars);

                        if (next.equals(endWord)) return level + 1;
                        if (wordSet.remove(next)) {
                            queue.offer(next);
                        }
                    }
                    chars[j] = orig;
                }
            }
            level++;
        }
        return 0;
    }

    public static void main(String[] args) {
        LC0127_WordLadder sol = new LC0127_WordLadder();
        List<String> wl = Arrays.asList("hot", "dot", "dog", "lot", "log", "cog");
        int res = sol.ladderLength("hit", "cog", wl);
        System.out.println("Word Ladder length: " + res); // 5
    }
}
"""),
        ("LC0130_SurroundedRegions.java", "LC0130 Surrounded Regions", """/**
 * Problem: 130. Surrounded Regions
 * Difficulty: Medium
 * Category: Depth-First Search, Breadth-First Search, Matrix
 *
 * Algorithm:
 * Boundary DFS traversal: all 'O' cells connected to border cannot be captured.
 * Traverse from all border cells, mark visited 'O' as temporary 'S'.
 * Flip all remaining 'O' to 'X' (captured), flip 'S' back to 'O'.
 *
 * Time Complexity: O(M * N)
 * Space Complexity: O(M * N) recursion stack
 */
public class LC0130_SurroundedRegions {

    public void solve(char[][] board) {
        if (board == null || board.length == 0) return;
        int m = board.length, n = board[0].length;

        for (int i = 0; i < m; i++) {
            dfs(board, i, 0, m, n);
            dfs(board, i, n - 1, m, n);
        }
        for (int j = 0; j < n; j++) {
            dfs(board, 0, j, m, n);
            dfs(board, m - 1, j, m, n);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                else if (board[i][j] == 'S') board[i][j] = 'O';
            }
        }
    }

    private void dfs(char[][] b, int r, int c, int m, int n) {
        if (r < 0 || r >= m || c < 0 || c >= n || b[r][c] != 'O') return;
        b[r][c] = 'S';
        dfs(b, r + 1, c, m, n);
        dfs(b, r - 1, c, m, n);
        dfs(b, r, c + 1, m, n);
        dfs(b, r, c - 1, m, n);
    }

    public static void main(String[] args) {
        LC0130_SurroundedRegions sol = new LC0130_SurroundedRegions();
        char[][] board = {
            {'X','X','X','X'},
            {'X','O','O','X'},
            {'X','X','O','X'},
            {'X','O','X','X'}
        };
        sol.solve(board);
        for (char[] row : board) System.out.println(new String(row));
    }
}
"""),
        ("LC0261_GraphValidTree.java", "LC0261 Graph Valid Tree", """/**
 * Problem: 261. Graph Valid Tree
 * Difficulty: Medium
 * Category: Graph, Union Find, Breadth-First Search
 *
 * Algorithm:
 * A graph of N nodes is a valid tree iff it has exactly N - 1 edges and no cycles.
 * Use Union-Find: for each edge (u, v), find roots. If root(u) == root(v), cycle exists.
 *
 * Time Complexity: O(N * alpha(N))
 * Space Complexity: O(N)
 */
public class LC0261_GraphValidTree {

    private int[] parent;

    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false;

        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        for (int[] edge : edges) {
            int rootA = find(edge[0]);
            int rootB = find(edge[1]);
            if (rootA == rootB) return false;
            parent[rootA] = rootB;
        }
        return true;
    }

    private int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    public static void main(String[] args) {
        LC0261_GraphValidTree sol = new LC0261_GraphValidTree();
        int[][] edges = {{0,1}, {0,2}, {0,3}, {1,4}};
        System.out.println("Valid tree: " + sol.validTree(5, edges)); // true
    }
}
"""),
        ("LC0310_MinimumHeightTrees.java", "LC0310 Minimum Height Trees", """import java.util.*;

/**
 * Problem: 310. Minimum Height Trees
 * Difficulty: Medium
 * Category: Tree, Breadth-First Search, Graph, Topological Sort
 *
 * Algorithm:
 * Prune leaves inward level by level until 1 or 2 nodes remain (the centroid(s)).
 * Start with all nodes having degree 1, strip leaves until remaining <= 2.
 *
 * Time Complexity: O(V + E)
 * Space Complexity: O(V + E)
 */
public class LC0310_MinimumHeightTrees {

    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) return Collections.singletonList(0);

        List<Set<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new HashSet<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        List<Integer> leaves = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (adj.get(i).size() == 1) leaves.add(i);
        }

        int remaining = n;
        while (remaining > 2) {
            remaining -= leaves.size();
            List<Integer> newLeaves = new ArrayList<>();
            for (int leaf : leaves) {
                int neighbor = adj.get(leaf).iterator().next();
                adj.get(neighbor).remove(leaf);
                if (adj.get(neighbor).size() == 1) newLeaves.add(neighbor);
            }
            leaves = newLeaves;
        }
        return leaves;
    }

    public static void main(String[] args) {
        LC0310_MinimumHeightTrees sol = new LC0310_MinimumHeightTrees();
        int[][] edges = {{1,0}, {1,2}, {1,3}};
        System.out.println("MHT roots: " + sol.findMinHeightTrees(4, edges)); // [1]
    }
}
"""),
        ("LC0399_EvaluateDivision.java", "LC0399 Evaluate Division", """import java.util.*;

/**
 * Problem: 399. Evaluate Division
 * Difficulty: Medium
 * Category: Graph, Depth-First Search, Breadth-First Search, Union Find
 *
 * Algorithm:
 * Model variables as graph nodes. Edge (u -> v) has weight val, (v -> u) has 1/val.
 * For each query (src, dst), perform DFS/BFS to find path product.
 *
 * Time Complexity: O(Q * (V + E))
 * Space Complexity: O(V + E)
 */
public class LC0399_EvaluateDivision {

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> graph = new HashMap<>();

        for (int i = 0; i < equations.size(); i++) {
            String u = equations.get(i).get(0);
            String v = equations.get(i).get(1);
            double val = values[i];

            graph.computeIfAbsent(u, k -> new HashMap<>()).put(v, val);
            graph.computeIfAbsent(v, k -> new HashMap<>()).put(u, 1.0 / val);
        }

        double[] res = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            String src = queries.get(i).get(0);
            String dst = queries.get(i).get(1);
            res[i] = dfs(graph, src, dst, new HashSet<>());
        }
        return res;
    }

    private double dfs(Map<String, Map<String, Double>> g, String cur, String target, Set<String> visited) {
        if (!g.containsKey(cur) || !g.containsKey(target)) return -1.0;
        if (cur.equals(target)) return 1.0;

        visited.add(cur);
        for (Map.Entry<String, Double> neighbor : g.get(cur).entrySet()) {
            if (!visited.contains(neighbor.getKey())) {
                double sub = dfs(g, neighbor.getKey(), target, visited);
                if (sub != -1.0) return sub * neighbor.getValue();
            }
        }
        return -1.0;
    }

    public static void main(String[] args) {
        LC0399_EvaluateDivision sol = new LC0399_EvaluateDivision();
        List<List<String>> eq = Arrays.asList(Arrays.asList("a","b"), Arrays.asList("b","c"));
        double[] vals = {2.0, 3.0};
        List<List<String>> queries = Arrays.asList(Arrays.asList("a","c"), Arrays.asList("b","a"));
        System.out.println(Arrays.toString(sol.calcEquation(eq, vals, queries))); // [6.0, 0.5]
    }
}
"""),
        ("LC0547_NumberOfProvinces.java", "LC0547 Number of Provinces", """/**
 * Problem: 547. Number of Provinces
 * Difficulty: Medium
 * Category: Depth-First Search, Breadth-First Search, Union Find, Graph
 *
 * Algorithm:
 * Disjoint Set Union (DSU) or standard visited DFS over n cities.
 * For each city, if not visited, launch DFS to mark all transitively connected cities.
 * Increment province counter per connected component.
 *
 * Time Complexity: O(N^2)
 * Space Complexity: O(N)
 */
public class LC0547_NumberOfProvinces {

    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(isConnected, visited, i, n);
                count++;
            }
        }
        return count;
    }

    private void dfs(int[][] matrix, boolean[] visited, int i, int n) {
        visited[i] = true;
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 1 && !visited[j]) {
                dfs(matrix, visited, j, n);
            }
        }
    }

    public static void main(String[] args) {
        LC0547_NumberOfProvinces sol = new LC0547_NumberOfProvinces();
        int[][] conn = {{1,1,0},{1,1,0},{0,0,1}};
        System.out.println("Provinces: " + sol.findCircleNum(conn)); // 2
    }
}
""")
    ],

    # -------------------------------------------------------------
    # Day 2: Stack & Monotonic Stack
    # -------------------------------------------------------------
    2: [
        ("LC0085_MaximalRectangle.java", "LC0085 Maximal Rectangle", """import java.util.*;

/**
 * Problem: 85. Maximal Rectangle
 * Difficulty: Hard
 * Category: Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
 *
 * Algorithm:
 * Maintain running histogram heights row by row.
 * For each row, calculate largest rectangle in histogram via Monotonic Stack in O(N).
 *
 * Time Complexity: O(M * N)
 * Space Complexity: O(N)
 */
public class LC0085_MaximalRectangle {

    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0) return 0;
        int cols = matrix[0].length;
        int[] heights = new int[cols];
        int maxArea = 0;

        for (char[] row : matrix) {
            for (int j = 0; j < cols; j++) {
                heights[j] = row[j] == '1' ? heights[j] + 1 : 0;
            }
            maxArea = Math.max(maxArea, largestHistogram(heights));
        }
        return maxArea;
    }

    private int largestHistogram(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int max = 0;
        for (int i = 0; i <= heights.length; i++) {
            int h = (i == heights.length) ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > h) {
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                max = Math.max(max, height * width);
            }
            stack.push(i);
        }
        return max;
    }

    public static void main(String[] args) {
        LC0085_MaximalRectangle sol = new LC0085_MaximalRectangle();
        char[][] mat = {
            {'1','0','1','0','0'},
            {'1','0','1','1','1'},
            {'1','1','1','1','1'},
            {'1','0','0','1','0'}
        };
        System.out.println("Maximal Rectangle: " + sol.maximalRectangle(mat)); // 6
    }
}
"""),
        ("LC0316_RemoveDuplicateLetters.java", "LC0316 Remove Duplicate Letters", """import java.util.*;

/**
 * Problem: 316. Remove Duplicate Letters
 * Difficulty: Medium
 * Category: String, Stack, Greedy, Monotonic Stack
 *
 * Algorithm:
 * Greedily maintain monotonic increasing stack.
 * Track frequency of remaining chars; if stack top > current and can appear later, pop it.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1) auxiliary (26 alphabet characters)
 */
public class LC0316_RemoveDuplicateLetters {

    public String removeDuplicateLetters(String s) {
        int[] count = new int[26];
        boolean[] inStack = new boolean[26];
        for (char c : s.toCharArray()) count[c - 'a']++;

        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            count[c - 'a']--;
            if (inStack[c - 'a']) continue;

            while (!stack.isEmpty() && stack.peek() > c && count[stack.peek() - 'a'] > 0) {
                inStack[stack.pop() - 'a'] = false;
            }
            stack.push(c);
            inStack[c - 'a'] = true;
        }

        StringBuilder sb = new StringBuilder();
        for (char c : stack) sb.append(c);
        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        LC0316_RemoveDuplicateLetters sol = new LC0316_RemoveDuplicateLetters();
        System.out.println(sol.removeDuplicateLetters("bcabc")); // abc
        System.out.println(sol.removeDuplicateLetters("cbacdcbc")); // acdb
    }
}
"""),
        ("LC0394_DecodeString.java", "LC0394 Decode String", """import java.util.*;

/**
 * Problem: 394. Decode String
 * Difficulty: Medium
 * Category: String, Stack, Recursion
 *
 * Algorithm:
 * Two stacks: one for counts k, one for intermediate StringBuilders.
 * On '[', push current string and multiplier. On ']', pop multiplier and repeat buffer.
 *
 * Time Complexity: O(maxK * N)
 * Space Complexity: O(N)
 */
public class LC0394_DecodeString {

    public String decodeString(String s) {
        Deque<Integer> countStack = new ArrayDeque<>();
        Deque<StringBuilder> strStack = new ArrayDeque<>();
        StringBuilder current = new StringBuilder();
        int k = 0;

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                k = k * 10 + (c - '0');
            } else if (c == '[') {
                countStack.push(k);
                strStack.push(current);
                current = new StringBuilder();
                k = 0;
            } else if (c == ']') {
                StringBuilder decoded = current;
                current = strStack.pop();
                int repeat = countStack.pop();
                while (repeat-- > 0) current.append(decoded);
            } else {
                current.append(c);
            }
        }
        return current.toString();
    }

    public static void main(String[] args) {
        LC0394_DecodeString sol = new LC0394_DecodeString();
        System.out.println(sol.decodeString("3[a]2[bc]")); // aaabcbc
        System.out.println(sol.decodeString("3[a2[c]]"));  // accaccacc
    }
}
"""),
        ("LC0496_NextGreaterElementI.java", "LC0496 Next Greater Element I", """import java.util.*;

/**
 * Problem: 496. Next Greater Element I
 * Difficulty: Easy
 * Category: Array, Hash Table, Stack, Monotonic Stack
 *
 * Algorithm:
 * Use monotonic decreasing stack on nums2 to map each element to its next greater element.
 * Lookup answers for nums1 in O(1) via HashMap.
 *
 * Time Complexity: O(nums1.length + nums2.length)
 * Space Complexity: O(nums2.length)
 */
public class LC0496_NextGreaterElementI {

    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap<>();
        Deque<Integer> stack = new ArrayDeque<>();

        for (int num : nums2) {
            while (!stack.isEmpty() && stack.peek() < num) {
                map.put(stack.pop(), num);
            }
            stack.push(num);
        }

        int[] res = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            res[i] = map.getOrDefault(nums1[i], -1);
        }
        return res;
    }

    public static void main(String[] args) {
        LC0496_NextGreaterElementI sol = new LC0496_NextGreaterElementI();
        int[] n1 = {4, 1, 2}, n2 = {1, 3, 4, 2};
        System.out.println(Arrays.toString(sol.nextGreaterElement(n1, n2))); // [-1, 3, -1]
    }
}
"""),
        ("LC0503_NextGreaterElementII.java", "LC0503 Next Greater Element II", """import java.util.*;

/**
 * Problem: 503. Next Greater Element II
 * Difficulty: Medium
 * Category: Array, Stack, Monotonic Stack
 *
 * Algorithm:
 * Circular array: simulate 2 * N iterations using index modulo n.
 * Monotonic decreasing index stack resolves next greater circular element.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0503_NextGreaterElementII {

    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        Arrays.fill(res, -1);
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < 2 * n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i % n]) {
                res[stack.pop()] = nums[i % n];
            }
            if (i < n) stack.push(i);
        }
        return res;
    }

    public static void main(String[] args) {
        LC0503_NextGreaterElementII sol = new LC0503_NextGreaterElementII();
        System.out.println(Arrays.toString(sol.nextGreaterElements(new int[]{1, 2, 1}))); // [2, -1, 2]
    }
}
"""),
        ("LC0739_DailyTemperatures.java", "LC0739 Daily Temperatures", """import java.util.*;

/**
 * Problem: 739. Daily Temperatures
 * Difficulty: Medium
 * Category: Array, Stack, Monotonic Stack
 *
 * Algorithm:
 * Monotonic decreasing stack storing indices.
 * When current temp > stack.peek() temp, pop and distance is cur_idx - popped_idx.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0739_DailyTemperatures {

    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] res = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
                int prev = stack.pop();
                res[prev] = i - prev;
            }
            stack.push(i);
        }
        return res;
    }

    public static void main(String[] args) {
        LC0739_DailyTemperatures sol = new LC0739_DailyTemperatures();
        int[] temps = {73, 74, 75, 71, 69, 72, 76, 73};
        System.out.println(Arrays.toString(sol.dailyTemperatures(temps))); // [1, 1, 4, 2, 1, 1, 0, 0]
    }
}
""")
    ],

    # -------------------------------------------------------------
    # Day 3: Sliding Window & Two Pointers
    # -------------------------------------------------------------
    3: [
        ("LC0030_SubstringConcatenation.java", "LC0030 Substring with Concatenation of All Words", """import java.util.*;

/**
 * Problem: 30. Substring with Concatenation of All Words
 * Difficulty: Hard
 * Category: Hash Table, String, Sliding Window
 *
 * Algorithm:
 * Word length is fixed L, total words C. Window length is L * C.
 * Slide window in steps of L across L possible starting offsets.
 *
 * Time Complexity: O(N * L)
 * Space Complexity: O(C * L)
 */
public class LC0030_SubstringConcatenation {

    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<>();
        if (s == null || words == null || words.length == 0) return res;

        int wordLen = words[0].length(), wordCount = words.length;
        int totalLen = wordLen * wordCount;
        if (s.length() < totalLen) return res;

        Map<String, Integer> wordFreq = new HashMap<>();
        for (String w : words) wordFreq.merge(w, 1, Integer::sum);

        for (int i = 0; i <= s.length() - totalLen; i++) {
            Map<String, Integer> seen = new HashMap<>();
            int j = 0;
            while (j < wordCount) {
                String sub = s.substring(i + j * wordLen, i + (j + 1) * wordLen);
                if (!wordFreq.containsKey(sub)) break;
                seen.merge(sub, 1, Integer::sum);
                if (seen.get(sub) > wordFreq.get(sub)) break;
                j++;
            }
            if (j == wordCount) res.add(i);
        }
        return res;
    }

    public static void main(String[] args) {
        LC0030_SubstringConcatenation sol = new LC0030_SubstringConcatenation();
        System.out.println(sol.findSubstring("barfoothefoobarman", new String[]{"foo", "bar"})); // [0, 9]
    }
}
"""),
        ("LC0159_LongestSubstringTwoDistinct.java", "LC0159 Longest Substring with At Most Two Distinct Characters", """import java.util.*;

/**
 * Problem: 159. Longest Substring with At Most Two Distinct Characters
 * Difficulty: Medium
 * Category: Hash Table, String, Sliding Window
 *
 * Algorithm:
 * Sliding window maintaining character frequency map.
 * Expand right pointer; shrink left pointer whenever map.size() > 2.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0159_LongestSubstringTwoDistinct {

    public int lengthOfLongestSubstringTwoDistinct(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int left = 0, maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            map.merge(s.charAt(right), 1, Integer::sum);
            while (map.size() > 2) {
                char lc = s.charAt(left++);
                map.put(lc, map.get(lc) - 1);
                if (map.get(lc) == 0) map.remove(lc);
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }

    public static void main(String[] args) {
        LC0159_LongestSubstringTwoDistinct sol = new LC0159_LongestSubstringTwoDistinct();
        System.out.println(sol.lengthOfLongestSubstringTwoDistinct("eceba")); // 3 ("ece")
    }
}
"""),
        ("LC0239_SlidingWindowMaximum.java", "LC0239 Sliding Window Maximum", """import java.util.*;

/**
 * Problem: 239. Sliding Window Maximum
 * Difficulty: Hard
 * Category: Array, Queue, Sliding Window, Heap, Monotonic Queue
 *
 * Algorithm:
 * Monotonic decreasing deque storing indices.
 * Remove indices falling out of window [i - k + 1, i].
 * Maintain strictly decreasing order in deque; first element is always window max.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(k)
 */
public class LC0239_SlidingWindowMaximum {

    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] res = new int[n - k + 1];
        Deque<Integer> dq = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            while (!dq.isEmpty() && dq.peekFirst() < i - k + 1) dq.pollFirst();
            while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i]) dq.pollLast();

            dq.offerLast(i);
            if (i >= k - 1) {
                res[i - k + 1] = nums[dq.peekFirst()];
            }
        }
        return res;
    }

    public static void main(String[] args) {
        LC0239_SlidingWindowMaximum sol = new LC0239_SlidingWindowMaximum();
        int[] nums = {1, 3, -1, -3, 5, 3, 6, 7};
        System.out.println(Arrays.toString(sol.maxSlidingWindow(nums, 3))); // [3,3,5,5,6,7]
    }
}
"""),
        ("LC0567_PermutationInString.java", "LC0567 Permutation in String", """/**
 * Problem: 567. Permutation in String
 * Difficulty: Medium
 * Category: Hash Table, Two Pointers, String, Sliding Window
 *
 * Algorithm:
 * Fixed-size sliding window of length s1.length() over s2.
 * Maintain 26-char frequency difference or match counter.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0567_PermutationInString {

    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;

        int[] count1 = new int[26];
        int[] count2 = new int[26];

        for (int i = 0; i < s1.length(); i++) {
            count1[s1.charAt(i) - 'a']++;
            count2[s2.charAt(i) - 'a']++;
        }

        if (matches(count1, count2)) return true;

        for (int i = s1.length(); i < s2.length(); i++) {
            count2[s2.charAt(i) - 'a']++;
            count2[s2.charAt(i - s1.length()) - 'a']--;
            if (matches(count1, count2)) return true;
        }
        return false;
    }

    private boolean matches(int[] c1, int[] c2) {
        for (int i = 0; i < 26; i++) {
            if (c1[i] != c2[i]) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        LC0567_PermutationInString sol = new LC0567_PermutationInString();
        System.out.println(sol.checkInclusion("ab", "eidbaooo")); // true
        System.out.println(sol.checkInclusion("ab", "eidboaoo")); // false
    }
}
"""),
        ("LC0632_SmallestRange.java", "LC0632 Smallest Range Covering Elements from K Lists", """import java.util.*;

/**
 * Problem: 632. Smallest Range Covering Elements from K Lists
 * Difficulty: Hard
 * Category: Array, Hash Table, Greedy, Sliding Window, Sorting, Heap
 *
 * Algorithm:
 * Min-heap of size K containing the current element from each list.
 * Track current maximum across the heap. Range is [minHeap.peek(), maxVal].
 * Advance pointer in the list containing the minimum element.
 *
 * Time Complexity: O(N * log K) where N is total elements across all lists
 * Space Complexity: O(K)
 */
public class LC0632_SmallestRange {

    public int[] smallestRange(List<List<Integer>> nums) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < nums.size(); i++) {
            int val = nums.get(i).get(0);
            pq.offer(new int[]{val, i, 0});
            max = Math.max(max, val);
        }

        int[] res = {pq.peek()[0], max};

        while (true) {
            int[] cur = pq.poll();
            int r = cur[1], c = cur[2];
            if (c + 1 >= nums.get(r).size()) break;

            int next = nums.get(r).get(c + 1);
            pq.offer(new int[]{next, r, c + 1});
            max = Math.max(max, next);

            if (max - pq.peek()[0] < res[1] - res[0]) {
                res[0] = pq.peek()[0];
                res[1] = max;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        LC0632_SmallestRange sol = new LC0632_SmallestRange();
        List<List<Integer>> lists = Arrays.asList(
            Arrays.asList(4,10,15,24,26),
            Arrays.asList(0,9,12,20),
            Arrays.asList(5,18,22,30)
        );
        System.out.println(Arrays.toString(sol.smallestRange(lists))); // [20, 24]
    }
}
"""),
        ("LC0643_MaximumAverageSubarrayI.java", "LC0643 Maximum Average Subarray I", """/**
 * Problem: 643. Maximum Average Subarray I
 * Difficulty: Easy
 * Category: Array, Sliding Window
 *
 * Algorithm:
 * Maintain sliding window of fixed length k.
 * Compute initial sum of first k elements, slide right by adding incoming and subtracting outgoing.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0643_MaximumAverageSubarrayI {

    public double findMaxAverage(int[] nums, int k) {
        double sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];

        double maxSum = sum;
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            maxSum = Math.max(maxSum, sum);
        }
        return maxSum / k;
    }

    public static void main(String[] args) {
        LC0643_MaximumAverageSubarrayI sol = new LC0643_MaximumAverageSubarrayI();
        System.out.println(sol.findMaxAverage(new int[]{1, 12, -5, -6, 50, 3}, 4)); // 12.75
    }
}
""")
    ],

    # -------------------------------------------------------------
    # Day 4: Bit Manipulation & Math
    # -------------------------------------------------------------
    4: [
        ("LC0190_ReverseBits.java", "LC0190 Reverse Bits", """/**
 * Problem: 190. Reverse Bits
 * Difficulty: Easy
 * Category: Divide and Conquer, Bit Manipulation
 *
 * Algorithm:
 * Iterate 32 times: shift result left, append least significant bit of n, shift n right.
 *
 * Time Complexity: O(1) - exactly 32 bit operations
 * Space Complexity: O(1)
 */
public class LC0190_ReverseBits {

    public int reverseBits(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            res = (res << 1) | (n & 1);
            n >>= 1;
        }
        return res;
    }

    public static void main(String[] args) {
        LC0190_ReverseBits sol = new LC0190_ReverseBits();
        System.out.println(sol.reverseBits(43261596)); // 964176192
    }
}
"""),
        ("LC0191_NumberOf1Bits.java", "LC0191 Number of 1 Bits", """/**
 * Problem: 191. Number of 1 Bits
 * Difficulty: Easy
 * Category: Divide and Conquer, Bit Manipulation
 *
 * Algorithm:
 * Brian Kernighan's Algorithm: n = n & (n - 1) flips the lowest set bit to 0.
 *
 * Time Complexity: O(k) where k is the number of 1-bits (<= 32)
 * Space Complexity: O(1)
 */
public class LC0191_NumberOf1Bits {

    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        LC0191_NumberOf1Bits sol = new LC0191_NumberOf1Bits();
        System.out.println(sol.hammingWeight(11));  // 3
        System.out.println(sol.hammingWeight(128)); // 1
    }
}
"""),
        ("LC0231_PowerOfTwo.java", "LC0231 Power of Two", """/**
 * Problem: 231. Power of Two
 * Difficulty: Easy
 * Category: Math, Bit Manipulation, Recursion
 *
 * Algorithm:
 * A positive integer n is a power of 2 iff it has exactly one set bit: (n & (n - 1)) == 0.
 *
 * Time Complexity: O(1)
 * Space Complexity: O(1)
 */
public class LC0231_PowerOfTwo {

    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }

    public static void main(String[] args) {
        LC0231_PowerOfTwo sol = new LC0231_PowerOfTwo();
        System.out.println(sol.isPowerOfTwo(16)); // true
        System.out.println(sol.isPowerOfTwo(3));  // false
    }
}
"""),
        ("LC0260_SingleNumberIII.java", "LC0260 Single Number III", """import java.util.*;

/**
 * Problem: 260. Single Number III
 * Difficulty: Medium
 * Category: Array, Bit Manipulation
 *
 * Algorithm:
 * XOR sum of all elements = a ^ b.
 * Find lowest set bit diff = xor & (-xor) which differs between a and b.
 * Partition array into two buckets by diff bit and XOR each bucket to find a and b.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0260_SingleNumberIII {

    public int[] singleNumber(int[] nums) {
        int xor = 0;
        for (int n : nums) xor ^= n;

        int diff = xor & (-xor);
        int a = 0;
        for (int n : nums) {
            if ((n & diff) != 0) a ^= n;
        }
        return new int[]{a, xor ^ a};
    }

    public static void main(String[] args) {
        LC0260_SingleNumberIII sol = new LC0260_SingleNumberIII();
        System.out.println(Arrays.toString(sol.singleNumber(new int[]{1, 2, 1, 3, 2, 5}))); // [3, 5]
    }
}
"""),
        ("LC0268_MissingNumber.java", "LC0268 Missing Number", """/**
 * Problem: 268. Missing Number
 * Difficulty: Easy
 * Category: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
 *
 * Algorithm:
 * Expected sum from 0..n is n * (n + 1) / 2.
 * Missing number = expected_sum - actual_sum.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0268_MissingNumber {

    public int missingNumber(int[] nums) {
        int n = nums.length;
        int expected = n * (n + 1) / 2;
        for (int num : nums) expected -= num;
        return expected;
    }

    public static void main(String[] args) {
        LC0268_MissingNumber sol = new LC0268_MissingNumber();
        System.out.println(sol.missingNumber(new int[]{3, 0, 1})); // 2
        System.out.println(sol.missingNumber(new int[]{0, 1}));    // 2
    }
}
"""),
        ("LC0371_SumOfTwoIntegers.java", "LC0371 Sum of Two Integers", """/**
 * Problem: 371. Sum of Two Integers
 * Difficulty: Medium
 * Category: Math, Bit Manipulation
 *
 * Algorithm:
 * Addition without +: sum = a ^ b, carry = (a & b) << 1.
 * Repeat until carry is 0.
 *
 * Time Complexity: O(1) - max 32 iterations
 * Space Complexity: O(1)
 */
public class LC0371_SumOfTwoIntegers {

    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }

    public static void main(String[] args) {
        LC0371_SumOfTwoIntegers sol = new LC0371_SumOfTwoIntegers();
        System.out.println(sol.getSum(1, 2)); // 3
        System.out.println(sol.getSum(2, 3)); // 5
    }
}
""")
    ],

    # -------------------------------------------------------------
    # Day 5: Dynamic Programming (2D & State Transitions)
    # -------------------------------------------------------------
    5: [
        ("LC0097_InterleavingString.java", "LC0097 Interleaving String", """/**
 * Problem: 97. Interleaving String
 * Difficulty: Medium
 * Category: String, Dynamic Programming
 *
 * Algorithm:
 * 2D DP: dp[i][j] indicates whether s1[0..i-1] and s2[0..j-1] interleave to form s3[0..i+j-1].
 *
 * Time Complexity: O(M * N)
 * Space Complexity: O(M * N) (or O(N) space optimized)
 */
public class LC0097_InterleavingString {

    public boolean isInterleave(String s1, String s2, String s3) {
        int m = s1.length(), n = s2.length();
        if (m + n != s3.length()) return false;

        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;

        for (int i = 1; i <= m; i++) dp[i][0] = dp[i - 1][0] && s1.charAt(i - 1) == s3.charAt(i - 1);
        for (int j = 1; j <= n; j++) dp[0][j] = dp[0][j - 1] && s2.charAt(j - 1) == s3.charAt(j - 1);

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = (dp[i - 1][j] && s1.charAt(i - 1) == s3.charAt(i + j - 1)) ||
                           (dp[i][j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1));
            }
        }
        return dp[m][n];
    }

    public static void main(String[] args) {
        LC0097_InterleavingString sol = new LC0097_InterleavingString();
        System.out.println(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac")); // true
    }
}
"""),
        ("LC0115_DistinctSubsequences.java", "LC0115 Distinct Subsequences", """/**
 * Problem: 115. Distinct Subsequences
 * Difficulty: Hard
 * Category: String, Dynamic Programming
 *
 * Algorithm:
 * dp[i][j] = count of distinct subsequences of s[0..i-1] matching t[0..j-1].
 * If s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j].
 * Else: dp[i][j] = dp[i-1][j].
 *
 * Time Complexity: O(M * N)
 * Space Complexity: O(M * N)
 */
public class LC0115_DistinctSubsequences {

    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        long[][] dp = new long[m + 1][n + 1];

        for (int i = 0; i <= m; i++) dp[i][0] = 1;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = dp[i - 1][j];
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    dp[i][j] += dp[i - 1][j - 1];
                }
            }
        }
        return (int) dp[m][n];
    }

    public static void main(String[] args) {
        LC0115_DistinctSubsequences sol = new LC0115_DistinctSubsequences();
        System.out.println(sol.numDistinct("rabbbit", "rabbit")); // 3
    }
}
"""),
        ("LC0132_PalindromePartitioningII.java", "LC0132 Palindrome Partitioning II", """/**
 * Problem: 132. Palindrome Partitioning II
 * Difficulty: Hard
 * Category: String, Dynamic Programming
 *
 * Algorithm:
 * Precompute palindrome table pal[i][j] where s[i..j] is palindrome.
 * dp[i] = min cuts for substring s[0..i].
 *
 * Time Complexity: O(N^2)
 * Space Complexity: O(N^2)
 */
public class LC0132_PalindromePartitioningII {

    public int minCut(String s) {
        int n = s.length();
        boolean[][] pal = new boolean[n][n];
        int[] dp = new int[n];

        for (int i = 0; i < n; i++) {
            dp[i] = i;
            for (int j = 0; j <= i; j++) {
                if (s.charAt(j) == s.charAt(i) && (i - j <= 2 || pal[j + 1][i - 1])) {
                    pal[j][i] = true;
                    dp[i] = (j == 0) ? 0 : Math.min(dp[i], dp[j - 1] + 1);
                }
            }
        }
        return dp[n - 1];
    }

    public static void main(String[] args) {
        LC0132_PalindromePartitioningII sol = new LC0132_PalindromePartitioningII();
        System.out.println(sol.minCut("aab")); // 1
    }
}
"""),
        ("LC0188_BestTimeToBuyAndSellStockIV.java", "LC0188 Best Time to Buy and Sell Stock IV", """import java.util.*;

/**
 * Problem: 188. Best Time to Buy and Sell Stock IV
 * Difficulty: Hard
 * Category: Array, Dynamic Programming
 *
 * Algorithm:
 * State arrays buy[k] and sell[k].
 * If k >= n / 2, equivalent to unlimited transactions (greedy peak-valley).
 *
 * Time Complexity: O(k * N)
 * Space Complexity: O(k)
 */
public class LC0188_BestTimeToBuyAndSellStockIV {

    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if (n == 0 || k == 0) return 0;

        if (k >= n / 2) {
            int profit = 0;
            for (int i = 1; i < n; i++) {
                if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
            }
            return profit;
        }

        int[] buy = new int[k];
        int[] sell = new int[k];
        Arrays.fill(buy, Integer.MIN_VALUE);

        for (int p : prices) {
            for (int i = 0; i < k; i++) {
                buy[i] = Math.max(buy[i], (i == 0 ? 0 : sell[i - 1]) - p);
                sell[i] = Math.max(sell[i], buy[i] + p);
            }
        }
        return sell[k - 1];
    }

    public static void main(String[] args) {
        LC0188_BestTimeToBuyAndSellStockIV sol = new LC0188_BestTimeToBuyAndSellStockIV();
        System.out.println(sol.maxProfit(2, new int[]{2, 4, 1, 7})); // 9
    }
}
"""),
        ("LC0309_BestTimeCooldown.java", "LC0309 Best Time to Buy and Sell Stock with Cooldown", """/**
 * Problem: 309. Best Time to Buy and Sell Stock with Cooldown
 * Difficulty: Medium
 * Category: Array, Dynamic Programming
 *
 * Algorithm:
 * Three states: held, sold (must rest tomorrow), rest.
 * Transitions: held = max(held, rest - price), sold = held + price, rest = max(rest, sold_prev).
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0309_BestTimeCooldown {

    public int maxProfit(int[] prices) {
        if (prices == null || prices.length < 2) return 0;

        int held = -prices[0], sold = 0, rest = 0;
        for (int i = 1; i < prices.length; i++) {
            int prevHeld = held;
            int prevSold = sold;
            int prevRest = rest;

            held = Math.max(prevHeld, prevRest - prices[i]);
            sold = prevHeld + prices[i];
            rest = Math.max(prevRest, prevSold);
        }
        return Math.max(sold, rest);
    }

    public static void main(String[] args) {
        LC0309_BestTimeCooldown sol = new LC0309_BestTimeCooldown();
        System.out.println(sol.maxProfit(new int[]{1, 2, 3, 0, 2})); // 3
    }
}
"""),
        ("LC0518_CoinChangeII.java", "LC0518 Coin Change II", """/**
 * Problem: 518. Coin Change II
 * Difficulty: Medium
 * Category: Array, Dynamic Programming
 *
 * Algorithm:
 * Unbounded Knapsack / Combinations:
 * Outer loop over coins, inner loop over amounts from coin to target amount.
 *
 * Time Complexity: O(amount * coins.length)
 * Space Complexity: O(amount)
 */
public class LC0518_CoinChangeII {

    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;

        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i - coin];
            }
        }
        return dp[amount];
    }

    public static void main(String[] args) {
        LC0518_CoinChangeII sol = new LC0518_CoinChangeII();
        System.out.println(sol.change(5, new int[]{1, 2, 5})); // 4
    }
}
""")
    ],

    # -------------------------------------------------------------
    # Day 6: Trie & String Algorithms
    # -------------------------------------------------------------
    6: [
        ("LC0211_DesignAddSearchWords.java", "LC0211 Design Add and Search Words Data Structure", """/**
 * Problem: 211. Design Add and Search Words Data Structure
 * Difficulty: Medium
 * Category: String, Depth-First Search, Design, Trie
 *
 * Algorithm:
 * Trie node array of 26 letters.
 * Wildcard '.' triggers recursive DFS across all valid non-null child nodes.
 *
 * Time Complexity: Add: O(M), Search: O(26^M) worst-case wildcard, O(M) without dots
 * Space Complexity: O(Total characters in words)
 */
public class LC0211_DesignAddSearchWords {

    private TrieNode root = new TrieNode();

    static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd;
    }

    public void addWord(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (cur.children[c - 'a'] == null) cur.children[c - 'a'] = new TrieNode();
            cur = cur.children[c - 'a'];
        }
        cur.isEnd = true;
    }

    public boolean search(String word) {
        return dfs(root, word, 0);
    }

    private boolean dfs(TrieNode node, String word, int idx) {
        if (node == null) return false;
        if (idx == word.length()) return node.isEnd;

        char c = word.charAt(idx);
        if (c == '.') {
            for (TrieNode child : node.children) {
                if (dfs(child, word, idx + 1)) return true;
            }
            return false;
        }
        return dfs(node.children[c - 'a'], word, idx + 1);
    }

    public static void main(String[] args) {
        LC0211_DesignAddSearchWords sol = new LC0211_DesignAddSearchWords();
        sol.addWord("bad"); sol.addWord("dad"); sol.addWord("mad");
        System.out.println(sol.search("pad")); // false
        System.out.println(sol.search("bad")); // true
        System.out.println(sol.search(".ad")); // true
        System.out.println(sol.search("b..")); // true
    }
}
"""),
        ("LC0212_WordSearchII.java", "LC0212 Word Search II", """import java.util.*;

/**
 * Problem: 212. Word Search II
 * Difficulty: Hard
 * Category: Array, String, Backtracking, Trie, Matrix
 *
 * Algorithm:
 * Build Trie from word list. DFS board matching letters along Trie path.
 * In-place grid marking prevents duplicate visits during single search.
 *
 * Time Complexity: O(M * N * 4^(max_word_len))
 * Space Complexity: O(Trie nodes)
 */
public class LC0212_WordSearchII {

    static class Trie {
        Trie[] ch = new Trie[26];
        String word;
    }

    public List<String> findWords(char[][] board, String[] words) {
        Trie root = new Trie();
        for (String w : words) {
            Trie cur = root;
            for (char c : w.toCharArray()) {
                if (cur.ch[c - 'a'] == null) cur.ch[c - 'a'] = new Trie();
                cur = cur.ch[c - 'a'];
            }
            cur.word = w;
        }

        List<String> res = new ArrayList<>();
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                dfs(board, i, j, root, res);
            }
        }
        return res;
    }

    private void dfs(char[][] b, int r, int c, Trie node, List<String> res) {
        if (r < 0 || r >= b.length || c < 0 || c >= b[0].length || b[r][c] == '#') return;
        char orig = b[r][c];
        if (node.ch[orig - 'a'] == null) return;

        node = node.ch[orig - 'a'];
        if (node.word != null) {
            res.add(node.word);
            node.word = null;
        }

        b[r][c] = '#';
        dfs(b, r + 1, c, node, res);
        dfs(b, r - 1, c, node, res);
        dfs(b, r, c + 1, node, res);
        dfs(b, r, c - 1, node, res);
        b[r][c] = orig;
    }

    public static void main(String[] args) {
        LC0212_WordSearchII sol = new LC0212_WordSearchII();
        char[][] board = {
            {'o','a','a','n'},
            {'e','t','a','e'},
            {'i','h','k','r'},
            {'i','f','l','v'}
        };
        System.out.println(sol.findWords(board, new String[]{"oath","pea","eat","rain"})); // [oath, eat]
    }
}
"""),
        ("LC0336_PalindromePairs.java", "LC0336 Palindrome Pairs", """import java.util.*;

/**
 * Problem: 336. Palindrome Pairs
 * Difficulty: Hard
 * Category: Array, Hash Table, String, Trie
 *
 * Algorithm:
 * HashMap word-to-index lookup.
 * For each word, split into prefix and suffix; check if one is palindrome and reversed other exists.
 *
 * Time Complexity: O(N * L^2) where L is max word length
 * Space Complexity: O(N * L)
 */
public class LC0336_PalindromePairs {

    public List<List<Integer>> palindromePairs(String[] words) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < words.length; i++) map.put(words[i], i);

        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j <= words[i].length(); j++) {
                String prefix = words[i].substring(0, j);
                String suffix = words[i].substring(j);

                if (isPalin(prefix)) {
                    String revSuffix = new StringBuilder(suffix).reverse().toString();
                    Integer idx = map.get(revSuffix);
                    if (idx != null && idx != i) res.add(Arrays.asList(idx, i));
                }
                if (j > 0 && isPalin(suffix)) {
                    String revPrefix = new StringBuilder(prefix).reverse().toString();
                    Integer idx = map.get(revPrefix);
                    if (idx != null && idx != i) res.add(Arrays.asList(i, idx));
                }
            }
        }
        return res;
    }

    private boolean isPalin(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) if (s.charAt(l++) != s.charAt(r--)) return false;
        return true;
    }

    public static void main(String[] args) {
        LC0336_PalindromePairs sol = new LC0336_PalindromePairs();
        System.out.println(sol.palindromePairs(new String[]{"abcd","dcba","lls","s","sssll"}));
    }
}
"""),
        ("LC0421_MaximumXOR.java", "LC0421 Maximum XOR of Two Numbers in an Array", """/**
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
"""),
        ("LC0472_ConcatenatedWords.java", "LC0472 Concatenated Words", """import java.util.*;

/**
 * Problem: 472. Concatenated Words
 * Difficulty: Hard
 * Category: Array, String, Dynamic Programming, Depth-First Search, Trie
 *
 * Algorithm:
 * HashSet word dictionary. For each word, test if formable from >= 2 shorter words via 1D DP.
 *
 * Time Complexity: O(N * L^2)
 * Space Complexity: O(N * L)
 */
public class LC0472_ConcatenatedWords {

    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Set<String> set = new HashSet<>(Arrays.asList(words));
        List<String> res = new ArrayList<>();

        for (String w : words) {
            int len = w.length();
            if (len == 0) continue;
            boolean[] dp = new boolean[len + 1];
            dp[0] = true;

            for (int i = 1; i <= len; i++) {
                for (int j = 0; j < i; j++) {
                    if (dp[j] && set.contains(w.substring(j, i)) && !(j == 0 && i == len)) {
                        dp[i] = true;
                        break;
                    }
                }
            }
            if (dp[len]) res.add(w);
        }
        return res;
    }

    public static void main(String[] args) {
        LC0472_ConcatenatedWords sol = new LC0472_ConcatenatedWords();
        String[] words = {"cat","cats","catsdogcats","dog","dogcatsdog","hippodogcats","rat"};
        System.out.println(sol.findAllConcatenatedWordsInADict(words));
    }
}
"""),
        ("LC0648_ReplaceWords.java", "LC0648 Replace Words", """import java.util.*;

/**
 * Problem: 648. Replace Words
 * Difficulty: Medium
 * Category: Array, Hash Table, String, Trie
 *
 * Algorithm:
 * Insert dictionary roots into Trie. For each sentence word, find shortest matching root.
 *
 * Time Complexity: O(Dict chars + Sentence chars)
 * Space Complexity: O(Dict chars)
 */
public class LC0648_ReplaceWords {

    static class Trie {
        Trie[] ch = new Trie[26];
        String rootWord;
    }

    public String replaceWords(List<String> dictionary, String sentence) {
        Trie root = new Trie();
        for (String word : dictionary) {
            Trie cur = root;
            for (char c : word.toCharArray()) {
                if (cur.ch[c - 'a'] == null) cur.ch[c - 'a'] = new Trie();
                cur = cur.ch[c - 'a'];
            }
            cur.rootWord = word;
        }

        StringBuilder sb = new StringBuilder();
        for (String word : sentence.split(" ")) {
            Trie cur = root;
            String replacement = null;
            for (char c : word.toCharArray()) {
                if (cur.ch[c - 'a'] == null || cur.rootWord != null) {
                    replacement = cur.rootWord;
                    break;
                }
                cur = cur.ch[c - 'a'];
            }
            if (replacement == null) replacement = word;
            if (sb.length() > 0) sb.append(' ');
            sb.append(replacement);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        LC0648_ReplaceWords sol = new LC0648_ReplaceWords();
        System.out.println(sol.replaceWords(Arrays.asList("cat","bat","rat"), "the cattle was rattled by the battery"));
    }
}
""")
    ],

    # -------------------------------------------------------------
    # Day 7: Advanced Trees & LCA
    # -------------------------------------------------------------
    7: [
        ("LC0297_SerializeDeserializeBinaryTree.java", "LC0297 Serialize and Deserialize Binary Tree", """import java.util.*;

/**
 * Problem: 297. Serialize and Deserialize Binary Tree
 * Difficulty: Hard
 * Category: String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree
 *
 * Algorithm:
 * Preorder DFS traversal with "#" representing null pointers.
 * Deserialization uses recursive index pointer / token queue.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0297_SerializeDeserializeBinaryTree {

    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    public String serialize(TreeNode root) {
        if (root == null) return "#";
        return root.val + "," + serialize(root.left) + "," + serialize(root.right);
    }

    private int idx;

    public TreeNode deserialize(String data) {
        idx = 0;
        String[] tokens = data.split(",");
        return build(tokens);
    }

    private TreeNode build(String[] tokens) {
        if (idx >= tokens.length || tokens[idx].equals("#")) {
            idx++;
            return null;
        }
        TreeNode node = new TreeNode(Integer.parseInt(tokens[idx++]));
        node.left = build(tokens);
        node.right = build(tokens);
        return node;
    }

    public static void main(String[] args) {
        LC0297_SerializeDeserializeBinaryTree sol = new LC0297_SerializeDeserializeBinaryTree();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        String s = sol.serialize(root);
        System.out.println("Serialized: " + s); // 1,2,#,#,3,#,#
        TreeNode res = sol.deserialize(s);
        System.out.println("Re-serialized: " + sol.serialize(res));
    }
}
"""),
        ("LC0450_DeleteNodeInBST.java", "LC0450 Delete Node in a BST", """/**
 * Problem: 450. Delete Node in a BST
 * Difficulty: Medium
 * Category: Tree, Binary Search Tree, Binary Tree
 *
 * Algorithm:
 * Locate target node via BST property.
 * If 0 or 1 child, return existing child. If 2 children, swap with inorder successor and delete successor.
 *
 * Time Complexity: O(H) where H is tree height
 * Space Complexity: O(H) recursion stack
 */
public class LC0450_DeleteNodeInBST {

    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;

        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else {
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;

            TreeNode successor = root.right;
            while (successor.left != null) successor = successor.left;
            root.val = successor.val;
            root.right = deleteNode(root.right, successor.val);
        }
        return root;
    }

    public static void main(String[] args) {
        LC0450_DeleteNodeInBST sol = new LC0450_DeleteNodeInBST();
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(3);
        root.right = new TreeNode(6);
        TreeNode res = sol.deleteNode(root, 3);
        System.out.println("New left child: " + (res.left != null ? res.left.val : "null"));
    }
}
"""),
        ("LC0538_ConvertBSTToGreaterTree.java", "LC0538 Convert BST to Greater Tree", """/**
 * Problem: 538. Convert BST to Greater Tree
 * Difficulty: Medium
 * Category: Tree, Depth-First Search, Binary Search Tree, Binary Tree
 *
 * Algorithm:
 * Reverse in-order traversal: Right -> Root -> Left.
 * Accumulate running sum and assign to current node.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(H)
 */
public class LC0538_ConvertBSTToGreaterTree {

    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    private int sum = 0;

    public TreeNode convertBST(TreeNode root) {
        if (root != null) {
            convertBST(root.right);
            sum += root.val;
            root.val = sum;
            convertBST(root.left);
        }
        return root;
    }

    public static void main(String[] args) {
        LC0538_ConvertBSTToGreaterTree sol = new LC0538_ConvertBSTToGreaterTree();
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(1);
        root.right = new TreeNode(6);
        TreeNode res = sol.convertBST(root);
        System.out.println("Root new val: " + res.val); // 10
    }
}
"""),
        ("LC0543_DiameterOfBinaryTree.java", "LC0543 Diameter of Binary Tree", """/**
 * Problem: 543. Diameter of Binary Tree
 * Difficulty: Easy
 * Category: Tree, Depth-First Search, Binary Tree
 *
 * Algorithm:
 * Post-order DFS computing max depth of left and right subtrees.
 * Diameter at each node is left_depth + right_depth.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(H)
 */
public class LC0543_DiameterOfBinaryTree {

    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    private int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        maxDiameter = 0;
        depth(root);
        return maxDiameter;
    }

    private int depth(TreeNode node) {
        if (node == null) return 0;
        int l = depth(node.left);
        int r = depth(node.right);
        maxDiameter = Math.max(maxDiameter, l + r);
        return 1 + Math.max(l, r);
    }

    public static void main(String[] args) {
        LC0543_DiameterOfBinaryTree sol = new LC0543_DiameterOfBinaryTree();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        System.out.println("Diameter: " + sol.diameterOfBinaryTree(root)); // 2
    }
}
"""),
        ("LC0572_SubtreeOfAnotherTree.java", "LC0572 Subtree of Another Tree", """/**
 * Problem: 572. Subtree of Another Tree
 * Difficulty: Easy
 * Category: Tree, Depth-First Search, String Matching, Binary Tree, Hash Function
 *
 * Algorithm:
 * Check if current tree is identical to subRoot via isSame(root, subRoot).
 * If not, recurse on left and right children.
 *
 * Time Complexity: O(M * N)
 * Space Complexity: O(H)
 */
public class LC0572_SubtreeOfAnotherTree {

    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) return false;
        if (isSame(root, subRoot)) return true;
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    private boolean isSame(TreeNode a, TreeNode b) {
        if (a == null && b == null) return true;
        if (a == null || b == null) return false;
        return a.val == b.val && isSame(a.left, b.left) && isSame(a.right, b.right);
    }

    public static void main(String[] args) {
        LC0572_SubtreeOfAnotherTree sol = new LC0572_SubtreeOfAnotherTree();
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(4);
        root.right = new TreeNode(5);
        TreeNode sub = new TreeNode(4);
        System.out.println("Is subtree: " + sol.isSubtree(root, sub)); // true
    }
}
"""),
        ("LC0652_FindDuplicateSubtrees.java", "LC0652 Find Duplicate Subtrees", """import java.util.*;

/**
 * Problem: 652. Find Duplicate Subtrees
 * Difficulty: Medium
 * Category: Hash Table, Tree, Depth-First Search, Binary Tree
 *
 * Algorithm:
 * Post-order serialization string for each subtree.
 * HashMap tracks frequency of serialized representations; collect duplicate root nodes.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0652_FindDuplicateSubtrees {

    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    private Map<String, Integer> count = new HashMap<>();
    private List<TreeNode> res = new ArrayList<>();

    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        count.clear();
        res.clear();
        serialize(root);
        return res;
    }

    private String serialize(TreeNode node) {
        if (node == null) return "#";
        String key = node.val + "," + serialize(node.left) + "," + serialize(node.right);
        count.merge(key, 1, Integer::sum);
        if (count.get(key) == 2) {
            res.add(node);
        }
        return key;
    }

    public static void main(String[] args) {
        LC0652_FindDuplicateSubtrees sol = new LC0652_FindDuplicateSubtrees();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.right.left = new TreeNode(2);
        root.right.left.left = new TreeNode(4);
        List<TreeNode> dups = sol.findDuplicateSubtrees(root);
        System.out.println("Duplicate subtrees count: " + dups.size()); // 2
    }
}
""")
    ]
}

def generate_all_solutions():
    print("[*] Generating 42 Java solutions into staging/day1 through staging/day7...")
    import shutil
    for day, probrecs in PROBLEMS.items():
        day_dir = os.path.join(ROOT, "staging", f"day{day}")
        if os.path.isdir(day_dir):
            shutil.rmtree(day_dir)
        os.makedirs(day_dir, exist_ok=True)
        for filename, _, code in probrecs:
            filepath = os.path.join(day_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(code.strip() + "\n")
            print(f"  -> Generated {os.path.relpath(filepath, ROOT)}")
    print("[+] All 42 solutions generated successfully.")

def generate_day_scripts():
    print("[*] Generating daily shell scripts day1.sh through day7.sh...")
    for day, probrecs in PROBLEMS.items():
        sh_path = os.path.join(ROOT, f"day{day}.sh")
        lines = [
            "#!/bin/bash",
            "# =================================================================",
            f"# Day {day} LeetCode Submissions (6 Sequential Java Contributions)",
            "# Compatible with Termux (Android) and standard Linux/macOS bash",
            "# =================================================================",
            "set -e",
            "",
            'SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"',
            'cd "$SCRIPT_DIR"',
            "",
            'echo "================================================================"',
            f'echo "🚀 Executing Day {day} Submissions (6 Problems in Java)"',
            'echo "================================================================"',
            "",
            "if ! command -v git &> /dev/null; then",
            '    echo "[-] Git is not installed. In Termux, run: pkg install git"',
            "    exit 1",
            "fi",
            "",
            'echo "[*] Syncing with remote repository..."',
            "git pull --rebase origin main || true",
            ""
        ]

        for i, (filename, title, _) in enumerate(probrecs, 1):
            lines.extend([
                f"# [{i}/6] {filename}",
                f'echo "[*] Processing [{i}/6]: {title}..."',
                f'if [ -f "./{filename}" ] && git ls-files --error-unmatch "./{filename}" >/dev/null 2>&1 && git diff --quiet HEAD -- "./{filename}"; then',
                f'    echo "    [✓] {filename} is already committed in git repository."',
                f'else',
                f'    cp "staging/day{day}/{filename}" "./{filename}"',
                f'    git add "{filename}"',
                f'    git commit -m "feat(leetcode): solve {title} in Java"',
                f'    echo "    [+] Committed [{i}/6]: {title}"',
                f'    command -v sleep >/dev/null 2>&1 && sleep 2 || true',
                f'fi',
                ""
            ])

        lines.extend([
            'echo "================================================================"',
            f'echo "[*] Day {day} commits recorded! Pushing to GitHub..."',
            'echo "================================================================"',
            "git push origin main || git push",
            "",
            'echo ""',
            f'echo "🎉 [SUCCESS] Day {day} complete! 6 contributions pushed to GitHub."',
            'echo "================================================================"',
            ""
        ]        )

        with open(sh_path, "wb") as f:
            f.write("\n".join(lines).encode("utf-8"))
        print(f"  -> Generated {os.path.basename(sh_path)}")

def generate_auto_detector_scripts():
    print("[*] Generating auto-detector and smart master runner scripts...")
    
    auto_sh_path = os.path.join(ROOT, "auto_submit.sh")
    auto_sh_content = """#!/bin/bash
# =================================================================
# 🧠 Intelligent Auto-Detector & Daily Submissions Runner
# Automatically detects what has already been solved/pushed to GitHub
# and seamlessly runs the next pending batch without manual checking.
# Compatible with Termux (Android) and standard Linux/macOS bash.
# =================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================"
echo "⚡ LeetCode Auto-Detector & Submission Engine"
echo "================================================================"

# Verify git
if ! command -v git &> /dev/null; then
    echo "[-] Git is not installed. In Termux, run: pkg install git"
    exit 1
fi

# Sync remote first
echo "[*] Fetching latest status from GitHub..."
git pull --rebase origin main 2>/dev/null || true

# Count total problems in root
TOTAL_ROOT=$(find . -maxdepth 1 -name "LC*.java" | wc -l | tr -d ' ')
echo "[*] Total Java solutions currently active in root: $TOTAL_ROOT"
echo "----------------------------------------------------------------"

# Scan staging/day1 through staging/day7
NEXT_DAY=""
ALL_DONE=true

for day in 1 2 3 4 5 6 7; do
    DAY_DIR="staging/day$day"
    if [ ! -d "$DAY_DIR" ]; then
        continue
    fi

    TOTAL_DAY=0
    DONE_DAY=0

    for f in "$DAY_DIR"/LC*.java; do
        [ -e "$f" ] || continue
        TOTAL_DAY=$((TOTAL_DAY + 1))
        BNAME=$(basename "$f")
        if [ -f "./$BNAME" ]; then
            DONE_DAY=$((DONE_DAY + 1))
        fi
    done

    if [ "$DONE_DAY" -eq "$TOTAL_DAY" ] && [ "$TOTAL_DAY" -gt 0 ]; then
        echo "  [✓] Day $day: Completed ($DONE_DAY/$TOTAL_DAY uploaded)"
    elif [ "$DONE_DAY" -gt 0 ] && [ "$DONE_DAY" -lt "$TOTAL_DAY" ]; then
        echo "  [⚡] Day $day: Partially complete ($DONE_DAY/$TOTAL_DAY uploaded, $((TOTAL_DAY - DONE_DAY)) pending)"
        if [ -z "$NEXT_DAY" ]; then
            NEXT_DAY="$day"
            ALL_DONE=false
        fi
    else
        echo "  [ ] Day $day: Queued (0/$TOTAL_DAY uploaded)"
        if [ -z "$NEXT_DAY" ]; then
            NEXT_DAY="$day"
            ALL_DONE=false
        fi
    fi
done

echo "----------------------------------------------------------------"

if [ "$1" == "status" ] || [ "$1" == "--status" ] || [ "$1" == "-s" ]; then
    echo "[*] Status check complete."
    if [ "$ALL_DONE" = true ]; then
        echo "🎉 All 42 problems across Days 1-7 are fully submitted!"
    else
        echo "⚡ Next batch queued: DAY $NEXT_DAY. Run './auto_submit.sh' to execute."
    fi
    exit 0
fi

if [ -n "$1" ] && [ "$1" != "auto" ] && [ "$1" != "--auto" ]; then
    TARGET_DAY="$1"
    echo "[!] User requested override: Day $TARGET_DAY"
else
    if [ "$ALL_DONE" = true ]; then
        echo "🎉 All 42 problems across Days 1-7 have already been submitted!"
        echo "[*] Nothing pending to upload. You're fully up-to-date!"
        exit 0
    fi
    TARGET_DAY="$NEXT_DAY"
    echo "⚡ Auto-detected next pending batch: DAY $TARGET_DAY"
fi

if [ ! -f "day${TARGET_DAY}.sh" ]; then
    echo "[-] Error: day${TARGET_DAY}.sh not found!"
    exit 1
fi

echo "[*] Launching execution for Day $TARGET_DAY..."
if command -v chmod &> /dev/null; then
    chmod +x "day${TARGET_DAY}.sh" || true
fi

sh "day${TARGET_DAY}.sh"
"""
    with open(auto_sh_path, "wb") as f:
        f.write(auto_sh_content.encode("utf-8"))
    print(f"  -> Generated {os.path.basename(auto_sh_path)}")

    run_sh_path = os.path.join(ROOT, "run_day.sh")
    run_sh_content = """#!/bin/bash
# Master Daily Runner with Auto-Detector for Termux (Android) / Linux
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if command -v chmod &> /dev/null; then
    chmod +x auto_submit.sh || true
fi

if [ "$1" == "status" ] || [ "$1" == "--status" ]; then
    sh auto_submit.sh --status
elif [ -n "$1" ]; then
    sh auto_submit.sh "$1"
else
    sh auto_submit.sh auto
fi
"""
    with open(run_sh_path, "wb") as f:
        f.write(run_sh_content.encode("utf-8"))
    print(f"  -> Updated {os.path.basename(run_sh_path)}")

    py_det_path = os.path.join(ROOT, "scripts", "detector.py")
    py_det_content = '''"""
detector.py
Analyzes the LeetCode repository to detect which problems have been submitted,
which staging problems are pending, and optionally runs the next daily batch.
"""

import os
import sys
import subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_root_solutions():
    files = [f for f in os.listdir(ROOT) if f.startswith("LC") and f.endswith(".java")]
    return sorted(files)

def analyze_staging():
    days = {}
    for day in range(1, 8):
        day_dir = os.path.join(ROOT, "staging", f"day{day}")
        if not os.path.isdir(day_dir):
            continue
        day_files = sorted([f for f in os.listdir(day_dir) if f.startswith("LC") and f.endswith(".java")])
        days[day] = day_files
    return days

def report_status():
    root_sols = set(get_root_solutions())
    staging_days = analyze_staging()

    print("=" * 64)
    print("🔍 LEETCODE REPOSITORY UPLOAD DETECTOR")
    print("=" * 64)
    print(f"Total problems active in repository root: {len(root_sols)}")
    print("-" * 64)

    next_day = None
    all_completed = True

    for day, files in staging_days.items():
        completed = [f for f in files if f in root_sols]
        pending = [f for f in files if f not in root_sols]

        if len(pending) == 0:
            status_str = "✅ COMPLETED"
        elif len(completed) > 0:
            status_str = f"⚡ PARTIAL ({len(completed)}/{len(files)} uploaded)"
            if next_day is None:
                next_day = day
                all_completed = False
        else:
            status_str = f"⏳ QUEUED (0/{len(files)} uploaded)"
            if next_day is None:
                next_day = day
                all_completed = False

        print(f"Day {day} [{status_str}]:")
        for f in files:
            mark = "  [✓]" if f in root_sols else "  [ ]"
            print(f"  {mark} {f}")
        print()

    print("-" * 64)
    if all_completed:
        print("🎉 ALL 42 STAGING PROBLEMS ACROSS ALL 7 DAYS ARE FULLY SUBMITTED!")
    else:
        print(f"⚡ NEXT BATCH RECOMMENDED: DAY {next_day}")
    print("=" * 64)
    return next_day

def run_day(day_num):
    day_script = os.path.join(ROOT, f"day{day_num}.sh")
    cmd = ["sh", day_script]
    print(f"[*] Executing Day {day_num} via sh...")
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("--run-next", "-r", "auto"):
        next_d = report_status()
        if next_d:
            print(f"\\n[*] Launching Day {next_d} automatically...")
            run_day(next_d)
    else:
        report_status()
'''
    with open(py_det_path, "wb") as f:
        f.write(py_det_content.encode("utf-8"))
    print(f"  -> Generated {os.path.basename(py_det_path)}")

if __name__ == "__main__":
    generate_all_solutions()
    generate_day_scripts()
    generate_auto_detector_scripts()
    print("\n[+] Week 3 build suite completed successfully.")
