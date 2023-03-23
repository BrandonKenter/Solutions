class Solution:
    def numSplits(self, s: str) -> int:
        ld, rd = defaultdict(int), Counter(s)
        count = 0
        for i in range(len(s) - 1):
            rd[s[i]] -= 1
            if rd[s[i]] == 0:
                rd.pop(s[i])
            ld[s[i]] += 1
            if len(ld) == len(rd):
                count += 1
        return count
