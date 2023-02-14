class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        words = text.split(" ")
        cnt = 0
        for word in words:
            for char in word:
                if char in broken_set:
                    break
            else:
                cnt += 1
        return cnt
