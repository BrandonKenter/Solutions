class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1: return True

        if word[0].isupper() and word[1].isupper():
            i = 2
            while i < len(word):
                if word[i].isupper() == False: return False
                i += 1
        elif word[0].islower():
            i = 1
            while i < len(word):
                if word[i].isupper(): return False
                i += 1
        else:
            i = 2
            while i < len(word):
                if word[i].isupper(): return False
                i += 1
        return True