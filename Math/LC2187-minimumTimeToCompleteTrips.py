class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, max(time) * totalTrips
        while left < right:
            trips = 0
            mid = (left + right) // 2
            for trip_time in time:
                trips += mid // trip_time
            if trips >= totalTrips:
                right = mid
            else:
                left = mid + 1
        return right
        