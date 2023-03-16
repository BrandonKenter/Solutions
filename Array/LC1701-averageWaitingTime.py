class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = next_available_time = 0
        for arrival, time in customers:
            next_available_time = time + max(next_available_time, arrival)
            wait += next_available_time - arrival
        return wait / len(customers)
            