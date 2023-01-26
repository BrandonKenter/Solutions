'''
Linear search and sorting
'''
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        for word in words:
            word_len = len(word)
            for i in range(len(text)):
                if text[i] == word[0] and word == text[i:i+word_len]:
                    res.append([i, i+word_len-1])
        res.sort()
        return res


'''
Trie
'''
class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        root = TrieNode()
        for word in words:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.end = True
        
        res = []
        for i in range(len(text)):
            cur = root
            j = i
            while j < len(text) and text[j] in cur.children:
                cur = cur.children[text[j]]
                if cur.end:
                    res.append([i, j])
                j += 1
        return res