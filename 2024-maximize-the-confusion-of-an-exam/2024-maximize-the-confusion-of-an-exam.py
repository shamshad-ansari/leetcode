class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        '''
        # Approach
        I keep the max frequency of a contigous block and do length - maxfFreq < k becuase a valid window is always
        formed by maxFreq + k = length and after rearraning it should act as the condition for my window
        '''

        maxFreq = 0
        best = 0
        count = {}
        l = 0
        for r, char in enumerate(answerKey):
            count[char] = count.get(char, 0) + 1
            maxFreq = max(maxFreq, count[char])

            while (r - l + 1) - maxFreq > k:
                tD = answerKey[l]
                count[tD] -= 1
                if count[tD] == 0:
                    count.pop(tD)
                l += 1
            
            best = max(best, r-l+1)

        return best