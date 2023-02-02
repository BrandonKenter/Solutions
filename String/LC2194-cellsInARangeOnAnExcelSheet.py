class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s1, s2 = s.split(":")
        col1, row1 = s1[0], s1[1]
        col2, row2 = s2[0], s2[1]
        
        res = []
        for col in range(ord(col1), ord(col2) + 1):
            for row in range(int(row1), int(row2) + 1):
                cell = ""
                cell += chr(col)
                cell += str(row)
                res.append(cell)
        return res