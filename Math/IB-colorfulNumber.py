class Solution:
    def colorful(self, A):
        prods = set()
        A = str(A)

        for i in range(len(A)):
            cur_prod = 1
            for j in range(i, len(A)):
                cur_prod *= int(A[j])
                if cur_prod in prods: return 0
                prods.add(cur_prod)
        return 1