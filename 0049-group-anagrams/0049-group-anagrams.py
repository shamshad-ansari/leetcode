class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        
        for word in strs:
            freq = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                freq[idx] += 1
            hashMap[tuple(freq)].append(word)
        return list(hashMap.values())