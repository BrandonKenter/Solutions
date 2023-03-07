class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_s = sum(arr)
        if total_s % 3 != 0: return False
        part_sum = total_s // 3
        cur_sum = 0
        c = 0
        for a in arr:
            cur_sum += a
            if cur_sum == part_sum:
                c += 1
                cur_sum = 0
        return c >= 3
        