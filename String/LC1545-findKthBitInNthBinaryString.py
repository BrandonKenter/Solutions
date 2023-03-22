class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ['0']
        for i in range(1, n+1):
            cur = [s[i-1]]
            cur.append("1")
            cur.append("".join(["1" if b == "0" else "0" for b in s[i-1]][::-1]))
            cur = "".join(cur)
            s.append(cur)
        return s[-1][k-1]
