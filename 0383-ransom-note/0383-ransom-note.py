class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for letter in ransomNote:
            count[letter] -= 1
            if count[letter] < 0:
                return False
        return True