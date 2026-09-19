class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # We can use a flag to break outer loop as well
        result = []
        stop = False
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i>=len(strs[j]):
                    stop = True
                    break
                if strs[0][i] != strs[j][i]:
                    stop = True
                    break
            if stop:
                break
            result.append(strs[0][i])
        return ''.join(result)    