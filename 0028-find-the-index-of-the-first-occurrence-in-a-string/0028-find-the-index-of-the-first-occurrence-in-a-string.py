class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        start = 0
        l , r = 0, 0
        while l < m and r < n:
            if needle[r] == haystack[l]:
                l += 1
                r += 1
                if r == n:
                    return start
            else:
                start += 1
                l = start
                r = 0
        return -1