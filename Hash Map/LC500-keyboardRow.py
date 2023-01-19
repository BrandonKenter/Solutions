class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        row_2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        row_3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

        res = []
        for word in words:
            word_lower = word.lower()
            word_set = set(word_lower)
            if word_set.issubset(row_1) or word_set.issubset(row_2) or word_set.issubset(row_3):
                res.append(word)
        return res