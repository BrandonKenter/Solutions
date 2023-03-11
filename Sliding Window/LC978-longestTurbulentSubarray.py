class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxi = 1
        first_l = second_l = 0
        for right in range(1, len(arr)):
            if right % 2 == 0 and arr[right-1] > arr[right] or right % 2 == 1 and arr[right-1] < arr[right]:
                    maxi = max(maxi, right - first_l + 1)
            else:
                first_l = right
            if right % 2 == 1 and arr[right-1] > arr[right] or right % 2 == 0 and arr[right-1] < arr[right]:
                maxi = max(maxi, right - second_l + 1)
            else:
                second_l = right
        return maxi
