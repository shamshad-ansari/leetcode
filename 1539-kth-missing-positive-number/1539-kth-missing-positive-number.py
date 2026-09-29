class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        s = set(arr)
        count = 0

        for i in range(1, max(arr) + k + 1):
            if i not in s:
                count += 1
                if count == k:
                    return i