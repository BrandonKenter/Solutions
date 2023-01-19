'''
Hash map
'''
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_counts = defaultdict(int)
        for num in arr:
            num_counts[num] += 1
        num_max = -1
        for num, freq in num_counts.items():
            if num == freq:
                num_max = max(num_max, num)
        return num_max


'''
Array
'''
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_counts = [0] * 501
        for num in arr:
            num_counts[num] += 1
        for num in range(len(num_counts) - 1, 0, -1):
            if num == num_counts[num]:
                return num
        return -1