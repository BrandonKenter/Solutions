class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        
        start = 0
        s = 0
        for i in range(len(gas)):
            s += gas[i]
            s -= cost[i]
            if s < 0:
                s = 0
                start = i + 1
        return start