class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        pre_count = 0
        for word in words:
            word_len = len(word)
            if word == s[:word_len]:
                pre_count += 1
        return pre_count