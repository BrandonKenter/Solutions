class Solution:
    def longestPalindrome(self, s: str) -> str:

        def get_pali_length(left, right):
            nonlocal longest, res
            while left >= 0 and right < len(s) and s[left] == s[right]:
                length = right - left + 1
                if length > longest:
                    longest = length
                    res = s[left:right+1]
                left -= 1
                right += 1
        
        res = ""
        longest = 0
        for i in range(len(s)):
            get_pali_length(i, i) # odd length
            get_pali_length(i, i+1) # even length
        return res