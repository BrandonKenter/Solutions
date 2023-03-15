class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        w_freqs = [] # frequencies of each word's lexographically smallest char
        for w in words:
            w_freq = self.get_freq(w) 
            w_freqs.append(w_freq)
        w_freqs.sort() # sort to do binary search on it

        # Binary search to find the last T that satisfies the condition:
        #   - q_freq < w_freqs[mid]
        # Using left < right because we are searching for an insert position
        # In other words, we are not searching for a specific number,
        #   only the last number that satisfies a certain condition.
        res = []
        for query in queries:
            q_freq = self.get_freq(query)
            
            left, right = 0, len(w_freqs)
            while left < right:
                mid = (left + right) // 2
                if q_freq < w_freqs[mid]:
                    right = mid
                else:
                    left = mid + 1
            # Answer for this query is the number of elements to the right of 
            #   the left index. This is the insert position.
            res.append(len(w_freqs) - left)
        return res
    
    # Gets the frequency of this word's lexographically smallest character
    def get_freq(self, word):
        w_freq = float('inf')
        largest_c = 'za' # largest char seen
        c_freqs = Counter(word)
        for c, freq in c_freqs.items():
            if c < largest_c:
                largest_c = c
                w_freq = freq
        return w_freq
        