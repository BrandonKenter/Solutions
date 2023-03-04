class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) == 1 or len(s) != len(goal): return False
        dif_i, dif_j = -1, -1
        dif = 0
        counts = defaultdict(int)
        
        for i in range(len(s)):
            if s[i] != goal[i]: 
                if dif_i == -1: dif_i = i
                else: dif_j = i
                dif += 1
            counts[s[i]] += 1

        if dif > 2: return False
        if dif == 0 and max(counts.values()) < 2: return False
        if s[dif_i] != goal[dif_j] or s[dif_j] != goal[dif_i]: return False
        return True
