class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(board), len(board[0])
        vis = set()

        # Edge case handling
        char_count = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                char_count[board[i][j]] += 1
        for char in word:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if (
                r not in range(m) or 
                c not in range(n) or
                (r, c) in vis or 
                board[r][c] != word[i]
            ):
                return False

            vis.add((r, c))
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if backtrack(nei_r, nei_c, i+1):
                    return True
            vis.remove((r, c))
            return False
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and backtrack(r, c, 0): 
                    return True
        return False