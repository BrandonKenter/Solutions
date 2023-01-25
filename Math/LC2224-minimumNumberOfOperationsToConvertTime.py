class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur_hour, cur_min = current.split(':')
        cur_min = int(cur_min) + int(cur_hour) * 60
        cor_hour, cor_min = correct.split(':')
        cor_min = int(cor_min) + int(cor_hour) * 60
        
        # diff = absolute difference in minutes between current and correct minutes
        # ops = number of operations it takes to cover the difference
        diff, ops = abs(cur_min - cor_min), 0 
        increments = [60, 15, 5, 1]
        for inc in increments:
            # If the current diff is larger than current inc, use it as a step
            if diff // inc > 0:
                div = diff // inc
                ops += div 
                diff -= div * inc
        return ops