class Solution:
    def rob(self, nums: list[int]) -> int:
        # def solve(i):
        #     if i >= len(nums):
        #         return 0
        #     if i in dp:
        #         return dp[i]
        #     take = nums[i] + solve(i+2)
        #     skip = solve(i+1)
        #     dp[i] = max(take, skip)
        #     return dp[i]
        # return solve(0) 
        if len(nums) < 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            take = nums[i] + dp[i-2]
            skip = dp[i-1]
            dp[i] = max(take, skip)

        return max(dp)

