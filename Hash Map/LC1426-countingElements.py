class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        count = 0
        for num in arr:
            if num + 1 in arr_set:
                count += 1
        return count