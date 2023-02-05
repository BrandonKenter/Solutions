class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        cur_p = 0 # current number of passengers
        remaining_drops = [] # min heap of (drop time, numPassengers)
        for trip in trips:
            p, f, t = trip
            while remaining_drops and remaining_drops[0][0] <= f:
                _, dropped_p = heapq.heappop(remaining_drops)
                cur_p -= dropped_p 
            cur_p += p
            if cur_p > capacity: return False
            heapq.heappush(remaining_drops, (t, p))
        return True