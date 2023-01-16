class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def is_bijection(w1, w2):
            w1_dict, w2_dict = {}, {}
            for i in range(len(w1)):
                if w1[i] in w1_dict and w2[i] != w1_dict[w1[i]]: return False
                if w2[i] in w2_dict and w1[i] != w2_dict[w2[i]]: return False
                w1_dict[w1[i]] = w2[i]
                w2_dict[w2[i]] = w1[i]
            return True

        res = []
        for word in words:
            if is_bijection(word, pattern):
                res.append(word)
        return res