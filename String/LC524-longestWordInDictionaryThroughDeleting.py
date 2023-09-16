class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        maxiLen = 0
        maxiWord = ''
        for word in dictionary:
            j = 0
            for i in range(len(s)):
                if s[i] == word[j]:
                    j += 1
                    if j == len(word):
                        break
            if j == len(word):
                if len(word) > maxiLen:
                    maxiLen = len(word)
                    maxiWord = word
                elif len(word) == maxiLen:
                    maxiWord = min(maxiWord, word)
        return maxiWord
        