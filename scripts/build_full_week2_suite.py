"""
build_full_week2_suite.py
Complete generator for Week 2 (42 LeetCode Java problems across 7 days)
+ Intelligent Auto-Detector & Runner scripts.
"""

import os
import sys

ROOT = r"E:\LeetCode-Solutions-Java"

PROBLEMS = {
    # -------------------------------------------------------------
    # Day 1: Arrays, Two Pointers & In-Place Manipulations
    # -------------------------------------------------------------
    1: [
        ("LC0018_4Sum.java", "LC0018 4Sum", """import java.util.*;

/**
 * Problem: 18. 4Sum
 * Difficulty: Medium
 * Category: Array, Two Pointers, Sorting
 *
 * Algorithm:
 * Sort array, use two outer loops and two pointers for remaining two elements.
 * Use long to avoid integer overflow during 4-sum comparison.
 * Skip duplicates at each stage to avoid duplicate quadruplets.
 *
 * Time Complexity: O(N^3)
 * Space Complexity: O(1) auxiliary (ignoring output list)
 */
public class LC0018_4Sum {

    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums == null || nums.length < 4) return result;

        Arrays.sort(nums);
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                int left = j + 1;
                int right = n - 1;

                while (left < right) {
                    long sum = (long) nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        LC0018_4Sum solver = new LC0018_4Sum();
        int[] nums = {1, 0, -1, 0, -2, 2};
        List<List<Integer>> ans = solver.fourSum(nums, 0);
        assert ans.size() == 3;
        System.out.println("LC0018_4Sum passed all tests!");
    }
}
"""),
        ("LC0027_RemoveElement.java", "LC0027 Remove Element", """import java.util.Arrays;

/**
 * Problem: 27. Remove Element
 * Difficulty: Easy
 * Category: Array, Two Pointers
 *
 * Algorithm:
 * Fast-slow pointer: copy non-val elements to the front of the array.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0027_RemoveElement {

    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }

    public static void main(String[] args) {
        LC0027_RemoveElement solver = new LC0027_RemoveElement();
        int[] nums = {3, 2, 2, 3};
        int k = solver.removeElement(nums, 3);
        assert k == 2;
        assert nums[0] == 2 && nums[1] == 2;
        System.out.println("LC0027_RemoveElement passed all tests!");
    }
}
"""),
        ("LC0080_RemoveDuplicatesFromSortedArrayII.java", "LC0080 Remove Duplicates from Sorted Array II", """import java.util.Arrays;

/**
 * Problem: 80. Remove Duplicates from Sorted Array II
 * Difficulty: Medium
 * Category: Array, Two Pointers
 *
 * Algorithm:
 * Maintain index k. An element can be placed if k < 2 or nums[i] > nums[k - 2].
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0080_RemoveDuplicatesFromSortedArrayII {

    public int removeDuplicates(int[] nums) {
        if (nums.length <= 2) return nums.length;

        int k = 2;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] != nums[k - 2]) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }

    public static void main(String[] args) {
        LC0080_RemoveDuplicatesFromSortedArrayII solver = new LC0080_RemoveDuplicatesFromSortedArrayII();
        int[] nums = {1, 1, 1, 2, 2, 3};
        int k = solver.removeDuplicates(nums);
        assert k == 5;
        System.out.println("LC0080_RemoveDuplicatesFromSortedArrayII passed all tests!");
    }
}
"""),
        ("LC0088_MergeSortedArray.java", "LC0088 Merge Sorted Array", """import java.util.Arrays;

/**
 * Problem: 88. Merge Sorted Array
 * Difficulty: Easy
 * Category: Array, Two Pointers, Sorting
 *
 * Algorithm:
 * 3-Pointer reverse filling from the end of nums1 to prevent overwriting existing elements.
 *
 * Time Complexity: O(M + N)
 * Space Complexity: O(1)
 */
public class LC0088_MergeSortedArray {

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1;
        int p2 = n - 1;
        int p = m + n - 1;

        while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2]) {
                nums1[p--] = nums1[p1--];
            } else {
                nums1[p--] = nums2[p2--];
            }
        }

        while (p2 >= 0) {
            nums1[p--] = nums2[p2--];
        }
    }

    public static void main(String[] args) {
        LC0088_MergeSortedArray solver = new LC0088_MergeSortedArray();
        int[] nums1 = {1, 2, 3, 0, 0, 0};
        int[] nums2 = {2, 5, 6};
        solver.merge(nums1, 3, nums2, 3);
        assert Arrays.equals(nums1, new int[]{1, 2, 2, 3, 5, 6});
        System.out.println("LC0088_MergeSortedArray passed all tests!");
    }
}
"""),
        ("LC0209_MinimumSizeSubarraySum.java", "LC0209 Minimum Size Subarray Sum", """/**
 * Problem: 209. Minimum Size Subarray Sum
 * Difficulty: Medium
 * Category: Array, Binary Search, Sliding Window
 *
 * Algorithm:
 * Sliding window: expand right pointer until sum >= target, then shrink left pointer
 * while maintaining sum >= target, tracking the minimum window length.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0209_MinimumSizeSubarraySum {

    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int sum = 0;
        int minLen = Integer.MAX_VALUE;

        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];

            while (sum >= target) {
                minLen = Math.min(minLen, right - left + 1);
                sum -= nums[left++];
            }
        }
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }

    public static void main(String[] args) {
        LC0209_MinimumSizeSubarraySum solver = new LC0209_MinimumSizeSubarraySum();
        int[] nums = {2, 3, 1, 2, 4, 3};
        assert solver.minSubArrayLen(7, nums) == 2;
        System.out.println("LC0209_MinimumSizeSubarraySum passed all tests!");
    }
}
"""),
        ("LC0283_MoveZeroes.java", "LC0283 Move Zeroes", """import java.util.Arrays;

/**
 * Problem: 283. Move Zeroes
 * Difficulty: Easy
 * Category: Array, Two Pointers
 *
 * Algorithm:
 * Two pointer: maintain insertPosition. Iterate through array; whenever non-zero is found,
 * swap with insertPosition and advance insertPosition.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0283_MoveZeroes {

    public void moveZeroes(int[] nums) {
        int insertPos = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int temp = nums[insertPos];
                nums[insertPos] = nums[i];
                nums[i] = temp;
                insertPos++;
            }
        }
    }

    public static void main(String[] args) {
        LC0283_MoveZeroes solver = new LC0283_MoveZeroes();
        int[] nums = {0, 1, 0, 3, 12};
        solver.moveZeroes(nums);
        assert Arrays.equals(nums, new int[]{1, 3, 12, 0, 0});
        System.out.println("LC0283_MoveZeroes passed all tests!");
    }
}
"""),
    ],

    # -------------------------------------------------------------
    # Day 2: Linked Lists & Two-Pointer Traversals
    # -------------------------------------------------------------
    2: [
        ("LC0082_RemoveDuplicatesFromSortedListII.java", "LC0082 Remove Duplicates from Sorted List II", """/**
 * Problem: 82. Remove Duplicates from Sorted List II
 * Difficulty: Medium
 * Category: Linked List, Two Pointers
 *
 * Algorithm:
 * Use a sentinel/dummy head. When current node has a duplicate value ahead,
 * skip all contiguous nodes with that value.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0082_RemoveDuplicatesFromSortedListII {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        while (head != null) {
            if (head.next != null && head.val == head.next.val) {
                while (head.next != null && head.val == head.next.val) {
                    head = head.next;
                }
                prev.next = head.next;
            } else {
                prev = prev.next;
            }
            head = head.next;
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        LC0082_RemoveDuplicatesFromSortedListII solver = new LC0082_RemoveDuplicatesFromSortedListII();
        ListNode h = new ListNode(1);
        h.next = new ListNode(2);
        h.next.next = new ListNode(2);
        h.next.next.next = new ListNode(3);
        ListNode res = solver.deleteDuplicates(h);
        assert res.val == 1 && res.next.val == 3 && res.next.next == null;
        System.out.println("LC0082_RemoveDuplicatesFromSortedListII passed all tests!");
    }
}
"""),
        ("LC0083_RemoveDuplicatesFromSortedList.java", "LC0083 Remove Duplicates from Sorted List", """/**
 * Problem: 83. Remove Duplicates from Sorted List
 * Difficulty: Easy
 * Category: Linked List
 *
 * Algorithm:
 * Single pass: compare current node with current.next. If equal, drop next node.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0083_RemoveDuplicatesFromSortedList {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public ListNode deleteDuplicates(ListNode head) {
        ListNode curr = head;
        while (curr != null && curr.next != null) {
            if (curr.val == curr.next.val) {
                curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }
        return head;
    }

    public static void main(String[] args) {
        LC0083_RemoveDuplicatesFromSortedList solver = new LC0083_RemoveDuplicatesFromSortedList();
        ListNode h = new ListNode(1);
        h.next = new ListNode(1);
        h.next.next = new ListNode(2);
        ListNode res = solver.deleteDuplicates(h);
        assert res.val == 1 && res.next.val == 2 && res.next.next == null;
        System.out.println("LC0083_RemoveDuplicatesFromSortedList passed all tests!");
    }
}
"""),
        ("LC0086_PartitionList.java", "LC0086 Partition List", """/**
 * Problem: 86. Partition List
 * Difficulty: Medium
 * Category: Linked List, Two Pointers
 *
 * Algorithm:
 * Maintain two separate sublists (before and after), appending nodes based on val < x.
 * Connect before list tail to after list head.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0086_PartitionList {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public ListNode partition(ListNode head, int x) {
        ListNode beforeHead = new ListNode(0);
        ListNode afterHead = new ListNode(0);
        ListNode before = beforeHead;
        ListNode after = afterHead;

        while (head != null) {
            if (head.val < x) {
                before.next = head;
                before = before.next;
            } else {
                after.next = head;
                after = after.next;
            }
            head = head.next;
        }

        after.next = null;
        before.next = afterHead.next;
        return beforeHead.next;
    }

    public static void main(String[] args) {
        LC0086_PartitionList solver = new LC0086_PartitionList();
        ListNode h = new ListNode(1);
        h.next = new ListNode(4);
        h.next.next = new ListNode(3);
        h.next.next.next = new ListNode(2);
        ListNode res = solver.partition(h, 3);
        assert res.val == 1 && res.next.val == 2;
        System.out.println("LC0086_PartitionList passed all tests!");
    }
}
"""),
        ("LC0092_ReverseLinkedListII.java", "LC0092 Reverse Linked List II", """/**
 * Problem: 92. Reverse Linked List II
 * Difficulty: Medium
 * Category: Linked List
 *
 * Algorithm:
 * Move to node right before left. Iteratively insert each subsequent node
 * up to right between prev and prev.next.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0092_ReverseLinkedListII {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || left == right) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        for (int i = 0; i < left - 1; i++) {
            prev = prev.next;
        }

        ListNode curr = prev.next;
        for (int i = 0; i < right - left; i++) {
            ListNode next = curr.next;
            curr.next = next.next;
            next.next = prev.next;
            prev.next = next;
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        LC0092_ReverseLinkedListII solver = new LC0092_ReverseLinkedListII();
        ListNode h = new ListNode(1);
        h.next = new ListNode(2);
        h.next.next = new ListNode(3);
        h.next.next.next = new ListNode(4);
        ListNode res = solver.reverseBetween(h, 2, 3);
        assert res.next.val == 3 && res.next.next.val == 2;
        System.out.println("LC0092_ReverseLinkedListII passed all tests!");
    }
}
"""),
        ("LC0160_IntersectionOfTwoLinkedLists.java", "LC0160 Intersection of Two Linked Lists", """/**
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
"""),
        ("LC0203_RemoveLinkedListElements.java", "LC0203 Remove Linked List Elements", """/**
 * Problem: 203. Remove Linked List Elements
 * Difficulty: Easy
 * Category: Linked List, Recursion
 *
 * Algorithm:
 * Sentinel/dummy node allows uniform deletion even when target is at head.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0203_RemoveLinkedListElements {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy;

        while (curr.next != null) {
            if (curr.next.val == val) {
                curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        LC0203_RemoveLinkedListElements solver = new LC0203_RemoveLinkedListElements();
        ListNode h = new ListNode(1);
        h.next = new ListNode(2);
        h.next.next = new ListNode(6);
        h.next.next.next = new ListNode(3);
        ListNode res = solver.removeElements(h, 6);
        assert res.next.next.val == 3;
        System.out.println("LC0203_RemoveLinkedListElements passed all tests!");
    }
}
"""),
    ],

    # -------------------------------------------------------------
    # Day 3: Strings & Parsing / Math
    # -------------------------------------------------------------
    3: [
        ("LC0006_ZigzagConversion.java", "LC0006 Zigzag Conversion", """import java.util.ArrayList;
import java.util.List;

/**
 * Problem: 6. Zigzag Conversion
 * Difficulty: Medium
 * Category: String
 *
 * Algorithm:
 * Simulate writing across numRows string builders, tracking direction (goingDown).
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0006_ZigzagConversion {

    public String convert(String s, int numRows) {
        if (numRows == 1 || s.length() <= numRows) return s;

        List<StringBuilder> rows = new ArrayList<>();
        for (int i = 0; i < numRows; i++) rows.add(new StringBuilder());

        int curRow = 0;
        boolean goingDown = false;

        for (char c : s.toCharArray()) {
            rows.get(curRow).append(c);
            if (curRow == 0 || curRow == numRows - 1) {
                goingDown = !goingDown;
            }
            curRow += goingDown ? 1 : -1;
        }

        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) result.append(row);
        return result.toString();
    }

    public static void main(String[] args) {
        LC0006_ZigzagConversion solver = new LC0006_ZigzagConversion();
        assert solver.convert("PAYPALISHIRING", 3).equals("PAHNAPLSIIGYIR");
        System.out.println("LC0006_ZigzagConversion passed all tests!");
    }
}
"""),
        ("LC0012_IntegerToRoman.java", "LC0012 Integer to Roman", """/**
 * Problem: 12. Integer to Roman
 * Difficulty: Medium
 * Category: Hash Table, Math, String
 *
 * Algorithm:
 * Greedy value extraction using ordered symbol/value tables.
 *
 * Time Complexity: O(1) bounded by 3999
 * Space Complexity: O(1)
 */
public class LC0012_IntegerToRoman {

    private static final int[] VALUES = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    private static final String[] SYMBOLS = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    public String intToRoman(int num) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < VALUES.length && num > 0; i++) {
            while (num >= VALUES[i]) {
                num -= VALUES[i];
                sb.append(SYMBOLS[i]);
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        LC0012_IntegerToRoman solver = new LC0012_IntegerToRoman();
        assert solver.intToRoman(3749).equals("MMMDCCXLIX");
        assert solver.intToRoman(58).equals("LVIII");
        System.out.println("LC0012_IntegerToRoman passed all tests!");
    }
}
"""),
        ("LC0013_RomanToInteger.java", "LC0013 Roman to Integer", """import java.util.HashMap;
import java.util.Map;

/**
 * Problem: 13. Roman to Integer
 * Difficulty: Easy
 * Category: Hash Table, Math, String
 *
 * Algorithm:
 * Left-to-right scan: if current value < next value, subtract current value; otherwise add.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0013_RomanToInteger {

    public int romanToInt(String s) {
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        int total = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            int val = map.get(s.charAt(i));
            if (i < n - 1 && val < map.get(s.charAt(i + 1))) {
                total -= val;
            } else {
                total += val;
            }
        }
        return total;
    }

    public static void main(String[] args) {
        LC0013_RomanToInteger solver = new LC0013_RomanToInteger();
        assert solver.romanToInt("III") == 3;
        assert solver.romanToInt("LVIII") == 58;
        assert solver.romanToInt("MCMXCIV") == 1994;
        System.out.println("LC0013_RomanToInteger passed all tests!");
    }
}
"""),
        ("LC0043_MultiplyStrings.java", "LC0043 Multiply Strings", """/**
 * Problem: 43. Multiply Strings
 * Difficulty: Medium
 * Category: Math, String, Simulation
 *
 * Algorithm:
 * Grade-school multiplication: result of num1[i] * num2[j] sits at indices [i + j, i + j + 1].
 *
 * Time Complexity: O(N * M)
 * Space Complexity: O(N + M)
 */
public class LC0043_MultiplyStrings {

    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) return "0";

        int n = num1.length();
        int m = num2.length();
        int[] pos = new int[n + m];

        for (int i = n - 1; i >= 0; i--) {
            int d1 = num1.charAt(i) - '0';
            for (int j = m - 1; j >= 0; j--) {
                int d2 = num2.charAt(j) - '0';
                int mul = d1 * d2;
                int p1 = i + j;
                int p2 = i + j + 1;
                int sum = mul + pos[p2];

                pos[p2] = sum % 10;
                pos[p1] += sum / 10;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int p : pos) {
            if (!(sb.length() == 0 && p == 0)) {
                sb.append(p);
            }
        }
        return sb.length() == 0 ? "0" : sb.toString();
    }

    public static void main(String[] args) {
        LC0043_MultiplyStrings solver = new LC0043_MultiplyStrings();
        assert solver.multiply("2", "3").equals("6");
        assert solver.multiply("123", "456").equals("56088");
        System.out.println("LC0043_MultiplyStrings passed all tests!");
    }
}
"""),
        ("LC0058_LengthOfLastWord.java", "LC0058 Length of Last Word", """/**
 * Problem: 58. Length of Last Word
 * Difficulty: Easy
 * Category: String
 *
 * Algorithm:
 * Reverse scan: skip trailing spaces, then count characters until next space.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0058_LengthOfLastWord {

    public int lengthOfLastWord(String s) {
        int length = 0;
        int i = s.length() - 1;

        while (i >= 0 && s.charAt(i) == ' ') {
            i--;
        }

        while (i >= 0 && s.charAt(i) != ' ') {
            length++;
            i--;
        }
        return length;
    }

    public static void main(String[] args) {
        LC0058_LengthOfLastWord solver = new LC0058_LengthOfLastWord();
        assert solver.lengthOfLastWord("Hello World") == 5;
        assert solver.lengthOfLastWord("   fly me   to   the moon  ") == 4;
        System.out.println("LC0058_LengthOfLastWord passed all tests!");
    }
}
"""),
        ("LC0125_ValidPalindrome.java", "LC0125 Valid Palindrome", """/**
 * Problem: 125. Valid Palindrome
 * Difficulty: Easy
 * Category: Two Pointers, String
 *
 * Algorithm:
 * Two pointers from both ends, filtering non-alphanumeric and comparing case-insensitively.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0125_ValidPalindrome {

    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String[] args) {
        LC0125_ValidPalindrome solver = new LC0125_ValidPalindrome();
        assert solver.isPalindrome("A man, a plan, a canal: Panama");
        assert !solver.isPalindrome("race a car");
        System.out.println("LC0125_ValidPalindrome passed all tests!");
    }
}
"""),
    ],

    # -------------------------------------------------------------
    # Day 4: Binary Search & Intervals
    # -------------------------------------------------------------
    4: [
        ("LC0057_InsertInterval.java", "LC0057 Insert Interval", """import java.util.*;

/**
 * Problem: 57. Insert Interval
 * Difficulty: Medium
 * Category: Array, Intervals
 *
 * Algorithm:
 * 1. Add all intervals ending before newInterval starts.
 * 2. Merge all overlapping intervals with newInterval.
 * 3. Add all remaining intervals.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N) for output
 */
public class LC0057_InsertInterval {

    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        int i = 0;
        int n = intervals.length;

        // 1. Non-overlapping before
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.add(intervals[i++]);
        }

        // 2. Overlapping: merge
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.add(newInterval);

        // 3. Non-overlapping after
        while (i < n) {
            result.add(intervals[i++]);
        }

        return result.toArray(new int[result.size()][]);
    }

    public static void main(String[] args) {
        LC0057_InsertInterval solver = new LC0057_InsertInterval();
        int[][] intervals = {{1, 3}, {6, 9}};
        int[] newInterval = {2, 5};
        int[][] res = solver.insert(intervals, newInterval);
        assert res.length == 2;
        assert res[0][0] == 1 && res[0][1] == 5;
        System.out.println("LC0057_InsertInterval passed all tests!");
    }
}
"""),
        ("LC0081_SearchInRotatedSortedArrayII.java", "LC0081 Search in Rotated Sorted Array II", """/**
 * Problem: 81. Search in Rotated Sorted Array II
 * Difficulty: Medium
 * Category: Array, Binary Search
 *
 * Algorithm:
 * Rotated binary search with duplicates: when nums[left] == nums[mid] == nums[right],
 * shrink bounds (left++, right--); otherwise identify sorted half.
 *
 * Time Complexity: O(log N) average, O(N) worst-case with all duplicates
 * Space Complexity: O(1)
 */
public class LC0081_SearchInRotatedSortedArrayII {

    public boolean search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) return true;

            if (nums[left] == nums[mid] && nums[mid] == nums[right]) {
                left++;
                right--;
            } else if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        LC0081_SearchInRotatedSortedArrayII solver = new LC0081_SearchInRotatedSortedArrayII();
        int[] nums = {2, 5, 6, 0, 0, 1, 2};
        assert solver.search(nums, 0);
        assert !solver.search(nums, 3);
        System.out.println("LC0081_SearchInRotatedSortedArrayII passed all tests!");
    }
}
"""),
        ("LC0162_FindPeakElement.java", "LC0162 Find Peak Element", """/**
 * Problem: 162. Find Peak Element
 * Difficulty: Medium
 * Category: Array, Binary Search
 *
 * Algorithm:
 * Binary search: if nums[mid] < nums[mid + 1], a peak must exist in the right half.
 * Otherwise, a peak exists in the left half including mid.
 *
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */
public class LC0162_FindPeakElement {

    public int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    public static void main(String[] args) {
        LC0162_FindPeakElement solver = new LC0162_FindPeakElement();
        int[] nums = {1, 2, 3, 1};
        assert solver.findPeakElement(nums) == 2;
        System.out.println("LC0162_FindPeakElement passed all tests!");
    }
}
"""),
        ("LC0278_FirstBadVersion.java", "LC0278 First Bad Version", """/**
 * Problem: 278. First Bad Version
 * Difficulty: Easy
 * Category: Binary Search, Interactive
 *
 * Algorithm:
 * Binary search for boundary: if isBadVersion(mid) is true, search left half including mid;
 * otherwise search right half (mid + 1).
 *
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */
public class LC0278_FirstBadVersion {

    private int badVersion = 4;
    public boolean isBadVersion(int version) {
        return version >= badVersion;
    }

    public int firstBadVersion(int n) {
        int left = 1;
        int right = n;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    public static void main(String[] args) {
        LC0278_FirstBadVersion solver = new LC0278_FirstBadVersion();
        assert solver.firstBadVersion(5) == 4;
        System.out.println("LC0278_FirstBadVersion passed all tests!");
    }
}
"""),
        ("LC0704_BinarySearch.java", "LC0704 Binary Search", """/**
 * Problem: 704. Binary Search
 * Difficulty: Easy
 * Category: Array, Binary Search
 *
 * Algorithm:
 * Standard closed-range [left, right] binary search with overflow-safe midpoint.
 *
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */
public class LC0704_BinarySearch {

    public int search(int[] nums, int target) {
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
        return -1;
    }

    public static void main(String[] args) {
        LC0704_BinarySearch solver = new LC0704_BinarySearch();
        int[] nums = {-1, 0, 3, 5, 9, 12};
        assert solver.search(nums, 9) == 4;
        assert solver.search(nums, 2) == -1;
        System.out.println("LC0704_BinarySearch passed all tests!");
    }
}
"""),
        ("LC0875_KokoEatingBananas.java", "LC0875 Koko Eating Bananas", """/**
 * Problem: 875. Koko Eating Bananas
 * Difficulty: Medium
 * Category: Array, Binary Search on Answer
 *
 * Algorithm:
 * Binary search speed k in range [1, max(piles)].
 * For each speed, calculate hours needed: sum(ceil(pile / k)).
 *
 * Time Complexity: O(N * log(max(piles)))
 * Space Complexity: O(1)
 */
public class LC0875_KokoEatingBananas {

    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = 0;
        for (int p : piles) {
            if (p > right) right = p;
        }

        int ans = right;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canFinish(piles, mid, h)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }

    private boolean canFinish(int[] piles, int speed, int h) {
        long hours = 0;
        for (int p : piles) {
            hours += (p + speed - 1) / speed;
        }
        return hours <= h;
    }

    public static void main(String[] args) {
        LC0875_KokoEatingBananas solver = new LC0875_KokoEatingBananas();
        int[] piles = {3, 6, 7, 11};
        assert solver.minEatingSpeed(piles, 8) == 4;
        System.out.println("LC0875_KokoEatingBananas passed all tests!");
    }
}
"""),
    ],

    # -------------------------------------------------------------
    # Day 5: Trees & DFS/BFS
    # -------------------------------------------------------------
    5: [
        ("LC0108_ConvertSortedArrayToBST.java", "LC0108 Convert Sorted Array to Binary Search Tree", """/**
 * Problem: 108. Convert Sorted Array to Binary Search Tree
 * Difficulty: Easy
 * Category: Tree, Binary Search Tree, Binary Tree, Divide and Conquer
 *
 * Algorithm:
 * Recursively pick the middle element of the array slice as root, constructing left
 * and right subtrees from left and right halves respectively to maintain height-balance.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(log N) recursion stack
 */
public class LC0108_ConvertSortedArrayToBST {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums == null || nums.length == 0) return null;
        return build(nums, 0, nums.length - 1);
    }

    private TreeNode build(int[] nums, int left, int right) {
        if (left > right) return null;
        int mid = left + (right - left) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = build(nums, left, mid - 1);
        root.right = build(nums, mid + 1, right);
        return root;
    }

    public static void main(String[] args) {
        LC0108_ConvertSortedArrayToBST solver = new LC0108_ConvertSortedArrayToBST();
        int[] nums = {-10, -3, 0, 5, 9};
        TreeNode root = solver.sortedArrayToBST(nums);
        assert root != null && root.val == 0;
        System.out.println("LC0108_ConvertSortedArrayToBST passed all tests!");
    }
}
"""),
        ("LC0111_MinimumDepthOfBinaryTree.java", "LC0111 Minimum Depth of Binary Tree", """import java.util.LinkedList;
import java.util.Queue;

/**
 * Problem: 111. Minimum Depth of Binary Tree
 * Difficulty: Easy
 * Category: Tree, Depth-First Search, Breadth-First Search, Binary Tree
 *
 * Algorithm:
 * BFS level-order traversal: the very first leaf node encountered is guaranteed
 * to be at the minimum depth.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
public class LC0111_MinimumDepthOfBinaryTree {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    public int minDepth(TreeNode root) {
        if (root == null) return 0;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int depth = 1;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode curr = queue.poll();
                if (curr.left == null && curr.right == null) {
                    return depth;
                }
                if (curr.left != null) queue.offer(curr.left);
                if (curr.right != null) queue.offer(curr.right);
            }
            depth++;
        }
        return depth;
    }

    public static void main(String[] args) {
        LC0111_MinimumDepthOfBinaryTree solver = new LC0111_MinimumDepthOfBinaryTree();
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        assert solver.minDepth(root) == 2;
        System.out.println("LC0111_MinimumDepthOfBinaryTree passed all tests!");
    }
}
"""),
        ("LC0112_PathSum.java", "LC0112 Path Sum", """/**
 * Problem: 112. Path Sum
 * Difficulty: Easy
 * Category: Tree, Depth-First Search, Binary Tree
 *
 * Algorithm:
 * DFS: Subtract current root value from targetSum. If at a leaf, check if remainder is 0.
 * Otherwise, recurse on left and right children.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(H) where H is tree height
 */
public class LC0112_PathSum {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        if (root.left == null && root.right == null) {
            return root.val == targetSum;
        }
        return hasPathSum(root.left, targetSum - root.val) ||
               hasPathSum(root.right, targetSum - root.val);
    }

    public static void main(String[] args) {
        LC0112_PathSum solver = new LC0112_PathSum();
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(4);
        root.right = new TreeNode(8);
        root.left.left = new TreeNode(11);
        root.left.left.left = new TreeNode(7);
        root.left.left.right = new TreeNode(2);
        assert solver.hasPathSum(root, 22);
        assert !solver.hasPathSum(root, 100);
        System.out.println("LC0112_PathSum passed all tests!");
    }
}
"""),
        ("LC0113_PathSumII.java", "LC0113 Path Sum II", """import java.util.ArrayList;
import java.util.List;

/**
 * Problem: 113. Path Sum II
 * Difficulty: Medium
 * Category: Tree, Backtracking, Depth-First Search, Binary Tree
 *
 * Algorithm:
 * DFS backtracking: collect node values into a current path list.
 * When reaching a leaf where remainder equals node.val, save a copy of path.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(H) recursion stack
 */
public class LC0113_PathSumII {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> currentPath = new ArrayList<>();
        dfs(root, targetSum, currentPath, result);
        return result;
    }

    private void dfs(TreeNode node, int sum, List<Integer> currentPath, List<List<Integer>> result) {
        if (node == null) return;

        currentPath.add(node.val);

        if (node.left == null && node.right == null && sum == node.val) {
            result.add(new ArrayList<>(currentPath));
        } else {
            dfs(node.left, sum - node.val, currentPath, result);
            dfs(node.right, sum - node.val, currentPath, result);
        }

        currentPath.remove(currentPath.size() - 1);
    }

    public static void main(String[] args) {
        LC0113_PathSumII solver = new LC0113_PathSumII();
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(4);
        root.right = new TreeNode(8);
        root.left.left = new TreeNode(11);
        root.left.left.left = new TreeNode(7);
        root.left.left.right = new TreeNode(2);
        List<List<Integer>> paths = solver.pathSum(root, 22);
        assert paths.size() == 1;
        System.out.println("LC0113_PathSumII passed all tests!");
    }
}
"""),
        ("LC0129_SumRootToLeafNumbers.java", "LC0129 Sum Root to Leaf Numbers", """/**
 * Problem: 129. Sum Root to Leaf Numbers
 * Difficulty: Medium
 * Category: Tree, Depth-First Search, Binary Tree
 *
 * Algorithm:
 * DFS: Carry running number cur = cur * 10 + node.val down each branch.
 * Sum running numbers at leaf nodes.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(H)
 */
public class LC0129_SumRootToLeafNumbers {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int currentSum) {
        if (node == null) return 0;
        currentSum = currentSum * 10 + node.val;

        if (node.left == null && node.right == null) {
            return currentSum;
        }

        return dfs(node.left, currentSum) + dfs(node.right, currentSum);
    }

    public static void main(String[] args) {
        LC0129_SumRootToLeafNumbers solver = new LC0129_SumRootToLeafNumbers();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        assert solver.sumNumbers(root) == 25; // 12 + 13
        System.out.println("LC0129_SumRootToLeafNumbers passed all tests!");
    }
}
"""),
        ("LC0199_BinaryTreeRightSideView.java", "LC0199 Binary Tree Right Side View", """import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Problem: 199. Binary Tree Right Side View
 * Difficulty: Medium
 * Category: Tree, Depth-First Search, Breadth-First Search, Binary Tree
 *
 * Algorithm:
 * BFS level-order traversal: for each depth level, append the last node's value
 * to the output list.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(D) where D is max diameter of tree
 */
public class LC0199_BinaryTreeRightSideView {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                if (i == levelSize - 1) {
                    result.add(node.val);
                }
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        LC0199_BinaryTreeRightSideView solver = new LC0199_BinaryTreeRightSideView();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.right = new TreeNode(5);
        root.right.right = new TreeNode(4);
        List<Integer> res = solver.rightSideView(root);
        assert res.size() == 3 && res.get(0) == 1 && res.get(1) == 3 && res.get(2) == 4;
        System.out.println("LC0199_BinaryTreeRightSideView passed all tests!");
    }
}
"""),
    ],

    # -------------------------------------------------------------
    # Day 6: Dynamic Programming & Greedy
    # -------------------------------------------------------------
    6: [
        ("LC0045_JumpGameII.java", "LC0045 Jump Game II", """/**
 * Problem: 45. Jump Game II
 * Difficulty: Medium
 * Category: Array, Dynamic Programming, Greedy
 *
 * Algorithm:
 * Greedy BFS-like intervals: Maintain the current jump's reach boundary (curEnd)
 * and the farthest reach achievable from any position visited so far (farthest).
 * When reaching curEnd, increment jump count and update curEnd = farthest.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0045_JumpGameII {

    public int jump(int[] nums) {
        if (nums == null || nums.length <= 1) return 0;

        int jumps = 0;
        int curEnd = 0;
        int farthest = 0;

        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (i == curEnd) {
                jumps++;
                curEnd = farthest;
                if (curEnd >= nums.length - 1) break;
            }
        }
        return jumps;
    }

    public static void main(String[] args) {
        LC0045_JumpGameII solver = new LC0045_JumpGameII();
        int[] nums = {2, 3, 1, 1, 4};
        assert solver.jump(nums) == 2;
        System.out.println("LC0045_JumpGameII passed all tests!");
    }
}
"""),
        ("LC0063_UniquePathsII.java", "LC0063 Unique Paths II", """/**
 * Problem: 63. Unique Paths II
 * Difficulty: Medium
 * Category: Array, Dynamic Programming, Matrix
 *
 * Algorithm:
 * 1D DP array: dp[j] represents number of paths to cell (i, j).
 * If obstacle at (i, j), dp[j] = 0. Otherwise dp[j] += dp[j - 1].
 *
 * Time Complexity: O(M * N)
 * Space Complexity: O(N)
 */
public class LC0063_UniquePathsII {

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid == null || obstacleGrid[0][0] == 1) return 0;

        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[] dp = new int[n];
        dp[0] = 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0;
                } else if (j > 0) {
                    dp[j] += dp[j - 1];
                }
            }
        }
        return dp[n - 1];
    }

    public static void main(String[] args) {
        LC0063_UniquePathsII solver = new LC0063_UniquePathsII();
        int[][] grid = {
            {0, 0, 0},
            {0, 1, 0},
            {0, 0, 0}
        };
        assert solver.uniquePathsWithObstacles(grid) == 2;
        System.out.println("LC0063_UniquePathsII passed all tests!");
    }
}
"""),
        ("LC0134_GasStation.java", "LC0134 Gas Station", """/**
 * Problem: 134. Gas Station
 * Difficulty: Medium
 * Category: Array, Greedy
 *
 * Algorithm:
 * Greedy: If total gas < total cost, complete circuit is impossible.
 * Otherwise, track current tank balance. If tank drops below 0 starting at index i,
 * no station between i and current can be the valid start, so reset start to curr + 1.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0134_GasStation {

    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalTank = 0;
        int curTank = 0;
        int startingStation = 0;

        for (int i = 0; i < gas.length; i++) {
            int net = gas[i] - cost[i];
            totalTank += net;
            curTank += net;

            if (curTank < 0) {
                startingStation = i + 1;
                curTank = 0;
            }
        }
        return totalTank >= 0 ? startingStation : -1;
    }

    public static void main(String[] args) {
        LC0134_GasStation solver = new LC0134_GasStation();
        int[] gas = {1, 2, 3, 4, 5};
        int[] cost = {3, 4, 5, 1, 2};
        assert solver.canCompleteCircuit(gas, cost) == 3;
        System.out.println("LC0134_GasStation passed all tests!");
    }
}
"""),
        ("LC0213_HouseRobberII.java", "LC0213 House Robber II", """/**
 * Problem: 213. House Robber II
 * Difficulty: Medium
 * Category: Array, Dynamic Programming
 *
 * Algorithm:
 * Since houses are in a circle (house 0 is adjacent to house n-1), solve two subproblems:
 * 1. Max rob from house 0 to n-2.
 * 2. Max rob from house 1 to n-1.
 * Return max of both.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
public class LC0213_HouseRobberII {

    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);

        return Math.max(robLinear(nums, 0, nums.length - 2),
                        robLinear(nums, 1, nums.length - 1));
    }

    private int robLinear(int[] nums, int start, int end) {
        int prev1 = 0;
        int prev2 = 0;

        for (int i = start; i <= end; i++) {
            int temp = prev1;
            prev1 = Math.max(prev2 + nums[i], prev1);
            prev2 = temp;
        }
        return prev1;
    }

    public static void main(String[] args) {
        LC0213_HouseRobberII solver = new LC0213_HouseRobberII();
        int[] nums = {2, 3, 2};
        assert solver.rob(nums) == 3;
        int[] nums2 = {1, 2, 3, 1};
        assert solver.rob(nums2) == 4;
        System.out.println("LC0213_HouseRobberII passed all tests!");
    }
}
"""),
        ("LC0279_PerfectSquares.java", "LC0279 Perfect Squares", """import java.util.Arrays;

/**
 * Problem: 279. Perfect Squares
 * Difficulty: Medium
 * Category: Math, Dynamic Programming, Breadth-First Search
 *
 * Algorithm:
 * DP: dp[i] = min(dp[i - j * j] + 1) for all j * j <= i.
 * Base case dp[0] = 0.
 *
 * Time Complexity: O(N * sqrt(N))
 * Space Complexity: O(N)
 */
public class LC0279_PerfectSquares {

    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j * j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        LC0279_PerfectSquares solver = new LC0279_PerfectSquares();
        assert solver.numSquares(12) == 3; // 4 + 4 + 4
        assert solver.numSquares(13) == 2; // 4 + 9
        System.out.println("LC0279_PerfectSquares passed all tests!");
    }
}
"""),
        ("LC0338_CountingBits.java", "LC0338 Counting Bits", """import java.util.Arrays;

/**
 * Problem: 338. Counting Bits
 * Difficulty: Easy
 * Category: Dynamic Programming, Bit Manipulation
 *
 * Algorithm:
 * DP transition: dp[i] = dp[i >> 1] + (i & 1).
 * The number of set bits in i equals set bits in (i / 2) plus lowest bit.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1) auxiliary (excluding output array)
 */
public class LC0338_CountingBits {

    public int[] countBits(int n) {
        int[] ans = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            ans[i] = ans[i >> 1] + (i & 1);
        }
        return ans;
    }

    public static void main(String[] args) {
        LC0338_CountingBits solver = new LC0338_CountingBits();
        int[] res = solver.countBits(5);
        assert Arrays.equals(res, new int[]{0, 1, 1, 2, 1, 2});
        System.out.println("LC0338_CountingBits passed all tests!");
    }
}
"""),
    ],

    # -------------------------------------------------------------
    # Day 7: Bit Manipulation, Backtracking & Heaps
    # -------------------------------------------------------------
    7: [
        ("LC0029_DivideTwoIntegers.java", "LC0029 Divide Two Integers", """/**
 * Problem: 29. Divide Two Integers
 * Difficulty: Medium
 * Category: Math, Bit Manipulation
 *
 * Algorithm:
 * Exponential search using bitwise left-shifts: double the divisor (divisor << 1)
 * until it exceeds dividend, subtract, and accumulate shifted quotient count.
 * Handle overflow cases (Integer.MIN_VALUE / -1 = Integer.MAX_VALUE).
 *
 * Time Complexity: O(log^2(N)) or O(32)
 * Space Complexity: O(1)
 */
public class LC0029_DivideTwoIntegers {

    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        boolean negative = (dividend < 0) ^ (divisor < 0);
        long dvd = Math.abs((long) dividend);
        long dvs = Math.abs((long) divisor);
        long quotient = 0;

        while (dvd >= dvs) {
            long temp = dvs;
            long multiple = 1;
            while (dvd >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }
            dvd -= temp;
            quotient += multiple;
        }

        return (int) (negative ? -quotient : quotient);
    }

    public static void main(String[] args) {
        LC0029_DivideTwoIntegers solver = new LC0029_DivideTwoIntegers();
        assert solver.divide(10, 3) == 3;
        assert solver.divide(7, -3) == -2;
        System.out.println("LC0029_DivideTwoIntegers passed all tests!");
    }
}
"""),
        ("LC0077_Combinations.java", "LC0077 Combinations", """import java.util.ArrayList;
import java.util.List;

/**
 * Problem: 77. Combinations
 * Difficulty: Medium
 * Category: Backtracking
 *
 * Algorithm:
 * Backtracking with pruning: at state (start, currentList), ensure remaining numbers
 * (n - start + 1) >= (k - currentList.size()).
 *
 * Time Complexity: O(C(n, k))
 * Space Complexity: O(k) recursion stack
 */
public class LC0077_Combinations {

    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(1, n, k, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int start, int n, int k, List<Integer> current, List<List<Integer>> result) {
        if (current.size() == k) {
            result.add(new ArrayList<>(current));
            return;
        }

        // Pruning: need (k - current.size()) more elements
        for (int i = start; i <= n - (k - current.size()) + 1; i++) {
            current.add(i);
            backtrack(i + 1, n, k, current, result);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        LC0077_Combinations solver = new LC0077_Combinations();
        List<List<Integer>> res = solver.combine(4, 2);
        assert res.size() == 6;
        System.out.println("LC0077_Combinations passed all tests!");
    }
}
"""),
        ("LC0090_SubsetsII.java", "LC0090 Subsets II", """import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Problem: 90. Subsets II
 * Difficulty: Medium
 * Category: Array, Backtracking, Bit Manipulation
 *
 * Algorithm:
 * Sort input array to group duplicate values together.
 * In backtracking loop, if nums[i] == nums[i - 1] and i > start, skip to prevent duplicates.
 *
 * Time Complexity: O(N * 2^N)
 * Space Complexity: O(N) recursion stack
 */
public class LC0090_SubsetsII {

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(0, nums, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int start, int[] nums, List<Integer> current, List<List<Integer>> result) {
        result.add(new ArrayList<>(current));

        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i - 1]) continue;
            current.add(nums[i]);
            backtrack(i + 1, nums, current, result);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        LC0090_SubsetsII solver = new LC0090_SubsetsII();
        int[] nums = {1, 2, 2};
        List<List<Integer>> res = solver.subsetsWithDup(nums);
        assert res.size() == 6; // [], [1], [1,2], [1,2,2], [2], [2,2]
        System.out.println("LC0090_SubsetsII passed all tests!");
    }
}
"""),
        ("LC0202_HappyNumber.java", "LC0202 Happy Number", """import java.util.HashSet;
import java.util.Set;

/**
 * Problem: 202. Happy Number
 * Difficulty: Easy
 * Category: Hash Table, Math, Two Pointers
 *
 * Algorithm:
 * Floyd's Cycle-Finding (slow and fast runner) or Hash set to detect cycle in digit square sum.
 *
 * Time Complexity: O(log N)
 * Space Complexity: O(1) with Floyd's algorithm
 */
public class LC0202_HappyNumber {

    public boolean isHappy(int n) {
        int slow = n;
        int fast = getNext(n);

        while (fast != 1 && slow != fast) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }
        return fast == 1;
    }

    private int getNext(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }

    public static void main(String[] args) {
        LC0202_HappyNumber solver = new LC0202_HappyNumber();
        assert solver.isHappy(19);
        assert !solver.isHappy(2);
        System.out.println("LC0202_HappyNumber passed all tests!");
    }
}
"""),
        ("LC0242_ValidAnagram.java", "LC0242 Valid Anagram", """/**
 * Problem: 242. Valid Anagram
 * Difficulty: Easy
 * Category: Hash Table, String, Sorting
 *
 * Algorithm:
 * Frequency array of size 26 for lowercase English letters.
 * Increment for s, decrement for t; all counts must end at zero.
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1) (fixed 26-element array)
 */
public class LC0242_ValidAnagram {

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        for (int c : count) {
            if (c != 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        LC0242_ValidAnagram solver = new LC0242_ValidAnagram();
        assert solver.isAnagram("anagram", "nagaram");
        assert !solver.isAnagram("rat", "car");
        System.out.println("LC0242_ValidAnagram passed all tests!");
    }
}
"""),
        ("LC0295_FindMedianFromDataStream.java", "LC0295 Find Median from Data Stream", """import java.util.Collections;
import java.util.PriorityQueue;

/**
 * Problem: 295. Find Median from Data Stream
 * Difficulty: Hard
 * Category: Two Heaps, Design, Data Stream
 *
 * Algorithm:
 * Two Heaps:
 * - maxHeap stores lower half of numbers.
 * - minHeap stores upper half of numbers.
 * Balance heaps so maxHeap has equal or 1 more element than minHeap.
 * Median is either maxHeap.peek() or average of peek from both heaps.
 *
 * Time Complexity: addNum: O(log N), findMedian: O(1)
 * Space Complexity: O(N)
 */
public class LC0295_FindMedianFromDataStream {

    private PriorityQueue<Integer> maxHeap;
    private PriorityQueue<Integer> minHeap;

    public LC0295_FindMedianFromDataStream() {
        maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        minHeap = new PriorityQueue<>();
    }

    public void addNum(int num) {
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.offer(num);
        } else {
            minHeap.offer(num);
        }

        // Rebalance
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.offer(maxHeap.poll());
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.offer(minHeap.poll());
        }
    }

    public double findMedian() {
        if (maxHeap.size() > minHeap.size()) {
            return (double) maxHeap.peek();
        } else {
            return (maxHeap.peek() + minHeap.peek()) / 2.0;
        }
    }

    public static void main(String[] args) {
        LC0295_FindMedianFromDataStream finder = new LC0295_FindMedianFromDataStream();
        finder.addNum(1);
        finder.addNum(2);
        assert finder.findMedian() == 1.5;
        finder.addNum(3);
        assert finder.findMedian() == 2.0;
        System.out.println("LC0295_FindMedianFromDataStream passed all tests!");
    }
}
"""),
    ]
}

def generate_all_solutions():
    print("[*] Generating all 42 Java solutions into staging/day1 .. staging/day7...")
    for day, probrecs in PROBLEMS.items():
        day_dir = os.path.join(ROOT, "staging", f"day{day}")
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
            f"# =================================================================",
            f"# Day {day} LeetCode Submissions (6 Sequential Java Contributions)",
            f"# Compatible with Termux (Android) and standard Linux/macOS bash",
            f"# =================================================================",
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
                f'    sleep 2',
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
        ])

        # Write with LF endings
        with open(sh_path, "wb") as f:
            f.write("\n".join(lines).encode("utf-8"))
        print(f"  -> Generated {os.path.basename(sh_path)}")

def generate_auto_detector_scripts():
    print("[*] Generating auto-detector and smart master runner scripts...")
    
    # 1. auto_submit.sh - Pure Bash zero-friction auto detector & runner
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
    PENDING_FILES=()

    for f in "$DAY_DIR"/LC*.java; do
        [ -e "$f" ] || continue
        TOTAL_DAY=$((TOTAL_DAY + 1))
        BNAME=$(basename "$f")
        if [ -f "./$BNAME" ]; then
            DONE_DAY=$((DONE_DAY + 1))
        else
            PENDING_FILES+=("$BNAME")
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

# Handle status check
if [ "$1" == "status" ] || [ "$1" == "--status" ] || [ "$1" == "-s" ]; then
    echo "[*] Status check complete."
    if [ "$ALL_DONE" = true ]; then
        echo "🎉 All 42 problems across Days 1-7 are fully submitted!"
    else
        echo "⚡ Next batch queued: DAY $NEXT_DAY. Run './auto_submit.sh' to execute."
    fi
    exit 0
fi

# If user provided a specific day parameter, respect it
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
chmod +x "day${TARGET_DAY}.sh"
bash "day${TARGET_DAY}.sh"
"""

    with open(auto_sh_path, "wb") as f:
        f.write(auto_sh_content.encode("utf-8"))
    print(f"  -> Generated {os.path.basename(auto_sh_path)}")

    # 2. run_day.sh - Master interactive or auto runner
    run_sh_path = os.path.join(ROOT, "run_day.sh")
    run_sh_content = """#!/bin/bash
# Master Daily Runner with Auto-Detector for Termux (Android) / Linux
# Usage:
#   ./run_day.sh         (AUTO MODE: auto-detects what is uploaded and runs next batch)
#   ./run_day.sh status  (CHECKS STATUS: shows upload detector table)
#   ./run_day.sh 1       (RUNS Day 1 explicitly)
#   ./run_day.sh 2       (RUNS Day 2 explicitly)
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

chmod +x auto_submit.sh

if [ "$1" == "status" ] || [ "$1" == "--status" ]; then
    bash auto_submit.sh --status
elif [ -n "$1" ]; then
    bash auto_submit.sh "$1"
else
    bash auto_submit.sh auto
fi
"""
    with open(run_sh_path, "wb") as f:
        f.write(run_sh_content.encode("utf-8"))
    print(f"  -> Updated {os.path.basename(run_sh_path)}")

    # 3. scripts/detector.py - Rich python detector
    py_det_path = os.path.join(ROOT, "scripts", "detector.py")
    py_det_content = '''"""
detector.py
Analyzes the LeetCode repository to detect which problems have been submitted,
which staging problems are pending, and optionally runs the next daily batch.
"""

import os
import sys
import subprocess
import re

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
    if sys.platform == "win32":
        # In windows shell, execute via bash or python equivalent
        bash_path = "bash"
        cmd = [bash_path, day_script]
        print(f"[*] Executing Day {day_num} via bash...")
        subprocess.run(cmd, check=True)
    else:
        subprocess.run(["bash", day_script], check=True)

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
    print("\\n[+] Build suite completed successfully.")
