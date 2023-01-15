class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        count_1 = count_2 = 0
        
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                if i < half: count_1 += 1
                else: count_2 += 1
        return count_1 == count_2