class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_set = set(arr1)
        arr1_counts = [0] * 1001
        for num in arr1:
            arr1_counts[num] += 1
        
        res = []
        for num in arr2:
            if num in arr1_set:
                for i in range(arr1_counts[num]):
                    res.append(num)
                arr1_counts[num] = 0
        for num, freq in enumerate(arr1_counts):
            for i in range(freq):
                res.append(num)
        return res