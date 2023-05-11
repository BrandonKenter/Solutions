class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        target_sum = total_sum / k
        if total_sum % k:
            return False
        k_sums = [0 for i in range(k)]
        nums.sort(reverse=True)

        def backtrack(i):
            if i == len(nums):
                return True
            
            for j in range(len(k_sums)):
                if k_sums[j] + nums[i] <= target_sum:
                    k_sums[j] += nums[i]
                    if backtrack(i+1):
                        return True
                    k_sums[j] -= nums[i]
            return False

        return backtrack(0)
