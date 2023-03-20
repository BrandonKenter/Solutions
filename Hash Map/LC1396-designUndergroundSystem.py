class UndergroundSystem:

    def __init__(self):
        self.checkedCustomer = {} # id : (stationName, t)
        self.travelPairs = {} # (startStation, endStation) : [totalTime, totalInstances]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedCustomer[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.checkedCustomer[id][0]
        elapsedTime = t - self.checkedCustomer[id][1]
        if (startStation, stationName) in self.travelPairs:
            self.travelPairs[(startStation, stationName)][0] += elapsedTime
            self.travelPairs[(startStation, stationName)][1] += 1
        else:
            self.travelPairs[(startStation, stationName)] = [elapsedTime, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime = self.travelPairs[(startStation, endStation)][0]
        totalInstances = self.travelPairs[(startStation, endStation)][1]
        return totalTime / totalInstances


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
