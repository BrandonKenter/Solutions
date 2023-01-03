class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s2_count = defaultdict(int)
        l = 0
        
        for r in range(len(s2)):
            s2_count[s2[r]] += 1
            if s1_count == s2_count: return True
            if r >= len(s1) - 1:
                s2_count[s2[l]] -= 1
                if s2_count[s2[l]] == 0:
                    s2_count.pop(s2[l])
                l += 1
        return False