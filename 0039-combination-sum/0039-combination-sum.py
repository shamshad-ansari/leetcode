class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
            result = []
            current = []

            def solve(i, curr):
                if curr == target:
                    result.append(current.copy())
                    return
                
                # Check target first because reaching the end of candidates doesn't
                # invalidate a combination that has already reached the target.
                # Only stop for an invalid path after checking if we found an answer.
                if curr > target or i >= len(candidates):
                    return

                # TAKE candidates[i]
                current.append(candidates[i])
                solve(i, curr + candidates[i])  # same i because reuse is allowed
                

                # SKIP candidates[i]
                current.pop()
                solve(i + 1, curr)

            solve(0, 0)
            return result