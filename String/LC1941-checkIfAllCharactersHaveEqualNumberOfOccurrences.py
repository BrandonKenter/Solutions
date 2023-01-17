class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_counts = defaultdict(int)
        for char in s:
            char_counts[char] += 1
        
        count = -1
        for cur_count in char_counts.values():
            if count == -1:
                count = cur_count
                continue
            elif cur_count != count:
                return False
        return True