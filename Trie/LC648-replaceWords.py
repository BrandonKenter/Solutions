'''
Prefix hash
O(W^2*N) time / O(N) space where W is the length of the word and N is 
the length of the sentence.
'''
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(" ")
        roots = set(dictionary)
        for i in range(len(sentence)):
            word = sentence[i]
            for j in range(len(word)):
                if word[:j+1] in roots:
                    sentence[i] = word[:j+1]
                    break
        return " ".join(sentence)


'''
Trie
O(N*W) time / O(N) space where W is the length of the word and N is 
the length of the sentence.
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.end = True
        
        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            word = sentence[i]
            cur = root
            for j in range(len(word)):
                if word[j] in cur.children:
                    cur = cur.children[word[j]]
                    if cur.end == True:
                        sentence[i] = word[:j+1]
                        break
                else:
                    break
        return " ".join(sentence)