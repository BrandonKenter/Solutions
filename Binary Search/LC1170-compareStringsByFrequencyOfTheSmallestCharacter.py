class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def get_freq(word):
            smallest = 'z'
            counts = defaultdict(int)
            for c in word:
                counts[c] += 1
                if c < smallest:
                    smallest = c
            return counts[smallest]

        freqs = []
        for word in words:
            freq = get_freq(word)
            freqs.append(freq)
        freqs.sort()
        
        res = []
        for q in queries:
            q_freq = get_freq(q)
            left, right = 0, len(freqs)
            while left < right:
                mid = (left + right) // 2
                if freqs[mid] > q_freq:
                    right = mid
                else:
                    left = mid + 1
            res.append(len(freqs) - right)
        return res
