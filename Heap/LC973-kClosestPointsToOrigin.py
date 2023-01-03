'''
Max heap
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = [[-1 * (x ** 2 + y ** 2), x, y] for x, y in points] # [-distance, x, y]
        max_h = []
        
        for p in d:
            heapq.heappush(max_h, p)
            if len(max_h) > k:
                heapq.heappop(max_h)
        
        out = []
        for p in max_h:
            out.append([p[1], p[2]])
        return out

'''
Min heap
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_h = [[(x ** 2 + y ** 2), x, y] for x, y in points] # [distance, x, y]
        heapq.heapify(min_h)
        
        out = []
        for i in range(k):
            dist, x, y = heapq.heappop(min_h)
            out.append([x, y])
        return out