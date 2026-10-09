class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cum = 0
        best = float('-inf')

        for num in nums:
            cum += num
            if num > cum:
                cum = num
            best = max(best, cum)
            
        return best