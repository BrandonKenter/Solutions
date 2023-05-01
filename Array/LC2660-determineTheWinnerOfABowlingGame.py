class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        p1 = p2 = 0
        for i in range(len(player1)):
            if i == 0:
                p1, p2 = p1 + player1[i], p2 + player2[i]
            elif i == 1:
                p1 += player1[i] if player1[i-1] != 10 else player1[i] * 2
                p2 += player2[i] if player2[i-1] != 10 else player2[i] * 2
            else:
                p1 += player1[i] if player1[i-1] != 10 and player1[i-2] != 10 else player1[i] * 2
                p2 += player2[i] if player2[i-1] != 10 and player2[i-2] != 10 else player2[i] * 2
                
        if p1 > p2: return 1
        elif p2 > p1: return 2
        else: return 0
