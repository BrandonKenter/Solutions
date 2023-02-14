# Does not have the optimization, so all test cases won't pass
# This is a interview-friendly solution (optimizations won't be expected in an interview)
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
        root = TrieNode()
        for word in words:
            root.add_word(word)

        def backtrack(r, c, cur):
            # Base case to check if state is valid
            if (
                r not in range(m) or 
                c not in range(n) or 
                (r, c) in vis or
                board[r][c] not in cur.children
            ):
                return

            # State is valid, so update state
            vis.add((r, c))
            cur_word.append(board[r][c])
            cur = cur.children[board[r][c]]

            # Check if state is a solution and add to collection if so
            # Do not return because we are asked for ALL solutions
            if cur.end:
                res.add("".join(cur_word))
            
            # Make next choices from the current state by calling backtrack for every
            # adjacent cell
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                backtrack(nei_r, nei_c, cur)

            # Clean up the choice
            vis.remove((r, c))
            cur_word.pop()
        
        # Call backtrack on every cell whose char is a child of root to explore 
        # all possible states
        for r in range(m):
            for c in range(n):
                if board[r][c] in root.children:
                    backtrack(r, c, root)
        return list(res)
