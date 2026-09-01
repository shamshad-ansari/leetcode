class UndergroundSystem:

    def __init__(self):
        # id -> (stationName, checkInTime)
        self.checkedIn = {}

        # (startStation, endStation) -> [totalTime, numberOfTrips]
        self.trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkedIn[id]

        travelTime = t - startTime
        route = (startStation, stationName)

        if route not in self.trips:
            self.trips[route] = [0, 0]

        self.trips[route][0] += travelTime
        self.trips[route][1] += 1

        # They're no longer checked in
        del self.checkedIn[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, numberOfTrips = self.trips[(startStation, endStation)]

        return totalTime / numberOfTrips
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)