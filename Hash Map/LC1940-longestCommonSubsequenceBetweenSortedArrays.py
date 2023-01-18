'''
Array to store number frequencies
'''
class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)
        num_freq = [0] * 101 # index = num, val at index = frequency
        
        for array in arrays:
            for num in array:
                num_freq[num] += 1
        
        left = 0
        sequence = []
        for right in range(len(num_freq)):
            if num_freq[right] == n:
                sequence.append(right)
        return sequence


'''
Hash map to store number frequencies
'''
class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)
        num_freq = defaultdict(int) # key = num, key = frequency
        
        for array in arrays:
            for num in array:
                num_freq[num] += 1
        
        left = 0
        sequence = []
        for right in range(101):
            if num_freq[right] == n:
                sequence.append(right)
        return sequence