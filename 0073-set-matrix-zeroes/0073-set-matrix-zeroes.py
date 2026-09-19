class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zeros = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.add((i,j))

        for i in range(m):
            for j in range(n):
                if (i,j) in zeros:
                    matrix[i] = [0] * n
                    for r in range(m):
                        matrix[r][j] = 0
        