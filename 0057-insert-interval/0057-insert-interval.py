class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        def position(intervals):
            start = 0
            end = len(intervals) - 1
            while start<=end:
                mid = (start + end)//2

                if intervals[mid][0] == newInterval[0]:
                    return mid
                if intervals[mid][0] > newInterval[0]:
                    end = mid -1
                else:
                    start = mid + 1
            return start
        
        idx = position(intervals)
        intervals.insert(idx, newInterval)

        result = []

        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result