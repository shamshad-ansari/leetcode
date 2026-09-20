class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        result = []
        count0 = Counter(words[0])
        if len(words) == 1:
            for k,v in count0.items():
                for _ in range(v):
                    result.append(k)
            return result

        count1 = Counter(words[1])
        common = {}
        for k in count0:
            if k in count1:
                common[k] = min(count0[k], count1[k])
            
        for i in range(2, len(words)):
            toDelete = []
            word = words[i]
            charCount = Counter(word)
            for k in common:
                if k not in charCount:
                    toDelete.append(k)
                else:
                    common[k] = min(common[k],charCount[k])
            for each in toDelete:
                del common[each]
            
        for k,v in common.items():
            for _ in range(v):
                result.append(k)
        return result