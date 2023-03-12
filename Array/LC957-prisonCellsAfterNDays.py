class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def nextDay(cells):
            copy = cells.copy()
            for i in range(1, len(cells) - 1):
                if copy[i-1] == copy[i+1]:
                    cells[i] = 1
                else:
                    cells[i] = 0
            cells[0] = 0
            cells[-1] = 0   
            return cells
        
        day1 = nextDay(cells)[:]
        n -= 1
        count = 0
        
        while n > 0:
            day = nextDay(cells)[:]
            n -= 1
            count += 1
            
            if day == day1:
                n = n % count
        return cells
