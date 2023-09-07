class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        maxi = left = 0
        for right in range(len(seats)):
            # Case where we found a seated person
            if seats[right] == 1:
                m = (left + right) // 2
                if seats[left] == 1:
                    maxi = max(maxi, m - left)
                else:
                    maxi = max(maxi, right)
                left = right
        # There is not a right seated person
        # Greedily take the rightmost position
        if seats[n-1] == 0:
            maxi = max(maxi, n - 1 - left)
        return maxi