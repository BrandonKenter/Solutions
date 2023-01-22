class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        range_nums = set()
        for start, end in ranges:
            for i in range(start, end + 1):
                range_nums.add(i)
        
        for i in range(left, right + 1):
            if i not in range_nums:
                return False
        return True