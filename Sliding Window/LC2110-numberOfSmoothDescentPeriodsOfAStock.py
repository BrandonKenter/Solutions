class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 1
        left = 0
        for right in range(1, len(prices)):
            # first condition executes when the value at this index is a part 
            # of the current smooth descent period

            # right - left is the number of extra subarrays this index adds
            # example: [4,3,2,1]
            #                 ^
            # at this index, we are adding [4,3,2,1], [3,2,1], [2,1] subarrays
            # these are all the possible subarrays at end at this new index
            # then we add + 1 to include the subarray of just this index
            if prices[right] == prices[right - 1] - 1:
                count += right - left + 1
            # this index is not a part of the previous smooth descent period
            else:
                left = right
                count += 1
        return count
        