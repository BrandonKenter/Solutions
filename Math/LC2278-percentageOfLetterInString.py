class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        letter_count = 0
        for char in s:
            if char == letter: letter_count += 1
        return math.floor(letter_count / n * 100)