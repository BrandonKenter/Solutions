class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = float('-inf')
        cur_vowels = left = 0
        for right in range(len(s)):
            if s[right] in 'aeiou':
                cur_vowels += 1
            
            if right - left + 1 == k:
                max_vowels = max(max_vowels, cur_vowels)
                if s[left] in 'aeiou':
                    cur_vowels -= 1
                left += 1
        return max_vowels