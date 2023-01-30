class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = cur_alt = 0
        for g in gain:
            cur_alt += g
            max_alt = max(max_alt, cur_alt)
        return max_alt