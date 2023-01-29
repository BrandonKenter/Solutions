class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_counts = defaultdict(int)
        for word in s1.split():
            word_counts[word] += 1
        for word in s2.split():
            word_counts[word] += 1
        
        res = []
        for word, word_count in word_counts.items():
            if word_count == 1:
                res.append(word)
        return res