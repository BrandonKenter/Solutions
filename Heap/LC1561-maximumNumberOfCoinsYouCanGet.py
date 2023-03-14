class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        max_h = [-p for p in piles]
        heapify(max_h)
        
        my_coins = 0
        n = len(piles)
        for i in range(n // 3):
            heappop(max_h)
            my_coins += (-1 * heappop(max_h))
        return my_coins
        