class Solution:
    def findGCD(self, nums: list[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        for i in range(mn,0,-1):
            if mn % i == 0 and mx % i == 0:
                return i