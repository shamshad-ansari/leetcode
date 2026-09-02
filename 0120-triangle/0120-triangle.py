class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def solve(row,col):
            if row >= len(triangle) or col >= len(triangle[-1]):
                return 0
            
            if (row,col) in memo:
                return memo[(row,col)]
            
            left = triangle[row][col] + solve(row+1,col)
            right = triangle[row][col] + solve(row+1,col+1)

            memo[(row,col)] = min(left, right)
            return memo[(row,col)]

        return solve(0,0)