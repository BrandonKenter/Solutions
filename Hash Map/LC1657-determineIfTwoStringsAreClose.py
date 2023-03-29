class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1, word2 = list(word1), list(word2)
        counts1, counts2 = Counter(word1), Counter(word2)
        if set(word1) != set(word2):
            return False
        if sorted(counts1.values()) != sorted(counts2.values()):
            return False
        return True
        