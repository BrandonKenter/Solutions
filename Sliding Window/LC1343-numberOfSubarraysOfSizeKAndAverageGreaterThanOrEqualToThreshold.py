class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = cur_sum = left = 0
        for right in range(len(arr)):
            cur_sum += arr[right]

            if right - left + 1 == k:
                avg = cur_sum // (right - left + 1)
                if avg >= threshold:
                    count += 1
                cur_sum -= arr[left]
                left += 1
        return count