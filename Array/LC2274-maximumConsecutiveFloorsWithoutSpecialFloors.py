class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        maxi = 0
        maxi = max(special[0] - bottom, top - special[-1])
        for i in range(len(special) - 1):
            if special[i] >= bottom and special[i+1] <= top:
                maxi = max(maxi, special[i+1] - special[i] - 1)
        return maxi
