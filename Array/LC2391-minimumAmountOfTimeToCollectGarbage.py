class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel_time_sums = [0 for i in range(len(garbage))]
        cur_sum = 0
        for i, t in enumerate(travel):
            travel_time_sums[i] = cur_sum
            cur_sum += t
        travel_time_sums[-1] = cur_sum

        res = 0
        max_m = max_p = max_g = 0
        for i, g in enumerate(garbage):
            g_counts = Counter(g)
            for garb, count in g_counts.items():
                res += count
                if garb == 'M':
                    max_m = i
                elif garb == 'P':
                    max_p = i
                else:
                    max_g = i
        res += (travel_time_sums[max_m] + travel_time_sums[max_p] + travel_time_sums[max_g])
        return res
            