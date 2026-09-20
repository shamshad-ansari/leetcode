class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        m = len(str1)
        n = len(str2)
        while n > 0:
            rem = m % n
            if rem == 0:
                return str1[:n]
            m = n
            n = rem
        return str1[:n]