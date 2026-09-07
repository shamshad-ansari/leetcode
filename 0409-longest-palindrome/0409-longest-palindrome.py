class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        hasOdd = False
        for key,val in count.items():
            if val % 2 == 1:
                hasOdd = True
            ans += (val // 2) * 2

        return ans+1 if hasOdd else ans