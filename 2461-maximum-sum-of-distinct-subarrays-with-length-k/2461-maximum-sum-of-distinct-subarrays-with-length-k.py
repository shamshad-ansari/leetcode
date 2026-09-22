class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        visited = set()
        cumSum = 0
        l = 0
        best = 0

        for r, num in enumerate(nums):
            while num in visited:
                visited.remove(nums[l])
                cumSum -= nums[l]
                l += 1

            visited.add(num)
            cumSum += num

            while r - l + 1 > k:
                visited.remove(nums[l])
                cumSum -= nums[l]
                l += 1

            if r - l + 1 == k:
                best = max(best, cumSum)

        return best
        