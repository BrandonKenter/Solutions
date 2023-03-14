class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_customers = sum(customers)
        max_loss = total_lost = cur_loss = left = 0
        for right in range(len(customers)):
            if grumpy[right]:
                total_lost += customers[right]
                cur_loss += customers[right]
                max_loss = max(max_loss, cur_loss)
            if right - left + 1 == minutes:
                if grumpy[left]:
                    cur_loss -= customers[left]
                left += 1
        return total_customers - total_lost + max_loss
        