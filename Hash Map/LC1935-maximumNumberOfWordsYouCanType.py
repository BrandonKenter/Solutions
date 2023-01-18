class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        words = text.split(" ")

        cnt = 0
        for word in words:
            i = 0
            while i < len(word):
                if word[i] in broken_set:
                    break
                i += 1
            if i == len(word): 
                cnt += 1
        return cnt