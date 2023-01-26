class Solution:
    def maxScore(self, s: str) -> int:
        left_zeroes = right_ones = 0
        for num in s: 
            if num == "1": right_ones += 1
        
        max_score = 0
        for right in range(len(s) - 1):
            if s[right] == '0': left_zeroes += 1
            if s[right] == '1': right_ones -= 1
            max_score = max(max_score, left_zeroes + right_ones)
        return max_score