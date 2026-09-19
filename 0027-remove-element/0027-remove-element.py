class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Some optimization but still O(n^2) in the worst case
        # consider this example nums = [1, 1, 1, 1, 2, 2, 2, 2], val = 1
        for i in range(len(nums)):
            if nums[i] != val:
                print(nums[i])
            swap = False
            for j in range(i, len(nums)):
                if nums[j] != val:
                    nums[j], nums[i] = nums[i], nums[j]
                    swap = True
                    break
            if not swap:
                break
        
        ans = 0
        while ans < len(nums) and nums[ans] != val:
            ans += 1
        
        return ans