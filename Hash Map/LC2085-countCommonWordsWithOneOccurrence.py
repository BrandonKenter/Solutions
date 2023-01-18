class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_counts, words2_counts = Counter(words1), Counter(words2)
        count = 0
        for word in words1:
            if words1_counts[word] == 1 and words2_counts[word] == 1:
                count += 1
        return count