class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        result = []
        result.append([rStart,cStart])
        step = 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        dr = 0

        while len(result) < rows * cols:
            if dr == 0 or dr == 2:
                step += 1
            
            for i in range(step):
                rStart += dirs[dr][0]
                cStart += dirs[dr][1]
                if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                    result.append([rStart,cStart])
            
            dr = (dr + 1) % len(dirs)
        
        return result