class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = [(num, i) for i, num in enumerate(arr)]
        sorted_arr.sort()
        res = [0] * len(arr)
        prev, rank = -1, 0 

        for i in range(len(sorted_arr)):
            idx = sorted_arr[i][1]
            if sorted_arr[i][0] == prev:
                res[idx] = rank
            else:
                rank += 1
                res[idx] = rank
                prev = sorted_arr[i][0]
        return res