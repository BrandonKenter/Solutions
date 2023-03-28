class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.value = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, value):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.value = value
    
    def get_pre_values(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        stack = [cur]
        s = 0
        while stack:
            cur = stack.pop()
            s += cur.value
            for node in cur.children.values():
                stack.append(node)
        return s
            
            
class MapSum:

    def __init__(self):
        self.m = Trie()

    def insert(self, key: str, val: int) -> None:
        self.m.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.m.get_pre_values(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)