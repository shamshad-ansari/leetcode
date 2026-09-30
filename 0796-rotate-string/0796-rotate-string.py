class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s) or Counter(s)!= Counter(goal):
            return False
        
        new = s
        for i in range(len(s)):
            new = new[1:] + new[:1]
            if new == goal:
                return True
        return False