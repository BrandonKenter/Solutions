class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            groups = []
            i = 0
            while i < len(s):
                group = s[i:i+k]
                g_sum = 0
                for digit in group: g_sum += int(digit)
                groups.append(str(g_sum))
                i += k
            s = "".join(groups)
        return s