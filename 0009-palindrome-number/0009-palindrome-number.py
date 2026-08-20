class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        ans = False
        y = x
        reversed = 0
        while x:
            r = x % 10
            reversed = reversed * 10 + r
            x = x // 10
        
        return y == reversed

        