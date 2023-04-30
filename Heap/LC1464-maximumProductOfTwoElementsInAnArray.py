'''
Max heap
O(N) time / O(N) space
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_h = [-num for num in nums]
        heapq.heapify(max_h)
        max1 = -1 * heapq.heappop(max_h)
        max2 = -1 * heapq.heappop(max_h)
        return (max1 - 1) * (max2 - 1)

    
'''
Min Heap
O(Nlog(2)) time / O(1) space
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_h = []
        for num in nums:
            heappush(min_h, num)
            if len(min_h) > 2:
                heappop(min_h)
        return (min_h[0] - 1) * (min_h[1] - 1)


'''
Variables for two highest elements 
O(N) time / O(1) space
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max2 = 0
        for num in nums:
            if num >= max1:
                max2 = max1
                max1 = num
            elif num >= max2:
                max2 = num
        return (max1 - 1) * (max2 - 1)
    
