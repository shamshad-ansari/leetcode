class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(r, c):
            # Using != O because we want to use the board as the visisted set
            # If it is not 0 that means its either X which we can skip of S which is visited
            if r >=m or r<0 or c >=n or c<0 or board[r][c] != "O":
                return
            
            board[r][c] = "S"
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(m):
            dfs(r,0)
            dfs(r,n-1)
        
        for c in range(n):
            dfs(0,c)
            dfs(m-1,c)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"