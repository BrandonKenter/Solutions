class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        l_less, l_greater, r_less, r_greater = [0]*n, [0]*n, [0]*n, [0]*n
        res = 0
        for i in range(1, len(rating) - 1):
            for j in range(len(rating)):
                if j < i:
                    if rating[j] < rating[i]: l_less[i] += 1
                    elif rating[j] > rating[i]: l_greater[i] += 1
                elif j > i:
                    if rating[j] < rating[i]: r_less[i] += 1
                    elif rating[j] > rating[i]: r_greater[i] += 1
            res += l_less[i] * r_greater[i] + l_greater[i] * r_less[i]
        return res
