class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        num_counts = defaultdict(int)
        res = []
        left = 0
        for right in range(len(nums)):
            num_counts[nums[right]] += 1

            if right - left + 1 == k:
                res.append(len(num_counts))
                num_counts[nums[left]] -= 1
                if num_counts[nums[left]] == 0:
                    num_counts.pop(nums[left])
                left += 1
        return res