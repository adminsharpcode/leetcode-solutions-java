#!/usr/bin/env python3
"""
build_week3_suite.py — Week 3 generator (Days 1-7, 6 problems each = 42 problems)
All problems are NEW — none overlap with the 137 already committed.
"""

import os, stat, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
STAGING = os.path.join(ROOT, "staging")

# ---------------------------------------------------------------------------
# 42 NEW problems — none in the existing 137-problem catalog
# ---------------------------------------------------------------------------
DAYS = {
    "day1": [
        ("LC0127_WordLadder.java", "LC0127 Word Ladder",
         """import java.util.*;
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
                        if (wordSet.remove(next)) queue.offer(next);
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
        List<String> wl = Arrays.asList("hot","dot","dog","lot","log","cog");
        System.out.println(sol.ladderLength("hit", "cog", wl)); // 5
    }
}
"""),
        ("LC0130_SurroundedRegions.java", "LC0130 Surrounded Regions",
         """public class LC0130_SurroundedRegions {
    public void solve(char[][] board) {
        if (board == null || board.length == 0) return;
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++) { dfs(board, i, 0, m, n); dfs(board, i, n-1, m, n); }
        for (int j = 0; j < n; j++) { dfs(board, 0, j, m, n); dfs(board, m-1, j, m, n); }
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                board[i][j] = board[i][j] == 'S' ? 'O' : 'X';
    }
    private void dfs(char[][] b, int i, int j, int m, int n) {
        if (i < 0 || i >= m || j < 0 || j >= n || b[i][j] != 'O') return;
        b[i][j] = 'S';
        dfs(b, i+1, j, m, n); dfs(b, i-1, j, m, n);
        dfs(b, i, j+1, m, n); dfs(b, i, j-1, m, n);
    }
    public static void main(String[] args) {
        LC0130_SurroundedRegions sol = new LC0130_SurroundedRegions();
        char[][] board = {{'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},{'X','O','X','X'}};
        sol.solve(board);
        for (char[] row : board) System.out.println(new String(row));
    }
}
"""),
        ("LC0261_GraphValidTree.java", "LC0261 Graph Valid Tree",
         """public class LC0261_GraphValidTree {
    int[] parent;
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false;
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int[] e : edges) {
            int a = find(e[0]), b = find(e[1]);
            if (a == b) return false;
            parent[a] = b;
        }
        return true;
    }
    int find(int x) { return parent[x] == x ? x : (parent[x] = find(parent[x])); }
    public static void main(String[] args) {
        LC0261_GraphValidTree sol = new LC0261_GraphValidTree();
        System.out.println(sol.validTree(5, new int[][]{{0,1},{0,2},{0,3},{1,4}})); // true
    }
}
"""),
        ("LC0310_MinimumHeightTrees.java", "LC0310 Minimum Height Trees",
         """import java.util.*;
public class LC0310_MinimumHeightTrees {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) return Collections.singletonList(0);
        List<Set<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new HashSet<>());
        for (int[] e : edges) { adj.get(e[0]).add(e[1]); adj.get(e[1]).add(e[0]); }
        List<Integer> leaves = new ArrayList<>();
        for (int i = 0; i < n; i++) if (adj.get(i).size() == 1) leaves.add(i);
        int remaining = n;
        while (remaining > 2) {
            remaining -= leaves.size();
            List<Integer> next = new ArrayList<>();
            for (int leaf : leaves) {
                int nb = adj.get(leaf).iterator().next();
                adj.get(nb).remove(leaf);
                if (adj.get(nb).size() == 1) next.add(nb);
            }
            leaves = next;
        }
        return leaves;
    }
    public static void main(String[] args) {
        LC0310_MinimumHeightTrees sol = new LC0310_MinimumHeightTrees();
        System.out.println(sol.findMinHeightTrees(4, new int[][]{{1,0},{1,2},{1,3}})); // [1]
    }
}
"""),
        ("LC0399_EvaluateDivision.java", "LC0399 Evaluate Division",
         """import java.util.*;
public class LC0399_EvaluateDivision {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> graph = new HashMap<>();
        for (int i = 0; i < equations.size(); i++) {
            String a = equations.get(i).get(0), b = equations.get(i).get(1);
            graph.computeIfAbsent(a, k -> new HashMap<>()).put(b, values[i]);
            graph.computeIfAbsent(b, k -> new HashMap<>()).put(a, 1.0 / values[i]);
        }
        double[] res = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            String src = queries.get(i).get(0), dst = queries.get(i).get(1);
            res[i] = dfs(graph, src, dst, new HashSet<>());
        }
        return res;
    }
    private double dfs(Map<String, Map<String, Double>> g, String src, String dst, Set<String> visited) {
        if (!g.containsKey(src) || !g.containsKey(dst)) return -1.0;
        if (src.equals(dst)) return 1.0;
        visited.add(src);
        for (Map.Entry<String, Double> e : g.get(src).entrySet()) {
            if (!visited.contains(e.getKey())) {
                double res = dfs(g, e.getKey(), dst, visited);
                if (res != -1.0) return res * e.getValue();
            }
        }
        return -1.0;
    }
    public static void main(String[] args) {
        LC0399_EvaluateDivision sol = new LC0399_EvaluateDivision();
        List<List<String>> eq = Arrays.asList(Arrays.asList("a","b"), Arrays.asList("b","c"));
        double[] vals = {2.0, 3.0};
        List<List<String>> q = Arrays.asList(Arrays.asList("a","c"), Arrays.asList("b","a"));
        System.out.println(Arrays.toString(sol.calcEquation(eq, vals, q))); // [6.0, 0.5]
    }
}
"""),
        ("LC0547_NumberOfProvinces.java", "LC0547 Number of Provinces",
         """public class LC0547_NumberOfProvinces {
    int[] parent;
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int i = 0; i < n; i++)
            for (int j = i+1; j < n; j++)
                if (isConnected[i][j] == 1) union(i, j);
        int count = 0;
        for (int i = 0; i < n; i++) if (find(i) == i) count++;
        return count;
    }
    int find(int x) { return parent[x] == x ? x : (parent[x] = find(parent[x])); }
    void union(int a, int b) { parent[find(a)] = find(b); }
    public static void main(String[] args) {
        LC0547_NumberOfProvinces sol = new LC0547_NumberOfProvinces();
        System.out.println(sol.findCircleNum(new int[][]{{1,1,0},{1,1,0},{0,0,1}})); // 2
    }
}
"""),
    ],
    "day2": [
        ("LC0085_MaximalRectangle.java", "LC0085 Maximal Rectangle",
         """import java.util.*;
public class LC0085_MaximalRectangle {
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0) return 0;
        int n = matrix[0].length, max = 0;
        int[] heights = new int[n];
        for (char[] row : matrix) {
            for (int j = 0; j < n; j++)
                heights[j] = row[j] == '1' ? heights[j] + 1 : 0;
            max = Math.max(max, largestRect(heights));
        }
        return max;
    }
    private int largestRect(int[] h) {
        Deque<Integer> stack = new ArrayDeque<>();
        int max = 0;
        for (int i = 0; i <= h.length; i++) {
            int cur = (i == h.length) ? 0 : h[i];
            while (!stack.isEmpty() && h[stack.peek()] > cur) {
                int height = h[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                max = Math.max(max, height * width);
            }
            stack.push(i);
        }
        return max;
    }
    public static void main(String[] args) {
        LC0085_MaximalRectangle sol = new LC0085_MaximalRectangle();
        char[][] m = {{'1','0','1','0','0'},{'1','0','1','1','1'},{'1','1','1','1','1'},{'1','0','0','1','0'}};
        System.out.println(sol.maximalRectangle(m)); // 6
    }
}
"""),
        ("LC0316_RemoveDuplicateLetters.java", "LC0316 Remove Duplicate Letters",
         """import java.util.*;
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
        ("LC0394_DecodeString.java", "LC0394 Decode String",
         """import java.util.*;
public class LC0394_DecodeString {
    public String decodeString(String s) {
        Deque<Integer> countStack = new ArrayDeque<>();
        Deque<StringBuilder> strStack = new ArrayDeque<>();
        StringBuilder current = new StringBuilder();
        int k = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) { k = k * 10 + (c - '0'); }
            else if (c == '[') { countStack.push(k); k = 0; strStack.push(current); current = new StringBuilder(); }
            else if (c == ']') { StringBuilder tmp = current; current = strStack.pop(); int times = countStack.pop(); while (times-- > 0) current.append(tmp); }
            else current.append(c);
        }
        return current.toString();
    }
    public static void main(String[] args) {
        LC0394_DecodeString sol = new LC0394_DecodeString();
        System.out.println(sol.decodeString("3[a]2[bc]")); // aaabcbc
        System.out.println(sol.decodeString("3[a2[c]]")); // accaccacc
    }
}
"""),
        ("LC0496_NextGreaterElementI.java", "LC0496 Next Greater Element I",
         """import java.util.*;
public class LC0496_NextGreaterElementI {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap<>();
        Deque<Integer> stack = new ArrayDeque<>();
        for (int n : nums2) {
            while (!stack.isEmpty() && stack.peek() < n) map.put(stack.pop(), n);
            stack.push(n);
        }
        int[] res = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) res[i] = map.getOrDefault(nums1[i], -1);
        return res;
    }
    public static void main(String[] args) {
        LC0496_NextGreaterElementI sol = new LC0496_NextGreaterElementI();
        System.out.println(Arrays.toString(sol.nextGreaterElement(new int[]{4,1,2}, new int[]{1,3,4,2}))); // [-1,3,-1]
    }
}
"""),
        ("LC0503_NextGreaterElementII.java", "LC0503 Next Greater Element II",
         """import java.util.*;
public class LC0503_NextGreaterElementII {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        Arrays.fill(res, -1);
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < 2 * n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i % n])
                res[stack.pop()] = nums[i % n];
            if (i < n) stack.push(i);
        }
        return res;
    }
    public static void main(String[] args) {
        LC0503_NextGreaterElementII sol = new LC0503_NextGreaterElementII();
        System.out.println(Arrays.toString(sol.nextGreaterElements(new int[]{1,2,1}))); // [2,-1,2]
    }
}
"""),
        ("LC0739_DailyTemperatures.java", "LC0739 Daily Temperatures",
         """import java.util.*;
public class LC0739_DailyTemperatures {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] res = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
                int idx = stack.pop();
                res[idx] = i - idx;
            }
            stack.push(i);
        }
        return res;
    }
    public static void main(String[] args) {
        LC0739_DailyTemperatures sol = new LC0739_DailyTemperatures();
        System.out.println(Arrays.toString(sol.dailyTemperatures(new int[]{73,74,75,71,69,72,76,73}))); // [1,1,4,2,1,1,0,0]
    }
}
"""),
    ],
    "day3": [
        ("LC0030_SubstringConcatenation.java", "LC0030 Substring with Concatenation of All Words",
         """import java.util.*;
public class LC0030_SubstringConcatenation {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<>();
        if (s == null || words == null || words.length == 0) return res;
        int wordLen = words[0].length(), wordCount = words.length;
        int totalLen = wordLen * wordCount;
        Map<String, Integer> freq = new HashMap<>();
        for (String w : words) freq.merge(w, 1, Integer::sum);
        for (int i = 0; i <= s.length() - totalLen; i++) {
            Map<String, Integer> seen = new HashMap<>();
            int j = 0;
            while (j < wordCount) {
                String word = s.substring(i + j * wordLen, i + (j + 1) * wordLen);
                if (!freq.containsKey(word)) break;
                seen.merge(word, 1, Integer::sum);
                if (seen.get(word) > freq.get(word)) break;
                j++;
            }
            if (j == wordCount) res.add(i);
        }
        return res;
    }
    public static void main(String[] args) {
        LC0030_SubstringConcatenation sol = new LC0030_SubstringConcatenation();
        System.out.println(sol.findSubstring("barfoothefoobarman", new String[]{"foo","bar"})); // [0, 9]
    }
}
"""),
        ("LC0239_SlidingWindowMaximum.java", "LC0239 Sliding Window Maximum",
         """import java.util.*;
public class LC0239_SlidingWindowMaximum {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] res = new int[n - k + 1];
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!dq.isEmpty() && dq.peek() < i - k + 1) dq.poll();
            while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i]) dq.pollLast();
            dq.offer(i);
            if (i >= k - 1) res[i - k + 1] = nums[dq.peek()];
        }
        return res;
    }
    public static void main(String[] args) {
        LC0239_SlidingWindowMaximum sol = new LC0239_SlidingWindowMaximum();
        System.out.println(Arrays.toString(sol.maxSlidingWindow(new int[]{1,3,-1,-3,5,3,6,7}, 3))); // [3,3,5,5,6,7]
    }
}
"""),
        ("LC0567_PermutationInString.java", "LC0567 Permutation in String",
         """public class LC0567_PermutationInString {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;
        int[] freq = new int[26];
        for (char c : s1.toCharArray()) freq[c - 'a']++;
        int l = 0, matches = 0;
        int[] window = new int[26];
        for (int r = 0; r < s2.length(); r++) {
            window[s2.charAt(r) - 'a']++;
            if (window[s2.charAt(r) - 'a'] == freq[s2.charAt(r) - 'a']) matches++;
            if (r >= s1.length()) {
                if (window[s2.charAt(l) - 'a'] == freq[s2.charAt(l) - 'a']) matches--;
                window[s2.charAt(l++) - 'a']--;
            }
            if (matches == 26) return true;
        }
        return false;
    }
    public static void main(String[] args) {
        LC0567_PermutationInString sol = new LC0567_PermutationInString();
        System.out.println(sol.checkInclusion("ab", "eidbaooo")); // true
        System.out.println(sol.checkInclusion("ab", "eidboaoo")); // false
    }
}
"""),
        ("LC0632_SmallestRange.java", "LC0632 Smallest Range Covering Elements from K Lists",
         """import java.util.*;
public class LC0632_SmallestRange {
    public int[] smallestRange(List<List<Integer>> nums) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < nums.size(); i++) {
            pq.offer(new int[]{nums.get(i).get(0), i, 0});
            max = Math.max(max, nums.get(i).get(0));
        }
        int[] res = {pq.peek()[0], max};
        while (true) {
            int[] cur = pq.poll();
            int val = cur[0], row = cur[1], col = cur[2];
            if (col + 1 >= nums.get(row).size()) break;
            int next = nums.get(row).get(col + 1);
            pq.offer(new int[]{next, row, col + 1});
            max = Math.max(max, next);
            if (max - pq.peek()[0] < res[1] - res[0]) res = new int[]{pq.peek()[0], max};
        }
        return res;
    }
    public static void main(String[] args) {
        LC0632_SmallestRange sol = new LC0632_SmallestRange();
        List<List<Integer>> nums = Arrays.asList(Arrays.asList(4,10,15,24,26),Arrays.asList(0,9,12,20),Arrays.asList(5,18,22,30));
        System.out.println(Arrays.toString(sol.smallestRange(nums))); // [20, 24]
    }
}
"""),
        ("LC0643_MaximumAverageSubarrayI.java", "LC0643 Maximum Average Subarray I",
         """public class LC0643_MaximumAverageSubarrayI {
    public double findMaxAverage(int[] nums, int k) {
        double sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];
        double max = sum;
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            max = Math.max(max, sum);
        }
        return max / k;
    }
    public static void main(String[] args) {
        LC0643_MaximumAverageSubarrayI sol = new LC0643_MaximumAverageSubarrayI();
        System.out.println(sol.findMaxAverage(new int[]{1,12,-5,-6,50,3}, 4)); // 12.75
    }
}
"""),
        ("LC0159_LongestSubstringTwoDistinct.java", "LC0159 Longest Substring with At Most Two Distinct Characters",
         """import java.util.*;
public class LC0159_LongestSubstringTwoDistinct {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int l = 0, max = 0;
        for (int r = 0; r < s.length(); r++) {
            map.merge(s.charAt(r), 1, Integer::sum);
            while (map.size() > 2) {
                char lc = s.charAt(l++);
                map.put(lc, map.get(lc) - 1);
                if (map.get(lc) == 0) map.remove(lc);
            }
            max = Math.max(max, r - l + 1);
        }
        return max;
    }
    public static void main(String[] args) {
        LC0159_LongestSubstringTwoDistinct sol = new LC0159_LongestSubstringTwoDistinct();
        System.out.println(sol.lengthOfLongestSubstringTwoDistinct("eceba")); // 3
        System.out.println(sol.lengthOfLongestSubstringTwoDistinct("ccaabbb")); // 5
    }
}
"""),
    ],
    "day4": [
        ("LC0190_ReverseBits.java", "LC0190 Reverse Bits",
         """public class LC0190_ReverseBits {
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
        System.out.println(Integer.toBinaryString(sol.reverseBits(43261596))); // 964176192
    }
}
"""),
        ("LC0191_NumberOf1Bits.java", "LC0191 Number of 1 Bits",
         """public class LC0191_NumberOf1Bits {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) { count += n & 1; n >>>= 1; }
        return count;
    }
    public static void main(String[] args) {
        LC0191_NumberOf1Bits sol = new LC0191_NumberOf1Bits();
        System.out.println(sol.hammingWeight(11)); // 3
        System.out.println(sol.hammingWeight(128)); // 1
    }
}
"""),
        ("LC0231_PowerOfTwo.java", "LC0231 Power of Two",
         """public class LC0231_PowerOfTwo {
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
        ("LC0260_SingleNumberIII.java", "LC0260 Single Number III",
         """import java.util.*;
public class LC0260_SingleNumberIII {
    public int[] singleNumber(int[] nums) {
        int xor = 0;
        for (int n : nums) xor ^= n;
        int diff = xor & (-xor);
        int a = 0;
        for (int n : nums) if ((n & diff) != 0) a ^= n;
        return new int[]{a, xor ^ a};
    }
    public static void main(String[] args) {
        LC0260_SingleNumberIII sol = new LC0260_SingleNumberIII();
        System.out.println(Arrays.toString(sol.singleNumber(new int[]{1,2,1,3,2,5}))); // [3,5]
    }
}
"""),
        ("LC0268_MissingNumber.java", "LC0268 Missing Number",
         """public class LC0268_MissingNumber {
    public int missingNumber(int[] nums) {
        int n = nums.length, sum = n * (n + 1) / 2;
        for (int x : nums) sum -= x;
        return sum;
    }
    public static void main(String[] args) {
        LC0268_MissingNumber sol = new LC0268_MissingNumber();
        System.out.println(sol.missingNumber(new int[]{3,0,1})); // 2
        System.out.println(sol.missingNumber(new int[]{0,1})); // 2
    }
}
"""),
        ("LC0371_SumOfTwoIntegers.java", "LC0371 Sum of Two Integers",
         """public class LC0371_SumOfTwoIntegers {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }
    public static void main(String[] args) {
        LC0371_SumOfTwoIntegers sol = new LC0371_SumOfTwoIntegers();
        System.out.println(sol.getSum(1, 2)); // 3
        System.out.println(sol.getSum(2, 3)); // 5
    }
}
"""),
    ],
    "day5": [
        ("LC0097_InterleavingString.java", "LC0097 Interleaving String",
         """public class LC0097_InterleavingString {
    public boolean isInterleave(String s1, String s2, String s3) {
        int m = s1.length(), n = s2.length();
        if (m + n != s3.length()) return false;
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;
        for (int i = 1; i <= m; i++) dp[i][0] = dp[i-1][0] && s1.charAt(i-1) == s3.charAt(i-1);
        for (int j = 1; j <= n; j++) dp[0][j] = dp[0][j-1] && s2.charAt(j-1) == s3.charAt(j-1);
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++)
                dp[i][j] = (dp[i-1][j] && s1.charAt(i-1) == s3.charAt(i+j-1)) ||
                            (dp[i][j-1] && s2.charAt(j-1) == s3.charAt(i+j-1));
        return dp[m][n];
    }
    public static void main(String[] args) {
        LC0097_InterleavingString sol = new LC0097_InterleavingString();
        System.out.println(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac")); // true
    }
}
"""),
        ("LC0115_DistinctSubsequences.java", "LC0115 Distinct Subsequences",
         """public class LC0115_DistinctSubsequences {
    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        long[][] dp = new long[m + 1][n + 1];
        for (int i = 0; i <= m; i++) dp[i][0] = 1;
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++) {
                dp[i][j] = dp[i-1][j];
                if (s.charAt(i-1) == t.charAt(j-1)) dp[i][j] += dp[i-1][j-1];
            }
        return (int) dp[m][n];
    }
    public static void main(String[] args) {
        LC0115_DistinctSubsequences sol = new LC0115_DistinctSubsequences();
        System.out.println(sol.numDistinct("rabbbit", "rabbit")); // 3
    }
}
"""),
        ("LC0188_BestTimeToBuyAndSellStockIV.java", "LC0188 Best Time to Buy and Sell Stock IV",
         """public class LC0188_BestTimeToBuyAndSellStockIV {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if (n == 0 || k == 0) return 0;
        if (k >= n / 2) {
            int profit = 0;
            for (int i = 1; i < n; i++) if (prices[i] > prices[i-1]) profit += prices[i] - prices[i-1];
            return profit;
        }
        int[] buy = new int[k], sell = new int[k];
        java.util.Arrays.fill(buy, Integer.MIN_VALUE);
        for (int p : prices)
            for (int i = 0; i < k; i++) {
                buy[i] = Math.max(buy[i], (i == 0 ? 0 : sell[i-1]) - p);
                sell[i] = Math.max(sell[i], buy[i] + p);
            }
        return sell[k-1];
    }
    public static void main(String[] args) {
        LC0188_BestTimeToBuyAndSellStockIV sol = new LC0188_BestTimeToBuyAndSellStockIV();
        System.out.println(sol.maxProfit(2, new int[]{2,4,1,7})); // 9
    }
}
"""),
        ("LC0309_BestTimeCooldown.java", "LC0309 Best Time to Buy and Sell Stock with Cooldown",
         """public class LC0309_BestTimeCooldown {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) return 0;
        int held = -prices[0], sold = 0, rest = 0;
        for (int i = 1; i < prices.length; i++) {
            int prevHeld = held, prevSold = sold, prevRest = rest;
            held = Math.max(prevHeld, prevRest - prices[i]);
            sold = prevHeld + prices[i];
            rest = Math.max(prevRest, prevSold);
        }
        return Math.max(sold, rest);
    }
    public static void main(String[] args) {
        LC0309_BestTimeCooldown sol = new LC0309_BestTimeCooldown();
        System.out.println(sol.maxProfit(new int[]{1,2,3,0,2})); // 3
    }
}
"""),
        ("LC0518_CoinChangeII.java", "LC0518 Coin Change II",
         """public class LC0518_CoinChangeII {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : coins)
            for (int i = coin; i <= amount; i++)
                dp[i] += dp[i - coin];
        return dp[amount];
    }
    public static void main(String[] args) {
        LC0518_CoinChangeII sol = new LC0518_CoinChangeII();
        System.out.println(sol.change(5, new int[]{1,2,5})); // 4
    }
}
"""),
        ("LC0132_PalindromePartitioningII.java", "LC0132 Palindrome Partitioning II",
         """public class LC0132_PalindromePartitioningII {
    public int minCut(String s) {
        int n = s.length();
        boolean[][] pal = new boolean[n][n];
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = i;
            for (int j = 0; j <= i; j++) {
                if (s.charAt(j) == s.charAt(i) && (i - j <= 2 || pal[j+1][i-1])) {
                    pal[j][i] = true;
                    dp[i] = j == 0 ? 0 : Math.min(dp[i], dp[j-1] + 1);
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
    ],
    "day6": [
        ("LC0211_DesignAddSearchWords.java", "LC0211 Design Add and Search Words Data Structure",
         """public class LC0211_DesignAddSearchWords {
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
    public boolean search(String word) { return dfs(root, word, 0); }
    private boolean dfs(TrieNode node, String word, int i) {
        if (node == null) return false;
        if (i == word.length()) return node.isEnd;
        char c = word.charAt(i);
        if (c == '.') { for (TrieNode child : node.children) if (dfs(child, word, i + 1)) return true; return false; }
        return dfs(node.children[c - 'a'], word, i + 1);
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
        ("LC0212_WordSearchII.java", "LC0212 Word Search II",
         """import java.util.*;
public class LC0212_WordSearchII {
    static class Trie {
        Trie[] ch = new Trie[26]; String word;
    }
    public List<String> findWords(char[][] board, String[] words) {
        Trie root = new Trie();
        for (String w : words) { Trie cur = root; for (char c : w.toCharArray()) { if (cur.ch[c-'a']==null) cur.ch[c-'a']=new Trie(); cur=cur.ch[c-'a']; } cur.word=w; }
        List<String> res = new ArrayList<>();
        for (int i = 0; i < board.length; i++)
            for (int j = 0; j < board[0].length; j++)
                dfs(board, i, j, root, res);
        return res;
    }
    private void dfs(char[][] b, int i, int j, Trie node, List<String> res) {
        if (i<0||i>=b.length||j<0||j>=b[0].length||b[i][j]=='#') return;
        char c=b[i][j]; if (node.ch[c-'a']==null) return;
        node=node.ch[c-'a']; if (node.word!=null) { res.add(node.word); node.word=null; }
        b[i][j]='#';
        dfs(b,i+1,j,node,res); dfs(b,i-1,j,node,res); dfs(b,i,j+1,node,res); dfs(b,i,j-1,node,res);
        b[i][j]=c;
    }
    public static void main(String[] args) {
        LC0212_WordSearchII sol = new LC0212_WordSearchII();
        char[][] board={{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}};
        System.out.println(sol.findWords(board, new String[]{"oath","pea","eat","rain"})); // [eat,oath]
    }
}
"""),
        ("LC0421_MaximumXOR.java", "LC0421 Maximum XOR of Two Numbers in an Array",
         """public class LC0421_MaximumXOR {
    static class TrieNode { TrieNode[] ch = new TrieNode[2]; }
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
        int max = 0;
        for (int n : nums) {
            TrieNode cur = root; int xor = 0;
            for (int i = 31; i >= 0; i--) {
                int bit = (n >> i) & 1, want = 1 - bit;
                if (cur.ch[want] != null) { xor |= (1 << i); cur = cur.ch[want]; }
                else cur = cur.ch[bit];
            }
            max = Math.max(max, xor);
        }
        return max;
    }
    public static void main(String[] args) {
        LC0421_MaximumXOR sol = new LC0421_MaximumXOR();
        System.out.println(sol.findMaximumXOR(new int[]{3,10,5,25,2,8})); // 28
    }
}
"""),
        ("LC0472_ConcatenatedWords.java", "LC0472 Concatenated Words",
         """import java.util.*;
public class LC0472_ConcatenatedWords {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Set<String> wordSet = new HashSet<>(Arrays.asList(words));
        List<String> res = new ArrayList<>();
        for (String word : words) {
            int n = word.length();
            boolean[] dp = new boolean[n + 1];
            dp[0] = true;
            for (int i = 1; i <= n; i++)
                for (int j = 0; j < i; j++)
                    if (dp[j] && wordSet.contains(word.substring(j, i)) && !(j == 0 && i == n)) { dp[i] = true; break; }
            if (dp[n]) res.add(word);
        }
        return res;
    }
    public static void main(String[] args) {
        LC0472_ConcatenatedWords sol = new LC0472_ConcatenatedWords();
        System.out.println(sol.findAllConcatenatedWordsInADict(new String[]{"cat","cats","catsdogcats","dog","dogcatsdog","hippodogcats","rat"}));
    }
}
"""),
        ("LC0648_ReplaceWords.java", "LC0648 Replace Words",
         """import java.util.*;
public class LC0648_ReplaceWords {
    static class Trie { Trie[] ch = new Trie[26]; String root; }
    public String replaceWords(List<String> dictionary, String sentence) {
        Trie root = new Trie();
        for (String word : dictionary) {
            Trie cur = root;
            for (char c : word.toCharArray()) { if (cur.ch[c-'a']==null) cur.ch[c-'a']=new Trie(); cur=cur.ch[c-'a']; }
            cur.root = word;
        }
        StringBuilder sb = new StringBuilder();
        for (String word : sentence.split(" ")) {
            Trie cur = root; String rep = null;
            for (char c : word.toCharArray()) { if (cur.ch[c-'a']==null || cur.root!=null) { rep=cur.root; break; } cur=cur.ch[c-'a']; }
            if (rep == null) rep = word;
            if (sb.length() > 0) sb.append(' ');
            sb.append(rep);
        }
        return sb.toString();
    }
    public static void main(String[] args) {
        LC0648_ReplaceWords sol = new LC0648_ReplaceWords();
        System.out.println(sol.replaceWords(Arrays.asList("cat","bat","rat"), "the cattle was rattled by the battery"));
        // the cat was rat by the bat
    }
}
"""),
        ("LC0336_PalindromePairs.java", "LC0336 Palindrome Pairs",
         """import java.util.*;
public class LC0336_PalindromePairs {
    public List<List<Integer>> palindromePairs(String[] words) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < words.length; i++) map.put(words[i], i);
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j <= words[i].length(); j++) {
                String prefix = words[i].substring(0, j), suffix = words[i].substring(j);
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
    private boolean isPalin(String s) { int l=0,r=s.length()-1; while(l<r) if(s.charAt(l++)!=s.charAt(r--)) return false; return true; }
    public static void main(String[] args) {
        LC0336_PalindromePairs sol = new LC0336_PalindromePairs();
        System.out.println(sol.palindromePairs(new String[]{"abcd","dcba","lls","s","sssll"})); // [[0,1],[1,0],[3,2],[2,4]]
    }
}
"""),
    ],
    "day7": [
        ("LC0297_SerializeDeserializeBinaryTree.java", "LC0297 Serialize and Deserialize Binary Tree",
         """import java.util.*;
public class LC0297_SerializeDeserializeBinaryTree {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    public String serialize(TreeNode root) {
        if (root == null) return "#";
        return root.val + "," + serialize(root.left) + "," + serialize(root.right);
    }
    private int idx;
    public TreeNode deserialize(String data) {
        idx = 0;
        String[] parts = data.split(",");
        return build(parts);
    }
    private TreeNode build(String[] parts) {
        if (idx >= parts.length || parts[idx].equals("#")) { idx++; return null; }
        TreeNode node = new TreeNode(Integer.parseInt(parts[idx++]));
        node.left = build(parts); node.right = build(parts);
        return node;
    }
    public static void main(String[] args) {
        LC0297_SerializeDeserializeBinaryTree sol = new LC0297_SerializeDeserializeBinaryTree();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2); root.right = new TreeNode(3);
        root.right.left = new TreeNode(4); root.right.right = new TreeNode(5);
        String s = sol.serialize(root);
        System.out.println(s); // 1,2,#,#,3,4,#,#,5,#,#
        TreeNode rebuilt = sol.deserialize(s);
        System.out.println(sol.serialize(rebuilt));
    }
}
"""),
        ("LC0450_DeleteNodeInBST.java", "LC0450 Delete Node in a BST",
         """public class LC0450_DeleteNodeInBST {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (key < root.val) root.left = deleteNode(root.left, key);
        else if (key > root.val) root.right = deleteNode(root.right, key);
        else {
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            TreeNode min = root.right;
            while (min.left != null) min = min.left;
            root.val = min.val;
            root.right = deleteNode(root.right, min.val);
        }
        return root;
    }
    public static void main(String[] args) {
        LC0450_DeleteNodeInBST sol = new LC0450_DeleteNodeInBST();
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(3); root.right = new TreeNode(6);
        root.left.left = new TreeNode(2); root.left.right = new TreeNode(4);
        root.right.right = new TreeNode(7);
        TreeNode res = sol.deleteNode(root, 3);
        System.out.println(res.left.val); // 4 or 2 depending on impl
    }
}
"""),
        ("LC0538_ConvertBSTToGreaterTree.java", "LC0538 Convert BST to Greater Tree",
         """public class LC0538_ConvertBSTToGreaterTree {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    int sum = 0;
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
        root.left = new TreeNode(1); root.right = new TreeNode(6);
        TreeNode res = sol.convertBST(root);
        System.out.println(res.val); // 10
    }
}
"""),
        ("LC0543_DiameterOfBinaryTree.java", "LC0543 Diameter of Binary Tree",
         """public class LC0543_DiameterOfBinaryTree {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    int max = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        depth(root);
        return max;
    }
    private int depth(TreeNode node) {
        if (node == null) return 0;
        int l = depth(node.left), r = depth(node.right);
        max = Math.max(max, l + r);
        return 1 + Math.max(l, r);
    }
    public static void main(String[] args) {
        LC0543_DiameterOfBinaryTree sol = new LC0543_DiameterOfBinaryTree();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2); root.right = new TreeNode(3);
        root.left.left = new TreeNode(4); root.left.right = new TreeNode(5);
        System.out.println(sol.diameterOfBinaryTree(root)); // 3
    }
}
"""),
        ("LC0572_SubtreeOfAnotherTree.java", "LC0572 Subtree of Another Tree",
         """public class LC0572_SubtreeOfAnotherTree {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
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
        root.left = new TreeNode(4); root.right = new TreeNode(5);
        root.left.left = new TreeNode(1); root.left.right = new TreeNode(2);
        TreeNode sub = new TreeNode(4);
        sub.left = new TreeNode(1); sub.right = new TreeNode(2);
        System.out.println(sol.isSubtree(root, sub)); // true
    }
}
"""),
        ("LC0652_FindDuplicateSubtrees.java", "LC0652 Find Duplicate Subtrees",
         """import java.util.*;
public class LC0652_FindDuplicateSubtrees {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    Map<String, Integer> count = new HashMap<>();
    List<TreeNode> res = new ArrayList<>();
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        serialize(root); return res;
    }
    private String serialize(TreeNode node) {
        if (node == null) return "#";
        String key = node.val + "," + serialize(node.left) + "," + serialize(node.right);
        count.merge(key, 1, Integer::sum);
        if (count.get(key) == 2) res.add(node);
        return key;
    }
    public static void main(String[] args) {
        LC0652_FindDuplicateSubtrees sol = new LC0652_FindDuplicateSubtrees();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2); root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.right.left = new TreeNode(2); root.right.right = new TreeNode(4);
        root.right.left.left = new TreeNode(4);
        List<TreeNode> dups = sol.findDuplicateSubtrees(root);
        for (TreeNode n : dups) System.out.print(n.val + " "); // 2 4
    }
}
"""),
    ],
}

# ---------------------------------------------------------------------------
# Day-script template
# ---------------------------------------------------------------------------
DAY_SCRIPTS = {}
for day_key, problems in DAYS.items():
    day_num = day_key.replace("day", "")
    blocks = []
    for fname, title, _ in problems:
        lc_num = fname[:6]  # e.g. LC0127
        problem_title = title  # e.g. "LC0127 Word Ladder"
        commit_msg = f"feat(leetcode): solve {lc_num} {title.split(' ', 1)[1]} in Java"
        block = f"""
# --- {problem_title} ---
FILE="staging/{day_key}/{fname}"
if git ls-files --error-unmatch "$FILE" > /dev/null 2>&1; then
  echo "SKIP: {problem_title} already committed."
else
  git add "$FILE"
  git commit -m "{commit_msg}"
  echo "COMMITTED: {problem_title}"
fi
"""
        blocks.append(block)
    DAY_SCRIPTS[day_key] = f"""#!/bin/sh
# day{day_num}.sh — Week 3 Day {day_num} submission runner
set -e
echo "=== Week 3 Day {day_num} ==="
{"".join(blocks)}
git push origin main
echo "=== Day {day_num} push complete ==="
"""

# ---------------------------------------------------------------------------
# auto_submit.sh — detects which day to run next
# ---------------------------------------------------------------------------
def build_problem_list():
    lines = []
    for day_key, problems in DAYS.items():
        for fname, title, _ in problems:
            lines.append(f'  "staging/{day_key}/{fname}"')
    return "\n".join(lines)

def build_day_checks():
    lines = []
    for day_key in sorted(DAYS.keys()):
        day_num = day_key.replace("day", "")
        lines.append(f"""
  # Check Day {day_num}
  DAY{day_num}_DONE=1
  for f in staging/{day_key}/*.java; do
    if ! git ls-files --error-unmatch "$f" > /dev/null 2>&1; then
      DAY{day_num}_DONE=0
      break
    fi
  done
  if [ "$DAY{day_num}_DONE" = "0" ]; then
    echo ">>> Running Day {day_num}..."
    sh day{day_num}.sh
    echo "Day {day_num} complete."
    exit 0
  else
    echo "Day {day_num}: already fully submitted."
  fi""")
    return "\n".join(lines)

AUTO_SUBMIT = f"""#!/bin/sh
# auto_submit.sh — Week 3 auto-detector & runner
# Detects which day has pending submissions and runs it.
set -e
echo "=============================="
echo " LeetCode Auto-Submit Week 3  "
echo "=============================="
echo ""
echo "Checking submission status..."
echo ""
{build_day_checks()}
echo ""
echo "DONE: All Week 3 days are fully submitted!"
"""

RUN_DAY = """#!/bin/sh
# run_day.sh — master runner
sh auto_submit.sh
"""

def write_lf(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="\n", encoding="utf-8") as f:
        f.write(content)
    print(f"  WROTE: {os.path.relpath(path, ROOT)}")

def generate_all_solutions():
    print("Generating Week 3 Java solutions...")
    for day_key, problems in DAYS.items():
        day_dir = os.path.join(STAGING, day_key)
        os.makedirs(day_dir, exist_ok=True)
        for fname, title, code in problems:
            path = os.path.join(day_dir, fname)
            write_lf(path, code)
    print(f"  Total: {sum(len(v) for v in DAYS.values())} Java files written.")

def generate_day_scripts():
    print("Generating day shell scripts...")
    for day_key, script_content in DAY_SCRIPTS.items():
        day_num = day_key.replace("day", "")
        path = os.path.join(ROOT, f"day{day_num}.sh")
        write_lf(path, script_content)

def generate_auto_detector():
    print("Generating auto_submit.sh and run_day.sh...")
    write_lf(os.path.join(ROOT, "auto_submit.sh"), AUTO_SUBMIT)
    write_lf(os.path.join(ROOT, "run_day.sh"), RUN_DAY)

if __name__ == "__main__":
    generate_all_solutions()
    generate_day_scripts()
    generate_auto_detector()
    print("\nWeek 3 suite generation complete!")
    print("Next: compile-verify with javac, then run auto_submit.sh")
