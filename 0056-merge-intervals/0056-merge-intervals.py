class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        n = len(intervals)
        result = []
        while i < n:
            first, last = intervals[i]
            j = i+1
            mx = last

            while j < n:
                x, y = intervals[j]
                if x <= mx:
                    mx = max(mx, y)
                else:
                    result.append([first,mx])
                    break
                j += 1
            i = j
        result.append([first,mx])
        return result