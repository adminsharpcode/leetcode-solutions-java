import java.util.HashSet;
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
