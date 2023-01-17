class Solution:
    def minPartitions(self, n: str) -> int:
        max_num = 0
        for char in n:
            max_num = max(max_num, int(char))
        return max_num