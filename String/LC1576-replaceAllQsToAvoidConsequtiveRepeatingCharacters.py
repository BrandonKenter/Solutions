class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                # First char case
                if i == 0:
                    if i + 1 < len(s):
                        if s[i+1] == '?':
                            s[i] = 'a'
                        else:
                            s[i] = 'a' if s[i+1] != 'a' else 'b'
                    else:
                        s[i] = 'a'
                # Last char case
                elif i == len(s) - 1:
                    if s[i-1] == 'a':
                        s[i] = 'b'
                    else:
                        s[i] = 'a'
                # Middle char case
                else:
                    if s[i+1] == '?':
                        s[i] = 'a' if s[i-1] != 'a' else 'b'
                    else:
                        for c in ['a', 'b', 'c']:
                            if c not in [s[i-1], s[i+1]]:
                                s[i] = c
                                break
        return "".join(s)
