class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST = {}
        mapTS = {}

        for i in range(len(s)):
            charS = s[i]
            charT = t[i]

            if not charS in mapST:
                mapST[charS] = charT
            elif mapST[charS] != charT:
                return False
            
            if charT not in mapTS:
                mapTS[charT] = charS
            elif mapTS[charT] != charS:
                return False
        
        return True