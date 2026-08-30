class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxNum = max(nums)
        minNum = min(nums)
        n = len(nums)
        count = 0
        for i, num in enumerate(nums):
                    n = len(nums)

        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))

        left = min(minIndex, maxIndex)
        right = max(minIndex, maxIndex)

        # Option 1: Remove both from the left
        bothLeft = right + 1

        # Option 2: Remove both from the right
        bothRight = n - left

        # Option 3: Remove one from each side
        bothSides = (left + 1) + (n - right)

        return min(bothLeft, bothRight, bothSides)