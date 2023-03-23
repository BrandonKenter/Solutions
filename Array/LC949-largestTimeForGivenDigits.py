class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = ''
        for i, a in enumerate(A):
            for j, b in enumerate(A):
                for k, c in enumerate(A):
                    for l, d in enumerate(A):
                        if i == j or i == k or j == k or i == l or j == l or k == l:
                            continue
                        hour, minute = str(a) + str(b), str(c) + str(d)
                        if hour < '24' and minute < '60':
                            ans = max(ans, hour + ':' + minute)
        return ans
        