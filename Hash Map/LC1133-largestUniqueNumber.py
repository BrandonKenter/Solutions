'''
Hash map
'''
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        max_num = -1
        for num, num_freq in freq.items():
            if num_freq == 1:
                max_num = max(max_num, num)
        return max_num


'''
Array
'''
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = [0] * 1001
        for num in nums:
            freq[num] += 1
        for num in range(len(freq) - 1, -1, -1):
            if freq[num] == 1:
                return num
        return -1