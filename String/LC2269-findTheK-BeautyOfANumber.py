class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count, left, s_num = 0, 0, str(num)
        left = 0
        for right in range(len(s_num)):
            if right - left + 1 == k:
                sub = int(s_num[left:right+1])
                if sub != 0 and num % sub == 0:
                    count += 1
                left += 1
        return count