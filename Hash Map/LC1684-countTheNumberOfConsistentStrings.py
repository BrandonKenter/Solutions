class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        res = []
        for word in words:
            i = 0
            for char in word:
                if char in allowed_set: i += 1
                else: break
            if i == len(word): res.append(word)
        return len(res)