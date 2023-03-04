class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        mid = arr[(n-1)//2]
        res = []
        left, right = 0, len(arr) - 1
        for i in range(k):
            if abs(arr[left] - mid) == abs(arr[right] - mid):
                if arr[left] > arr[right]:
                    res.append(arr[left])
                    left += 1
                else:
                    res.append(arr[right])
                    right -= 1
            elif abs(arr[left] - mid) > abs(arr[right] - mid):
                res.append(arr[left])
                left += 1
            else:
                res.append(arr[right])
                right -= 1
        return res
        