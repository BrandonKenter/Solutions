class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n, s = len(arr), sum(arr)
        re = .05 * len(arr)
        re_total = re * 2
        left, right = 0, len(arr) - 1
        for i in range(int(re)):
            s -= arr[left]
            s -= arr[right]
            left += 1
            right -= 1
        return s / (n - re_total)
        