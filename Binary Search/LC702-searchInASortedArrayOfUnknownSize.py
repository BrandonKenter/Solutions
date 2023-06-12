# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 10**4
        bound = 2**31 - 1
        while left < right:
            mid = (left + right) // 2
            val = reader.get(mid)
            if val == bound or val >= target:
                right = mid
            else:
                left = mid + 1
        return left if reader.get(left) == target else -1
        