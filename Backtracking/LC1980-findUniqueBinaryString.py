class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Cast nums to set to check if s is in nums in O(1) time
        nums_set = set(nums)

        # Initialize state collection
        s_arr = []

        # Create backtracking method
        def backtrack(i):
            # Check if current state is a solution
            # If so, return it  
            # Otherwise, return to previous choice space
            if len(s_arr) == len(nums):
                s = "".join(s_arr)
                if s not in nums_set:
                    return s
                else:
                    return
            
            # State is valid, so can proceed to make choice on this state
            # Choice to use a '1' at this position
            # Reflect current choice in state collection
            s_arr.append('1')
            # Recurse on next choice space of next state and store result in variable
            add_one = backtrack(i + 1)
            # Need to evaluate return value since finding a solution means we should return
            if add_one: return add_one
            # Clean up current choice (backtrack)
            s_arr.pop()
            
            # Choice to use a '0' at this position
            # Reflect current choice in state collection
            s_arr.append('0')
            # Recurse on next choice space of next state and store result in variable
            add_zero = backtrack(i + 1)
            # Need to evaluate return value since finding a solution means we should return
            if add_zero: return add_zero
            # Clean up current choice (backtrack)
            s_arr.pop()
        
        return backtrack(0)