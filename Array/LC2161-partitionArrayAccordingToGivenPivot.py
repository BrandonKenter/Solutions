class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        le, eq, gr = [], [], [] # less, equal, greater than pivot arrays

        for i in range(len(nums)):
            if nums[i] < pivot: le.append(nums[i])
            elif nums[i] == pivot: eq.append(nums[i])
            else: gr.append(nums[i])
        return le + eq + gr
