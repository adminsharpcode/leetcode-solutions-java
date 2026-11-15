"""
append_week2_days3_7.py
Generates Days 3 through 7 of the 42-problem mobile suite.
"""

import os

ROOT = r"E:\LeetCode-Solutions-Java"

PROBLEMS = {
    # -------------------------------------------------------------
    # Day 3: Strings & Parsing / Math
    # -------------------------------------------------------------
    3: [
        ("LC0006_ZigzagConversion.java", """import java.util.ArrayList;
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
        ("LC0012_IntegerToRoman.java", """/**
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
        ("LC0013_RomanToInteger.java", """import java.util.HashMap;
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
        ("LC0043_MultiplyStrings.java", """/**
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
        ("LC0058_LengthOfLastWord.java", """/**
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
        ("LC0125_ValidPalindrome.java", """/**
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
        ("LC0057_InsertInterval.java", """import java.util.*;

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
        ("LC0081_SearchInRotatedSortedArrayII.java", """/**
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

            // Handle duplicates ambiguity
            if (nums[left] == nums[mid] && nums[mid] == nums[right]) {
                left++;
                right--;
            } else if (nums[left] <= nums[mid]) {
                // Left half is sorted
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // Right half is sorted
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
        ("LC0162_FindPeakElement.java", """/**
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
        ("LC0278_FirstBadVersion.java", """/**
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

    // Mock API
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
        ("LC0704_BinarySearch.java", """/**
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
        ("LC0875_KokoEatingBananas.java", """/**
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
            hours += (p + speed - 1) / speed; // ceil division
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
    ]
}

def generate():
    for day, probrecs in PROBLEMS.items():
        target_dir = os.path.join(ROOT, "staging", f"day{day}")
        os.makedirs(target_dir, exist_ok=True)
        for filename, code in probrecs:
            filepath = os.path.join(target_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(code.strip() + "\n")
            print(f"Generated day{day}/{filename}")

if __name__ == "__main__":
    generate()
