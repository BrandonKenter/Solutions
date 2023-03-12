class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        div_len = defaultdict(int)
        maxi = 0
        maxi_str = ""
        
        for i in range(len(str1)):
            t = i + 1
            if m % t != 0:
                continue
            if str1[:i+1] * (m // t) == str1:
                div_len[tuple(str1[:i+1])] = i + 1
        
        for i in range(len(str2)):
            t = i + 1
            if n % t != 0:
                continue
            if str2[:i+1] * (n // t) == str2:
                if tuple(str2[:i+1]) in div_len:
                    if i + 1 > maxi:
                        maxi = i + 1
                        maxi_str = str2[:i+1]
        return maxi_str
        