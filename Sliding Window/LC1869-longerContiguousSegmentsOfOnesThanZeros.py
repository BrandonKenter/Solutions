class Solution:
    def checkZeroOnes(self, s: str) -> bool:

        def find_longest(val):
            max_consec, left = 0, 0
            for right in range(len(s)):
                if s[right] != val:
                    left = right + 1
                max_consec = max(max_consec, right - left + 1)
            return max_consec
        
        max_zero = find_longest('0')
        max_one = find_longest('1')
        return max_one > max_zero
        
