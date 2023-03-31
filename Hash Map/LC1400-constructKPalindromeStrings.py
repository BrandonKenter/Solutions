class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        counts = Counter(s)
        odds = 0
        for ch, count in counts.items():
            if count % 2:
                odds += 1
        
        if odds > k: return False
        return True
