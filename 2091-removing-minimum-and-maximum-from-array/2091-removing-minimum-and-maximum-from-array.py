class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxNum = max(nums)
        minNum = min(nums)
        n = len(nums)
        count = 0
        for i, num in enumerate(nums):
            count += 1
            if num == maxNum:
                beyondMax = n - i
                beforeMax = i + 1
                bestMax = min(beyondMax, beforeMax)
                print(bestMax)
            if num == minNum:
                beyondMin = n - i
                beforeMin = i + 1
                bestMin = min(beforeMin, beyondMin)
                print(bestMin)
        answer = min(
            max(beforeMin, beforeMax),
            max(beyondMin, beyondMax),
            beforeMin + beyondMax,
            beforeMax + beyondMin
        )
        return answer

'''
# both from left
max(beforeMin, beforeMax)

# both from right
max(beyondMin, beyondMax)

# min from left, max from right
beforeMin + beyondMax

# max from left, min from right
beforeMax + beyondMin
'''