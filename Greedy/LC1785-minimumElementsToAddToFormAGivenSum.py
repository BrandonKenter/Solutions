class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        dif = abs(goal - s)
        # Greedily use as many limit elements as possible
        limit_count = dif // limit
        s -= limit * limit_count
        # If there is a remainder after greedily using the max multiple 
        #   of limit, add one to result.
        return limit_count + 1 if dif % limit else limit_count
        