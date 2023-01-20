class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count, t_count = Counter(s), Counter(t)
        for char, char_count in t_count.items():
            if char_count > s_count[char]:
                return char