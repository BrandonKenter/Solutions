class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counts = Counter(chars)
        res = 0
        for word in words:
            word_counts = Counter(word)
            for char, char_count in word_counts.items():
                if char_count > chars_counts[char]:
                    break
            else:
                res += len(word)
        return res