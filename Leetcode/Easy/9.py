class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original_x = x
        reverse_x = 0
        while x != 0:
            digit = x % 10
            reverse_x = reverse_x * 10 + digit
            x //= 10

        return original_x == reverse_x