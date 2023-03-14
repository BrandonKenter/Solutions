class Solution:
    def oddString(self, words: List[str]) -> str:
        difs = {}

        for word in words:
            dif = []
            for i in range(1, len(word)):
                dif.append(ord(word[i]) - ord(word[i-1]))
            if tuple(dif) in difs:
                difs[tuple(dif)][1] += 1
            else:
                difs[tuple(dif)] = [word, 1]
        
        for word, count in difs.values():
            if count == 1:
                return word
