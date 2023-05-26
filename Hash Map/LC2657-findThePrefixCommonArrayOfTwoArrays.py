class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        A_seen = set()
        B_seen = set()
        common = 0
        res = []
        for i in range(len(A)):
            if A[i] in B_seen and A[i] not in A_seen:
                common += 1
            if B[i] in A_seen and B[i] not in B_seen:
                common += 1
            if B[i] == A[i] and A[i] not in A_seen and B[i] not in B_seen:
                common += 1
            A_seen.add(A[i])
            B_seen.add(B[i])
            res.append(common)
        return res
        