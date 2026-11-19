/**
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
