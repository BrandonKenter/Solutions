class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [0] * len(s)
        
        left_prev = float('-inf')
        for i in range(len(s)):
            char = s[i]
            if char == c: left_prev = i
            ans[i] = i - left_prev
            
        right_prev = float('inf')
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char == c: right_prev = i
            ans[i] = min(ans[i], right_prev - i)   
        return ans