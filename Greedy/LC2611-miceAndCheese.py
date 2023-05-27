class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diffs = [[] for i in range(len(reward1))]
        for i in range(len(reward1)):
            r1, r2 = reward1[i], reward2[i]
            diffs[i] = [r1 - r2, i]
            
        res = 0
        used = set()
        for diff, i in sorted(diffs, reverse=True):
            print(diff)
            if k > 0:
                used.add(i)
                res += reward1[i]
                k -= 1
        
        for i, r in enumerate(reward2):
            if i not in used:
                res += r
        return res
