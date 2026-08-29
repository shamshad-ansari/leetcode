class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stk = []
        result = [-1] * n
        for i in range(2 * n, -1, -1):
            idx = i % n 
            while stk and stk[-1] <= nums[idx]:
                stk.pop()
            if i < n and stk:
                result[idx] = stk[-1]
            stk.append(nums[idx])
        return result