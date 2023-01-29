class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # Get counts of each character for both words
        word1_counts, word2_counts = defaultdict(int), defaultdict(int)
        for char in word1: word1_counts[char] += 1
        for char in word2: word2_counts[char] += 1

        # Compare frequencies - if diff is > 3, return False
        for char in word1:
            if abs(word1_counts[char] - word2_counts[char]) > 3: return False
        for char in word2:
            if abs(word2_counts[char] - word1_counts[char]) > 3: return False
        return True