class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()
        cur_sum = left = 0
        for right in range(len(nums)):
            cur_sum += nums[right] 

            if right - left + 1 == 2:
                if cur_sum in sums:
                    return True
                sums.add(cur_sum)
                cur_sum -= nums[left]
                left += 1
        return False