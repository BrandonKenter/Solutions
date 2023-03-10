class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

        res = []
        for r, c in queens:
            for dir in directions:
                can_attack = self.search_dir(r, c, dir, queens, king)
                if can_attack:
                    res.append([r, c])
                    break
        return res

        
    def search_dir(self, r, c, dir, queens, king):
        while True:
            r, c = r + dir[0], c + dir[1]
            if (
                r not in range(8) or 
                c not in range(8) or 
                [r, c] in queens
            ):
                return False
            if [r, c] == king:
                return True
        