class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        current = []

        def solve(start, currSum):
            if currSum == target:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if currSum + candidates[i] > target:
                    break

                current.append(candidates[i])
                solve(i + 1, currSum + candidates[i])
                current.pop()

        solve(0, 0)
        return result