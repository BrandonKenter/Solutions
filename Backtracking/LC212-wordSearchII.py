# Valid state checking before backtrack call
# Fits my pattern better of just having solution state check at beginning of backtrack method
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
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Initialize the trie with the list of words
        root = TrieNode()
        for word in words:
            root.add_word(word)
        
        # Initialize state collection
        vis = set()
        cur_word = []
        # Initialize result collection
        res = set()


        # Create backtracking method
        # State parameters: 
        #   - r where r is the row in the board
        #   - c where c is the col in the board
        #   - cur where cur is the current node in the Trie
        def backtrack(r, c, cur):
            # Check if current state is a solution
            # If so, add to result collection
            # Do NOT return to previous choice space because there can
            # be more solutions on this decision path
            if cur.end:
                res.add("".join(cur_word))

            # Make next choices from current state by calling backtrack
            # for every adjacent cell
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                if (
                    nei_r not in range(m) or 
                    nei_c not in range(n) or 
                    (nei_r, nei_c) in vis or
                    board[nei_r][nei_c] not in cur.children
                ):
                    continue

                # Choice meets constraints
                # Reflect current choice in state collections
                vis.add((nei_r, nei_c))
                cur_word.append(board[nei_r][nei_c])

                # Recurse on next choice space of next state
                backtrack(nei_r, nei_c, cur.children[board[nei_r][nei_c]])

                # Clean up current choice (backtrack)
                # r, c and cur are automatically cleaned up because we are returning
                # to the previous execution context with previous args
                vis.remove((nei_r, nei_c))
                cur_word.pop()
        
        # We have to call backtrack on every cell to explore all possible states
        for r in range(m):
            for c in range(n):
                if board[r][c] in root.children:
                    vis.add((r, c))
                    cur_word.append(board[r][c])
                    cur = root.children[board[r][c]]
                    backtrack(r, c, cur)
                    vis.remove((r, c))
                    cur_word.pop()
        return list(res)



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
