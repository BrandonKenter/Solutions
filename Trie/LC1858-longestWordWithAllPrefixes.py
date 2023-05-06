class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
        
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        max_word = [0, ""] # [length, word]
        for word in words:
            if self.hasPrefixes(root, word):
                if len(word) > max_word[0]:
                    max_word = [len(word), word]
                elif len(word) == max_word[0] and word < max_word[1]:
                    max_word = [len(word), word]
        return max_word[1]
    
    def hasPrefixes(self, root, word):
        cur = root
        for c in word:
            if c in cur.children and cur.children[c].end:
                cur = cur.children[c]
            else:
                return False
        return True