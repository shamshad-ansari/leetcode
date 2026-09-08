class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        ans = 0
        while True:
            for char in "balloon":
                count[char] -= 1
                if count[char] < 0:
                    return ans
            ans += 1