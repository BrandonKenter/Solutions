class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False

    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                node = TrieNode()
                cur.children[c] = node
            cur = cur.children[c]
        cur.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(board), len(board[0])
        vis, res = set(), set()
        cur_word = []

        # Initialize the trie with the list of words
        for word in words:
            root = TrieNode()
            for word in words:
                root.add_word(word)

        def backtrack(r, c, cur):
            # Current state is not valid, so return
            if(
                r not in range(m) or 
                c not in range(n) or 
                (r, c) in vis or
                board[r][c] not in cur.children
            ):
                return
            
            # Current state is valid, so our choice is to add it to our path.
            # Note that theres a distinction between a state being valid and
            # a state being a solution. A solution state is inherently valid, 
            # but the reverse is not inherently true. So the "is valid state" 
            # check is done in the base case, and the "is solution" check is 
            # done here. 
            vis.add((r, c))
            cur_word.append(board[r][c])
            cur = cur.children[board[r][c]]
            if cur.end:
                res.add("".join(cur_word))
            
            # Explore all future candidates. The reason we don't return early
            # in this problem (some problems have a statement like: if backtrack() 
            # return True) is because we are looking for ALL words that exist in 
            # the board. So when we see that cur.end is True, we found only one 
            # word. So we still continue with recursion.
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                backtrack(nei_r, nei_c, cur)
            # Clean up the choice
            vis.remove((r, c))
            cur_word.pop()
        
        # We have to call backtrack on every cell to explore all possible states
        for r in range(m):
            for c in range(n):
                backtrack(r, c, root)
        return list(res)