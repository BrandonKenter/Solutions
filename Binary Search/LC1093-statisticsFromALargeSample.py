class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = maximum = 0
        # Min
        for i in range(len(count)):
            if count[i]: 
                minimum = i
                break
        # Max
        for i in range(len(count) - 1, -1, -1):
            if count[i]:
                maximum = i
                break

        # Mode
        mode = count.index(max(count))

        # Mean
        total_sum = sum([i * v for i, v in enumerate(count)])
        total_el = sum(count)
        mean = total_sum / total_el

        # Median
        n = sum(count)
        for i in range(len(count) - 1):
            count[i + 1] += count[i]
        median1 = bisect.bisect(count, (n - 1) / 2)
        median2 = bisect.bisect(count, n / 2)
        median = (median1 + median2) / 2.0
        
        return [minimum, maximum, mean, median, mode]
