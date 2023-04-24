class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        pre = []
        for i in range(len(nums)):
            if pre:
                pre.append(pre[i-1] + nums[i])
            else:
                pre.append(nums[i])

        for q in queries:
            left, right = 0, len(pre)
            while left < right:
                mid = (left + right) // 2
                if pre[mid] > q:
                    right = mid
                else:
                    left = mid + 1
            res.append(right)
        return res
    
