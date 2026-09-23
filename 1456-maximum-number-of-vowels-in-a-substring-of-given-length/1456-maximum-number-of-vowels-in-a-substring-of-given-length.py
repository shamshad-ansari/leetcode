class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        volCount = 0
        best = 0
        l = 0
        for r, char in enumerate(s):
            if char in 'aeiou':
                volCount += 1

            while r - l + 1 > k:
                c = s[l]
                if c in 'aeiou':
                    volCount -= 1
                l += 1
            
            best = max(best, volCount)

        return best       