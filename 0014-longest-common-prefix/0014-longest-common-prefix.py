class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        i = 0
        strs.sort()

        while i < len(strs[0]) and i < len(strs[-1]):
            if strs[0][i] != strs[-1][i]:
                return prefix
            
            prefix += strs[0][i] 
            i += 1
        
        return prefix
        
        