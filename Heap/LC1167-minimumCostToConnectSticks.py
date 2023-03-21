class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_h = [stick for stick in sticks]
        heapify(min_h)
        total_c = 0
        while len(min_h) > 1:
            s1 ,s2 = heappop(min_h), heappop(min_h)
            c = s1 + s2
            total_c += c
            heappush(min_h, c)
        return total_c 
