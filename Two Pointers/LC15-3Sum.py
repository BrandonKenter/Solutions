class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for l in range(len(nums) - 2):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
                
            m, r = l + 1, len(nums) - 1
            while m < r:
                s = nums[l] + nums[m] + nums[r]
                if s < 0:
                    m += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    while m < r and nums[m] == nums[m + 1]:
                        m += 1
                    while m < r and nums[r] == nums[r - 1]:
                        r -= 1
                    m += 1
                    r -= 1
        return res