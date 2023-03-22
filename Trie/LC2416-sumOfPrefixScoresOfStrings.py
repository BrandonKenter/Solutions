class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
    
    def add_word(self, word):
        root = self
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
            root.count += 1

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        res = []
        for word in words:
            count = 0
            cur = root
            for c in word:
                if c in cur.children:
                    count += cur.children[c].count
                else:
                    break
                cur = cur.children[c]
            res.append(count)
        return res
        