class Solution:
    def largestPalindromic(self, num: str) -> str:  
        c = Counter(num)
        num_counts = sorted(c.items(), key=lambda x:x[0], reverse=True)
        res = ['' for i in range(len(num))]
        i, j = 0, len(num) - 1
        single = ''
        for num, count in num_counts:
            while count >= 2:
                res[i] = res[j] = num
                i, j = i + 1, j - 1
                count -= 2
            if count == 1:
                if num > single:
                    single = num
        if single: res[i] = single
        s = "".join(res).lstrip('0').rstrip('0')
        return s if s != '' else '0'
        