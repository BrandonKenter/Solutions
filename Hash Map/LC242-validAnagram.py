class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        s_counts = defaultdict(int)
        for c in s:
            s_counts[c] += 1
        
        for c in t:
            if c not in s_counts or s_counts[c] == 0:
                return False
            s_counts[c] -= 1
        return True