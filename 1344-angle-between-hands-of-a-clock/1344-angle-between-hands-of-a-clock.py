class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        adjustment = 1/2 * minutes
        hourDegrees = 30 * hour + adjustment
        minutesDegrees = 6 * minutes
        ans = abs(hourDegrees - minutesDegrees)
        if ans > 180:
            return 360-ans
        return ans