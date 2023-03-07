class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        births = sorted([log[0] for log in logs])
        deaths = sorted([log[1] for log in logs])

        maxi = max_y = 0
        b = d = cur_count = 0
        while b < len(births) and d < len(deaths):
            if deaths[d] <= births[b]:
                cur_count -= 1
                d += 1
            else:
                cur_count += 1
                if cur_count > maxi:
                    maxi = cur_count
                    maxi_y = births[b]
                b += 1
        return maxi_y
                