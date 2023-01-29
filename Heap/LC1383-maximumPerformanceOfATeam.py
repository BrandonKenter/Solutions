class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        people = [(eff, spd) for eff, spd in sorted(zip(efficiency, speed), reverse=True)]
        max_perf = k_speed_sum = 0
        k_min_speed = []
        for eff, spd in people:
            k_speed_sum += spd
            heapq.heappush(k_min_speed, spd)
            max_perf = max(max_perf, eff * k_speed_sum)
            if len(k_min_speed) == k:
                k_speed_sum -= heapq.heappop(k_min_speed)
        return max_perf % (10**9 + 7)