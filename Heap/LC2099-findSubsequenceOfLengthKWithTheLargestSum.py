'''
Min heap
O(Nlog(k)) time / O(N) space
'''
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        min_h = []
        for num in nums:
            heappush(min_h, num)
            if len(min_h) > k:
                heappop(min_h)
        sub = Counter(min_h)
        res = []
        for num in nums:
            if sub[num] > 0:
                sub[num] -= 1
                res.append(num)
        return res


'''
Sorting 
O(Nlog(N)) time / O(N) space
'''
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums_s = sorted(nums)
        sub = Counter(nums_s[n-k:])
        
        res = []
        for num in nums:
            if sub[num] > 0:
                sub[num] -= 1
                res.append(num)
        return res
