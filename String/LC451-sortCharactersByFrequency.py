class Solution:
    def frequencySort(self, s: str) -> str:
        freq = [[] for i in range(len(s) + 1)]
        counts = Counter(s)
        
        for char, count in counts.items():
            freq[count].append(char)

        res = []
        for i in range(len(s), -1, -1):
            for char in freq[i]:
                res.append(i * char)
        return "".join(res)