class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower().split()

        banned_set = set(banned)
        word_freq = defaultdict(int)

        for word in paragraph:
            if word not in banned_set:
                word_freq[word] += 1
        return max(word_freq, key=word_freq.get)