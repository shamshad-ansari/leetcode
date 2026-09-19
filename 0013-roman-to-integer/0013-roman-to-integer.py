class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {   
             'I' : 1,
             'V' : 5,
             'X' : 10,
             'L' : 50,
             'C' : 100,
             'D' : 500,
             'M' : 1000
             }
        n = len(s)
        if n == 1:
            return mp[s[0]]
        num = 0
        i = n -1
        while i >= 0:
            char = s[i]
            num += mp[char]
            # We only take prev if i > 0 so we don't get index error
            if i > 0:
                prev = s[i-1]
                if (char == 'V' or char == 'X') and prev == 'I':
                    num -= 1
                    i -= 1
                elif (char == 'L' or char == 'C') and prev == 'X':
                    num -= 10
                    i-= 1
                elif (char == 'D' or char == 'M') and prev == 'C':
                    num -= 100
                    i-=1
            i-=1
        return num