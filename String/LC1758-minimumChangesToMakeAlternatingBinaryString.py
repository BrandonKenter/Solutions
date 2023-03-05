class Solution:
    def minOperations(self, s: str) -> int:
        z_dif = o_dif = 0
        for i in range(len(s)):
            if (s[i] != '0' and i%2==0) or (s[i] != '1' and i%2==1):
                z_dif += 1
            elif (s[i] != '1' and i%2==0) or (s[i] != '0' and i%2==1):
                o_dif += 1
        return min(z_dif, o_dif)
