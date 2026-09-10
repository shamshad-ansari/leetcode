class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def solve(i, target):
            if target == 0:
                return 0
            
            if target < 0 or i >= len(coins):
                return float('inf')

            
            take = 1 + solve(i, target - coins[i])
            skip = solve(i+1, target)

            return min(take, skip)
        
        result = solve(0, amount)
        return - 1 if result == float('inf') else result