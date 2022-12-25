class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()

        while n != 1:
            cur_sum = 0
            while n:
                cur_num = n % 10
                cur_sum += cur_num ** 2
                n = n // 10
            if cur_sum in vis:
                return False
            vis.add(cur_sum)
            n = cur_sum

        return True