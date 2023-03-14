class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            left, right = l[i], r[i]
            sub = nums[left:right+1]
            sub.sort()
            dif = sub[1] - sub[0]
            for j in range(2, len(sub)):
                if sub[j] - sub[j-1] != dif:
                    res.append(False)
                    break
            else:
                res.append(True)
        return res
        