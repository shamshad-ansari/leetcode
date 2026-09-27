# So basically the m=number of meeting rooms would be the number of maximum overlaps between the meeting times
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        events = []

        for start, end in intervals:
            events.append([start, +1])
            events.append([end, -1])

        # We need to also account for events which start and end at the same time for our events we want the 
        # end time to come first as it was already started else we get wrong answer
        events.sort(key= lambda x: (x[0], x[-1]))
        maxOverlap = 0
        cum = 0
        print(events)
        for time, delta in events:
            cum += delta
            maxOverlap = max(maxOverlap, cum)

        return maxOverlap