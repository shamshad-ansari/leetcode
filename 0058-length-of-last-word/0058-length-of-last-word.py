class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list = s.strip().split()
        return len(list[-1])


        