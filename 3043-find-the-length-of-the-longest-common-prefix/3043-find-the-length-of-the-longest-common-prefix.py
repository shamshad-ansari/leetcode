class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        set1 = set()
        set2 = set()
        ans = 0
        for num in arr2:
            set2.add(num)
            while num > 0:
                set2.add(num//10)
                num = num//10
        for num in arr1:
            set1.add(num)
            while num > 0:
                set1.add(num//10)
                num = num//10
        for num in set1:
            if num in set2:
                if num > 0:
                    n = int(math.log10(num)) + 1
                    ans = max(ans, n)
        
        return ans
