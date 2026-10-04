class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix = {0: 1}
        cum = 0
        ans = 0
        for num in nums:
            cum += num
            diff = cum - goal
            if diff in prefix:
                ans += prefix[diff]
            prefix[cum] = prefix.get(cum, 0) + 1
        
        return ans