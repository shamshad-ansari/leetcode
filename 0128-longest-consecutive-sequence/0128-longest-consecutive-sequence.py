class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        s = set(nums)
        visited = set()
        ans = 1

        for num in nums:
            if num - 1 in s or num in visited:
                continue
            else:
                count = 1
                while num + 1 in s:
                    count += 1
                    ans = max(ans, count)
                    visited.add(num)
                    num = num + 1
        return ans