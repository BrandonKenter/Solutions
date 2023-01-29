class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_position(check_left):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = l + (r - l) // 2
                val = nums[m]
                if val == target:
                    if check_left:
                        res[0] = m
                        r = m - 1
                    else:
                        res[1] = m
                        l = m + 1
                elif val < target:
                    l = m + 1
                else:
                    r = m - 1

        res = [-1, -1]
        find_position(True)
        find_position(False)
        return res
