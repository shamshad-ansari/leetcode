from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        if 1 in freq:
            ones = freq[1]
            if ones % 2 == 0:
                ones = ones - 1
            ans = max(ones, ans)
        
        for num in freq:
            if num == 1 or freq[num] == 1:
                continue

            x = num
            letter = 0

            while freq[x] >= 2:
                letter += 2
                x = x**2
            
            if x in freq:
                letter += 1
            else:
                letter -= 1

            ans = max(ans, letter)
            
        return ans