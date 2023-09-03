class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        num_to_i = {}
        for i, num in enumerate(arr):
            if num * 2 in num_to_i or num / 2 in num_to_i:
                return True
            num_to_i[num] = i
        return False
        