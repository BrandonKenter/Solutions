class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        evens_s1 = defaultdict(int)
        evens_s2 = defaultdict(int)
        odds_s1 = defaultdict(int)
        odds_s2 = defaultdict(int)

        for i in range(4):
            if i % 2 == 0:
                evens_s1[s1[i]] += 1
                evens_s2[s2[i]] += 1
            else:
                odds_s1[s1[i]] += 1
                odds_s2[s2[i]] += 1
        
        if evens_s1 == evens_s2 and odds_s1 == odds_s2:
            return True
        else:
            return False
            