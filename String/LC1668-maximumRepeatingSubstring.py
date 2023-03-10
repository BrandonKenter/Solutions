class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(word)
        maxi = left = right = cur = 0
        while right < len(sequence):
            if sequence[right:right+n] == word:
                right += n
                cur += 1
                maxi = max(maxi, cur)
            else:
                cur = 0
                # Need to only increment left by 1 because jumping to 
                # right could skip potential characters in max substring
                left += 1
                right = left
        return maxi
