class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right = 0, len(cardPoints) - k
        total = sum(cardPoints[right:])
        res = total
        
        while right < len(cardPoints):
            total -= cardPoints[right]
            total += cardPoints[left]
            res = max(res, total)
            left += 1
            right += 1
        return res