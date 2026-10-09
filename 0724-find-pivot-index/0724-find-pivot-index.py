class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        sumLeft = [0] * n
        sumRight = [0] * n
        left, right = 0, 0

        for i, num in enumerate(nums):
            sumLeft[i] = left
            left += num
        for i in range(n-1, -1, -1):
            sumRight[i] = right
            right += nums[i]
        
        for i in range(n):
            if sumLeft[i] == sumRight[i]:
                return i
        return -1