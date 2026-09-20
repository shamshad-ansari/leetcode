class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        n = len(s)
        mx = n
        mn = 0
        result = [0] * (n+1)
        for i, char in enumerate(s):
            if char == 'D':
                result[i] = mx
                mx -= 1
            elif char == "I":
                result[i] = mn
                mn += 1
        if s[-1] == 'D':
            result[-1] = mx
        else:
            result[-1] = mn  
        return result