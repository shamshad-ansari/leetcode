class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        s = set(arr)
        i = 1
        count = 0
        while True:
            if i not in s:
                count += 1
                if count == k:
                    return i
            i += 1