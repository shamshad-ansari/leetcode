class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]: 
        n = len(heights)
        ans = [0] * n
        stack = []
        for i in range(n-1,-1,-1):
            count = 0
            while stack and stack[-1] < heights[i]:
                count += 1
                stack.pop()
            if stack:
                count += 1
            stack.append(heights[i])
            ans[i] = count
        return ans