class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        r = c = 0
        char_map = {}
        for char in "abcdefghijklmnopqrstuvwxyz":
            char_map[char] = (r, c)
            c += 1
            if c == 5:
                r += 1
                c = 0
        
        r = c = 0
        res = []
        for char in target:
            targ_r, targ_c = char_map[char]
            if (r, c) == char_map['z']:
                self.move_row(r, targ_r, res)
                self.move_col(c, targ_c, res)
            else:
                self.move_col(c, targ_c, res)
                self.move_row(r, targ_r, res)
                
            res.append('!')
            r, c = targ_r, targ_c
        return "".join(res)
    

    def move_row(self, r, targ_r, res):
        r_change = targ_r - r
        if r_change < 0:
            res.append('U' * (-1 * r_change))
        else:
            res.append('D' * r_change)
    

    def move_col(self, c, targ_c, res):
        c_change = targ_c - c
        if c_change < 0:
            res.append('L' * (-1 * c_change))
        else:
            res.append('R' * (c_change))
