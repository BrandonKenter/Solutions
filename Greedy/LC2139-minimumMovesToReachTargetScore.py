class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        cur = target
        while cur != 1:
            if maxDoubles and cur % 2 == 0:
                cur = cur // 2
                moves += 1
                maxDoubles -= 1
            elif not maxDoubles:
                moves += cur - 1
                cur = 1
            else:
                moves += 1
                cur -= 1
        return moves
        