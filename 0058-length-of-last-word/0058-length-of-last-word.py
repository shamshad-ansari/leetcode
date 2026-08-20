class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        s = s.strip()
        i = 0
        while i < len(s):
            if s[i] != " ":
                length += 1
            
            else:
                length = 0
            i += 1

        return length  
        
            
            
            
        

        

            


                

        


        