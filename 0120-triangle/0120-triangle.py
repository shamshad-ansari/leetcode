class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * len(row) for row in triangle]
        dp[n-1] = triangle[n-1][:]

        for row in range(n-2,-1,-1):
            for col in range(len(triangle[row])):
                left = dp[row + 1][col]
                right = dp[row+1][col+1]
                dp[row][col] = triangle[row][col] + min(left, right)
        return dp[0][0]