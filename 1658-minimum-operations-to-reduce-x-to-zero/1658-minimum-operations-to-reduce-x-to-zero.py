# Not my code but improved version based on the same logic. Basically we don't need to check both direction only one way does the job
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        postfix = {}
        best = float('inf')

        post = 0
        for i in range(len(nums) - 1, -1, -1):
            post += nums[i]
            postfix[post] = len(nums) - i

            if post == x:
                best = min(best, len(nums) - i)

        pre = 0
        for i, num in enumerate(nums, start=1):
            pre += num

            if pre == x:
                best = min(best, i)

            complement = x - pre

            if complement in postfix:
                operations = i + postfix[complement]

                # prefix and suffix cannot overlap
                if operations <= len(nums):
                    best = min(best, operations)

        return best if best != float('inf') else -1