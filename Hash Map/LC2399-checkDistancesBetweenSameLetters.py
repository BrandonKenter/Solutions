class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        seen = defaultdict(int)
        for i, char in enumerate(s):
            if char in seen:
                idx = ord(char) - ord('a')
                if distance[idx] != i - seen[char] - 1:
                    return False
            else:
                seen[char] = i
        return True
