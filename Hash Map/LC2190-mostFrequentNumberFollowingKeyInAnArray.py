class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        target_counts = defaultdict(int)
        max_count = 0
        max_target = 0

        for i in range(len(nums) - 1):
            if nums[i] == key:
                target = nums[i+1]
                target_counts[target] += 1
                if target_counts[target] > max_count:
                    max_count = target_counts[target]
                    max_target = target
        return max_target