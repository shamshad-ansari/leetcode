class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache   
        def solve(i, op):
            if op < 0:
                return False
            if i >= len(s):
                return op == 0
            if s[i] == "(":
                op += 1
                if solve(i+1, op):
                    return True
            elif s[i] == ")":
                op -= 1
                if solve(i+1, op):
                    return True
            else:
                op += 1
                if solve(i+1, op):
                    return True
                op -= 1
                op -= 1
                if solve(i+1, op):
                    return True
                op += 1
                if solve(i+1, op):
                    return True
            return False

        return solve(0, 0)