'''
Hash map
O(Nlog(N)) time assuming N values
'''
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        values = defaultdict(int)
        for value, weight in items1:
            values[value] += weight
        
        for value, weight in items2:
            values[value] += weight
        
        return sorted(values.items())


'''
Array
O(N) time assuming N values
'''
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        values = [None] * 1001
        for value, weight in items1:
            if values[value] is None:
                values[value] = 0
            values[value] += weight
        
        for value, weight in items2:
            if values[value] is None:
                values[value] = 0
            values[value] += weight
        
        return [[value, weight] for value, weight in enumerate(values) if weight]