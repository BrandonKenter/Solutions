class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        last_row = [1]
        for i in range(rowIndex):
            cur_row = [1] * (len(last_row) + 1)
            for j in range(1, len(cur_row) - 1):
                cur_row[j] = last_row[j-1] + last_row[j]
            last_row = cur_row
        return last_row
    