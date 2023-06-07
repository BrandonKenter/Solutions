class Solution:
    def minimizedStringLength(self, s: str) -> int:
        uniques = set(s)
        return len(uniques)
        