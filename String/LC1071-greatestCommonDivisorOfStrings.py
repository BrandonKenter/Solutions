class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        divs = set()
        maxi, maxi_str = 0, ""
        
        for i in range(len(str1)):
            t = i + 1
            if m % t != 0:
                continue
            if str1[:i+1] * (m // t) == str1:
                divs.add(tuple(str1[:i+1]))
        
        for i in range(len(str2)):
            t = i + 1
            if n % t != 0:
                continue
            if str2[:i+1] * (n // t) == str2:
                if tuple(str2[:i+1]) in divs:
                    if i + 1 > maxi:
                        maxi = i + 1
                        maxi_str = str2[:i+1]
        return maxi_str
