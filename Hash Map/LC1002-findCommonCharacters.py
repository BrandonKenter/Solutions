class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res_counts = defaultdict(int)
        for char in words[0]:
            res_counts[char] += 1

        for i in range(1, len(words)):
            word = words[i]
            char_counts = defaultdict(int)
            for char in word:
                char_counts[char] += 1
            for char in res_counts:
                res_counts[char] = min(res_counts[char], char_counts[char])
        
        res = []
        for char, char_count in res_counts.items():
            if char_count != 0:
                for i in range(char_count):
                    res.append(char)
        return res