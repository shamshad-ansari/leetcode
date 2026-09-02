class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def solve(row,col):
            if row >= len(triangle) or col >= len(triangle[-1]):
                return 0
            
            left= triangle[row][col] + solve(row+1,col)
            right = triangle[row][col] + solve(row+1,col+1)

            return min(left, right)

        return solve(0,0)        