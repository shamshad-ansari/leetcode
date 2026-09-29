class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for char in s:
            if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
                result.append(char.lower())
        print(result)
        result = ''.join(result)

        def isPalindrome(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        return isPalindrome(result)
        