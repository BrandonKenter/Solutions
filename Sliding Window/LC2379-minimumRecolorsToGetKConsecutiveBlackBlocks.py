class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_white = float('inf')
        cur_white = left = 0
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                cur_white += 1
            
            if right - left + 1 == k:
                min_white = min(min_white, cur_white)
                if blocks[left] == 'W':
                    cur_white -= 1
                left += 1
        return min_white