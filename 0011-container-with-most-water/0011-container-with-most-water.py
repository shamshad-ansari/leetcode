class Solution:
    def maxArea(self, height: list[int]) -> int:
        best = 0
        l = 0
        r = len(height) - 1
        while l < r:
            w = r - l
            lh = height[l]
            rh = height[r]
            if rh >= lh:
                l += 1
            else:
                r -= 1
            h = min(lh, rh)
            area = w * h
            best = max(best, area)
        return best
        