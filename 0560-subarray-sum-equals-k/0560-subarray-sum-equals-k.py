class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = {}
        prefixSum[0] = 1
        s = 0
        count = 0

        for i in range(n):
            s += nums[i]
            diff = s - k

            if diff in prefixSum:
                count += prefixSum[diff]

            prefixSum[s] = prefixSum.get(s,0) + 1

        return count      