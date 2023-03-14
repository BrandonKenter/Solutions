class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        label_sums = [0] * len(edges)
        for i in range(len(edges)):
            label_sums[edges[i]] += i
        
        maxi = maxi_i = 0
        for i, s in enumerate(label_sums):
            if s > maxi:
                maxi = s
                maxi_i = i
        return maxi_i
        