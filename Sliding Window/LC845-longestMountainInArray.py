class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3: return 0
        left = right = longest = 0
        while right < len(arr):
            # Get to the start of the left side of the mountain
            while left < len(arr) - 1 and arr[left] >= arr[left+1]:
                left += 1
            right = left

            # Get to the top of the mountain
            while right < len(arr) - 1 and arr[right] < arr[right+1]:
                right += 1
            # If we reach the end of the array, there can be no
            #   right side of the mountain
            if right == len(arr) - 1:
                return longest
            # Save index of top of mountain so we can check if 
            #   we find a right side of at least length 1 below
            top = right 

            # Get to the bottom of the mountain
            while right < len(arr) - 1 and arr[right] > arr[right+1]:
                right += 1
            # Check if we have a right side
            if top != right:
                longest = max(longest, right - left + 1)
            # Update left to start at the first position that can be
            #   the start of the next mountain
            left = right
        return longest
