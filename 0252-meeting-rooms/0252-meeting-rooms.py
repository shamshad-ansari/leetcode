# Just copy pasted merge intervals code to see if it works (Did it some time ago)
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
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
                if x < mx:
                    mx = max(mx, y)
                    return False
                else:
                    break
                j += 1
            i = j
        # result.append([first,mx])
        return True
        