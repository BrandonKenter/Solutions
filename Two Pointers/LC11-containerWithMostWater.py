class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        most = 0
        
        while l < r:
            a = min(height[l], height[r]) * (r - l)
            most = max(most, a)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return most