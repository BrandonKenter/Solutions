class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        prefix_sum = cur_sum = max_sum = 0
        
        for num in sorted(satisfaction, reverse=True):
            prefix_sum += num
            cur_sum += prefix_sum
            max_sum = max(max_sum, cur_sum)
        return max_sum
        