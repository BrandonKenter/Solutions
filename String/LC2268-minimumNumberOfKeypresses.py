class Solution:
    def minimumKeypresses(self, s: str) -> int:
        freq = [[] for i in range(len(s) + 1)]
        counts = Counter(s)

        for char, count in counts.items():
            freq[count].append(char)
        
        keypresses = 0
        used = 0
        for i in range(len(s), -1, -1):
            for char in freq[i]:
                used += 1
                keypresses += i * (math.ceil(used / 9))
        return keypresses