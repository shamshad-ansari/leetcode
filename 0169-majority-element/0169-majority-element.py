class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        counter = Counter(nums)
        for key, value in counter.items():
            if value >= n/2:
                return key