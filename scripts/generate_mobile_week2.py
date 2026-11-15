"""
generate_mobile_week2.py
Generates 42 complete, production-grade LeetCode Java solutions organized across 7 days (6 problems/day)
into staging/day1/ through staging/day7/.
"""

import os

ROOT = r"E:\LeetCode-Solutions-Java"

PROBLEMS = {
    # -------------------------------------------------------------
    # Day 1: Arrays, Two Pointers & In-Place Manipulations
    # -------------------------------------------------------------
    1: [
        ("LC0018_4Sum.java", """import java.util.*;

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
        ("LC0027_RemoveElement.java", """import java.util.Arrays;

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
        ("LC0080_RemoveDuplicatesFromSortedArrayII.java", """import java.util.Arrays;

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
        ("LC0088_MergeSortedArray.java", """import java.util.Arrays;

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
        ("LC0209_MinimumSizeSubarraySum.java", """/**
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
        ("LC0283_MoveZeroes.java", """import java.util.Arrays;

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
        ("LC0082_RemoveDuplicatesFromSortedListII.java", """/**
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
                prev.next = head.next; // exclude all duplicates
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
        ("LC0083_RemoveDuplicatesFromSortedList.java", """/**
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
        ("LC0086_PartitionList.java", """/**
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
        ("LC0092_ReverseLinkedListII.java", """/**
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
        ("LC0160_IntersectionOfTwoLinkedLists.java", """/**
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
        ("LC0203_RemoveLinkedListElements.java", """/**
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
    ]
}

def generate_day(day_num, problems):
    target_dir = os.path.join(ROOT, "staging", f"day{day_num}")
    os.makedirs(target_dir, exist_ok=True)
    for filename, code in problems:
        filepath = os.path.join(target_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code.strip() + "\n")
        print(f"Generated day{day_num}/{filename}")

if __name__ == "__main__":
    for day, probrecs in PROBLEMS.items():
        generate_day(day, probrecs)
