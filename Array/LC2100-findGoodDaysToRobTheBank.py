class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        decreasing = [0] * len(security)
        consec = 0
        for i in range(1, len(security)):
            if security[i] <= security[i-1]:
                consec += 1
            else:
                consec = 0
            decreasing[i] = consec
            
        increasing = [0] * len(security)
        consec = 0
        for i in range(len(security) - 2, -1, -1):
            if security[i] <= security[i+1]:
                consec += 1
            else:
                consec = 0
            increasing[i] = consec

        res = []
        for i in range(len(security)):
            if decreasing[i] >= time and increasing[i] >= time:
                res.append(i)
        return res
        