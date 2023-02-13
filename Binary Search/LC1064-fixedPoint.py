# Template 2
# Find minimal k where isCondition(k) is True
# isCondition is "if value >= mid index"
# F F T T T T T <- find first index that is TRUE
# We use the relationship between the index we are at and the value
# at that index to update our search space. Since the array is sorted,
# this is possible. In the first example, if we are at index 2, our value
# is 0. If we search to the left, it is impossible for our index to 
# equal the value at that index since the integers are distinct and 
# increasing, but if we search to the right, the value CAN catch up
# to the index. So we search right. The opposite can be said if 
# value >= mid. If our value is greater than or equal to mid, we 
# want to update our search space to include right and we treat this 
# as our leftmost True value so far. Note that it technically isn't 
# True if val > mid, we just say it is True to maintain the pattern
# across all problems. We won't evaluate it as True in the end unless
# the ending index equals the ending value anyways.
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            val = arr[mid]
            if val >= mid:
                right = mid
            else:
                left = mid + 1
        return left if arr[left] == left else -1


# Template 1
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        smallest, left, right = -1, 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = arr[mid]
            if val == mid:
                smallest = val
                right = mid - 1
            elif val < mid:
                left = mid + 1
            else:
                right = mid - 1
        return smallest
