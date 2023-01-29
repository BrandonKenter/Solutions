class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num_counts = defaultdict(int)
        for num in nums: num_counts[num] += 1
        
        res = 0
        for num, num_count in num_counts.items():
            if num_count == 1: res += num
        return res