class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        y = x
        while x > 0:
            last = x % 10
            rev = rev * 10 + last
            x = x//10
        return y == rev