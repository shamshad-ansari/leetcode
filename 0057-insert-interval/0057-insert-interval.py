class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result = []
        for interval in intervals:
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(interval[1], result[-1][1])
        return result
