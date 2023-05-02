class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        numbers = set()
        i = 0
        while i < len(word):
            if word[i].isnumeric():
                j = i + 1
                while j < len(word) and word[j].isnumeric():
                    j += 1
                numbers.add(int(word[i:j]))
                i = j
            else:
                i += 1
        return len(numbers)