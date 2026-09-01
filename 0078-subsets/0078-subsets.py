class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def solve(i):
            if i == len(nums):
                result.append(current.copy())
                return
            
            current.append(nums[i])
            solve(i+1)

            current.pop()
            solve(i+1)
        
        solve(0)
        return result