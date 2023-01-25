class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        pre_len = len(searchWord)
        for i in range(len(words)):
            word = words[i]
            if word[:pre_len] == searchWord:
                return i + 1
        return -1