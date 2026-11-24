import java.util.ArrayList;
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
