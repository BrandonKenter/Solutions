'''
Brute-force
O(N^2)
'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(dominoes) - 1):
            for j in range(i + 1, len(dominoes)):
                a, b, c, d = dominoes[i][0], dominoes[i][1], dominoes[j][0], dominoes[j][1]
                if a == c and b == d or a == d and b == c:
                    cnt += 1
        return cnt


'''
O(N)
'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = defaultdict(int)
        for dom in dominoes:
            pair = tuple(sorted(dom))
            dic[pair] += 1
        
        cnt = 0
        for n in dic.values():
            pairs = n*(n-1)//2
            cnt += pairs
        return cnt
