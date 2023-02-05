class Solution:
    def minFlips(self, s: str) -> int:
        win_len = len(s)
        double_s = s * 2
        n = len(double_s)
        zero_start, one_start = [], []
        for i in range(n):
            if i % 2 == 0:
                zero_start.append('0')
                one_start.append('1')
            else:
                zero_start.append('1')
                one_start.append('0')
        
        z_start_dif = o_start_dif = 0
        min_dif = float('inf')
        left = 0
        for right in range(n):
            if double_s[right] != zero_start[right]: z_start_dif += 1
            if double_s[right] != one_start[right]: o_start_dif += 1

            if right - left + 1 == win_len:
                min_dif = min(min_dif, z_start_dif, o_start_dif)
                if double_s[left] != zero_start[left]: z_start_dif -= 1
                if double_s[left] != one_start[left]: o_start_dif -= 1
                left += 1
        return min_dif