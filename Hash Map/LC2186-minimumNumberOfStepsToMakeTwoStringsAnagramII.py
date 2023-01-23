class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counts = Counter(s)
        t_counts = Counter(t)

        steps = 0
        for char, count in t_counts.items():
            print(count)
            if count > s_counts[char]:
                steps += count - s_counts[char]
        
        for char, count in s_counts.items():
            if count > t_counts[char]:
                steps += count - t_counts[char]
        return steps