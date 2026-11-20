/**
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
