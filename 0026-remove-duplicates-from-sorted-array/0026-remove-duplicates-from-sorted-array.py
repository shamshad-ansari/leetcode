class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        visited = set()
        visited.add(nums[0])
        i = 0 
        n = len(nums)
        for j in range(n):
            if nums[j] not in visited:
                visited.add(nums[j])
                i += 1
                nums[i] = nums[j]
        return i + 1