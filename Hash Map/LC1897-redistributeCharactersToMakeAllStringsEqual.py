class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        char_counts = defaultdict(int)
        for word in words:
            for char in word:
                char_counts[char] += 1
        
        for char, char_count in char_counts.items():
            if char_count % n != 0:
                return False
        return True