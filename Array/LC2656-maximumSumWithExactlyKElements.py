class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        score = 0
        for i in range(k):
            score += maxi
            maxi += 1
        return score
        