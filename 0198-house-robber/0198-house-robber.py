class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = {}
        def solve(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            take = nums[i] + solve(i+2)
            skip = solve(i+1)
            dp[i] = max(take, skip)
            return dp[i]
        return solve(0) 