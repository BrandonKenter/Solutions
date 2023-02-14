class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # Initialize result collecction
        res = []
        # Initialize state collection
        combo = []
        
        # Create backtracking method
        # State parameters: 
        #   - i where i is the index of the candidates array
        #   - cur_sum where cur_sum is the current sum of the picked integers   
        def backtrack(i, cur_sum):
            # Check if current state is a solution
            # If so, add to result collection
            # Return to previous choice space
            if cur_sum == target:
                res.append(combo[:])
                return
            
            # Base case to check if current state is valid
            if i == len(candidates) or cur_sum > target:
                return
            
            # State is valid, so can proceed to make choice on this state
            # Reflect current choice in state collection
            # Current choice to include candidates[i]
            combo.append(candidates[i])
            # Recurse on next choice space of next state
            backtrack(i + 1, cur_sum + candidates[i])
            # Clean up current choice (backtrack)
            # i and cur_sum are automatically cleaned up because we are 
            # returning to the previous execution context with previous args
            combo.pop()
            
            # Recurse on choice space of next state
            # Current choice to NOT include candidates[i]
            # Skip all instances of nums[i] first
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, cur_sum)

        backtrack(0, 0)
        return res
