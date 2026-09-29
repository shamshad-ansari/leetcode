class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        nums = [False] * 2001
        count = 0 
        for num in arr:
            nums[num] = True
        
        for i in range(1, len(nums)): 
            if nums[i] == False: 
                count += 1
                print(count)

                if k == count:
                    return i