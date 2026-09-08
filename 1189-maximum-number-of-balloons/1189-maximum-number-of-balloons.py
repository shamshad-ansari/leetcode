class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        need = Counter("balloon")

        ans = float("inf")

        for char, needed_amount in need.items():
            available = counts[char]
            possible = available // needed_amount
            ans = min(ans, possible)

        return ans