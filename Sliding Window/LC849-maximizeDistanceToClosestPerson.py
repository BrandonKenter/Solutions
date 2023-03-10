class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        maxi = left = 0
        for right in range(1, len(seats)):
            # Case where we found a seated person
            if seats[right] == 1:
                # There is a left seated person
                # Take the middle position
                if seats[left] == 1:
                    m = (left + right) // 2
                    maxi = max(maxi, m - left)
                # There is not a left seated person
                # Greedily take the leftmost position
                else:
                    maxi = max(maxi, right - left)
                left = right
        # There is not a right seated person
        # Greedily take the rightmost position
        if seats[n-1] == 0:
            maxi = max(maxi, n - 1 - left)
        return maxi
        