class Solution:
    def findGCD(self, nums: list[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        while mn > 0:
            rem = mx % mn
            if rem == 0:
                return mn
            mx = mn
            mn = rem
        return mn