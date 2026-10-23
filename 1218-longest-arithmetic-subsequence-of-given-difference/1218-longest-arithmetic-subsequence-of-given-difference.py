class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        seen = defaultdict(int)
        best = 1
        for i, num in enumerate(arr):
            seen[num] = seen[num-difference] + 1
            best = max(best, seen[num])
            
        return best