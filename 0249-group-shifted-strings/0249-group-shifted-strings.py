from collections import defaultdict

class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        result = defaultdict(list)

        def getKey(word):
            k = []
            i = 0
            n = len(word)

            while i < n - 1:
                charA = word[i]
                charB = word[i + 1]

                diff = (ord(charB) - ord(charA)) % 26
                k.append(diff)
                i += 1

            # We just return empty tuple for single length words
            return tuple(k)

        for word in strings:
            key = getKey(word)
            result[key].append(word)

        return list(result.values())