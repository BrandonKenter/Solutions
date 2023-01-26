class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for i in range(len(words) - 1):
            for j in range(i+1, len(words)):
                word1, word2 = words[i], words[j]
                if word1 in word2:
                    res.add(word1)
                elif word2 in word1:
                    res.add(word2)
        return set(res)