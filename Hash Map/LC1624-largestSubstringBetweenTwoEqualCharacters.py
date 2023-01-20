class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        longest = -1
        seen = defaultdict(int)
        for i, char in enumerate(s):
            if char in seen:
                longest = max(longest, i - seen[char] + 1 - 2)
            else:
                seen[char] = i
        return longest