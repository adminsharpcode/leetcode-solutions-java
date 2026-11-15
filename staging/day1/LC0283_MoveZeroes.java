import java.util.Arrays;

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
