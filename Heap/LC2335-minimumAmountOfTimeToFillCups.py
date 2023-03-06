class Solution:
    def fillCups(self, amount: List[int]) -> int:
        max_heap = [-a for a in amount if a != 0]
        sec = 0
        while max_heap:
            if len(max_heap) > 1:
                type_1, type_2  = heappop(max_heap), heappop(max_heap)
                type_1 += 1
                type_2 += 1
                if type_1: heappush(max_heap, type_1)
                if type_2: heappush(max_heap, type_2)
                sec += 1
            else:
                type_1 = heappop(max_heap)
                sec += -1 * type_1
        return sec
