class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [''] * numRows
        r = 0
        direction = 1
        
        for char in s:
            rows[r] += char

            if r == 0:
                direction = 1
            elif r == numRows-1:
                direction = -1
            
            r += direction
            

        return ''.join(rows)