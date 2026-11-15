/**
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
