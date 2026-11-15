import java.util.Arrays;

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
