class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ts = {}

        for i in range(len(s)):
            if s[i] in st and st[s[i]] != t[i] or t[i] in ts and ts[t[i]] != s[i]:
                return False
            st[s[i]] = t[i]
            ts[t[i]] = s[i]
        return True