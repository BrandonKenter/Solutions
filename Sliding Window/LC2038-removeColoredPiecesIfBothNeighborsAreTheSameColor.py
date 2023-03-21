'''
Dynamic-size sliding window
Two-pass
'''
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_count, b_count = self.get_count('A', colors), self.get_count('B', colors)
        return a_count > b_count

    def get_count(self, c, colors):
        count = 0
        left = 0
        for right in range(len(colors)):
            if colors[right] != c:
                left = right + 1
            elif right - left + 1 >= 3:
                count += 1
        return count


'''
Static-size sliding window
Two-pass
'''
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_count = b_count = a_cur = b_cur = 0
        left = 0
        for right in range(len(colors)):
            if colors[right] == 'A':
                a_cur += 1
            else:
                b_cur += 1
            if right - left + 1 == 3:
                if a_cur == 3:
                    a_count += 1
                elif b_cur == 3:
                    b_count += 1
                if colors[left] == 'A':
                    a_cur -= 1
                else:
                    b_cur -= 1
                left += 1
        return a_count > b_count
                