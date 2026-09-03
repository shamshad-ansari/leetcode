class Solution:
    def plusOne(self, arr: List[int]) -> List[int]:
        digit = 0
        for num in arr:
            digit = digit * 10 + num
        result = []
        digit += 1
        while digit > 0:
            rm = digit % 10
            result.append(rm)
            digit = digit//10
        return result[::-1]            