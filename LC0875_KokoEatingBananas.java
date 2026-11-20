/**
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
