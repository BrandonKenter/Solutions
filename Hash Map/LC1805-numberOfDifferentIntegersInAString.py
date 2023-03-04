class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        replaced = []
        for c in word:
            if c.isnumeric(): replaced.append(c)
            else: replaced.append(" ")
        replaced = "".join(replaced)
        replaced = replaced.split()
        re_set = set()
        for r in replaced:
            re_set.add(int(r))
        return len(re_set)
        