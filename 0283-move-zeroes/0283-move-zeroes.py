class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)      
        result = []

        for i in range(n):
            if nums[i] != 0:
                result.append(nums[i])

        for i in range(len(result)):
            nums[i] = result[i]
        
        for j in range(i+1,n):
            nums[j] = 0