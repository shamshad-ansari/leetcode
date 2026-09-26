# Needed help to figure out the operations greater than len condition
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        prefix ={}
        postfix = {}
        best = float('inf')

        pre = 0
        for i, num in enumerate(nums, start = 1):
            pre += num
            if pre == x:
                best = min(best, i)
            prefix[pre] = i
        
        post = 0
        for i in range(len(nums)-1 , -1, -1):
            num = nums[i]
            post += num
            if post == x:
                best = min(best, len(nums)-i)
            postfix[post] = len(nums) - i

        pre = 0
        for i, num in enumerate(nums, start = 1):
            pre += num
            if pre > x:
                break
            complement = x - pre
            if complement in postfix:
                operations = i + postfix[complement]

                if operations <= len(nums):
                    best = min(best, operations)
        
        post = 0
        for i in range(len(nums)-1 , -1, -1):
            num = nums[i]
            post += num
            if post > x:
                break
            complement = x - post
            if complement in prefix:
                operations = (len(nums) - i) + prefix[complement]

                if operations <= len(nums):
                    best = min(best, operations)

        return best if best != float('inf') else -1