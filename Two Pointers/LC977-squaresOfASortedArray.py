class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        
        out = []
        while l <= r:
            l_num = nums[l] ** 2
            r_num = nums[r] ** 2
            if l_num > r_num:
                out.append(l_num)
                l += 1
            else:
                out.append(r_num)
                r -= 1
        return out[::-1]