class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        count = Counter(nums)
        for k,v in count.items():
            if v % 2 == 1:
                return False
        return True