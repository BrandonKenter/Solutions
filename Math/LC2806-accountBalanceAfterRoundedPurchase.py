class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        tens = purchaseAmount // 10
        ones = purchaseAmount % 10
        if ones <= 4:
            return 100 - tens * 10
        else:
            return 100 - (tens + 1) * 10
