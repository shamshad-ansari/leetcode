from collections import deque
import copy

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        visited = set()
        level = 0

        def toString(arr):
            s = []
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    s.append(str(arr[i][j]))
            return ''.join(s)

        def indexOf(arr):
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    if arr[i][j] == 0:
                        return (i, j)

        s = toString(board)
        target = '123450'
        visited.add(s)
        q = deque([board])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            n = len(q)
            for _ in range(n):
                arr = q.popleft()
                s = toString(arr)

                if s == target:
                    return level

                r, c = indexOf(arr)

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nr > 1 or nc < 0 or nc > 2:
                        continue

                    new_arr = copy.deepcopy(arr)

                    new_arr[nr][nc], new_arr[r][c] = new_arr[r][c], new_arr[nr][nc]

                    s = toString(new_arr)

                    if s not in visited:
                        q.append(new_arr)
                        
                        visited.add(s)

            level += 1

        return -1