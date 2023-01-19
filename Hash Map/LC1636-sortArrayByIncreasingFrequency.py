class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_freq = defaultdict(int) # index = num, value = frequency
        n = len(nums)
        for num in nums:
            num_freq[num] += 1
        
        freq_to_num = [[] for i in range(n + 1)]
        for num in range(100, -101, -1):
            if num in num_freq:
                freq = num_freq[num]
                freq_to_num[freq].append(num)
        
        res = []
        for i in range(n + 1):
            if len(freq_to_num[i]):
                for num in freq_to_num[i]:
                    for j in range(i):
                        res.append(num)
        return res