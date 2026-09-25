class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        items = {}
        l = 0
        ans = 0
        for fruit in fruits:
            items[fruit] = items.get(fruit, 0) + 1

            while len(items) > 2:
                lf = fruits[l]
                items[lf] = items.get(lf, 0) - 1
                if items[lf] <= 0:
                    items.pop(lf)
                l += 1

            ans = max(ans, sum(items.values()))

        return ans   