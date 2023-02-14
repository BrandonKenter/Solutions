# Does not have the optimization, so all test cases won't pass
# This is a interview-friendly solution (optimizations won't be expected in an interview)
class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        arr.sort(reverse=True)
        n, total_array_sum = len(arr), sum(arr)
        target_sum = total_array_sum // k
        if total_array_sum % k != 0:
            return False

        # Initialize state collection
        taken = [False] * n
        
        # Create backtracking method
        # State parameters: 
        #   - count where count is the count of partitions created
        #   - cur_sum where cur_sum is the current sum of the current partition
        def backtrack(count, cur_sum):
            # Check if current state is a solution
            # If so, return True because asked if ONE solution exists
            if count == k:
                return True

            # State is valid, so can proceed to make choice on this state
            # Iterate through choices for current state
            for j in range(n):
                # Check if choice meets constraints before attempting choice
                # If choice does not meet constraints, continue (prune)
                if (
                    taken[j] or
                    cur_sum + arr[j] > target_sum
                ):
                    continue

                # Choice meets constraints
                # Reflect current choice in state collections
                taken[j] = True
                # Recurse on next choice space of next state
                # Use two backtrack calls inside an if-else because we
                #   want to increment count and reset cur_sum if the 
                #   current choice finishes a partition
                # Add if condition and return value
                if cur_sum + arr[j] < target_sum:
                    if backtrack(count, cur_sum + arr[j]):
                        return True
                else:
                    if backtrack(count + 1, 0):
                        return True
                # Clean up choice (backtrack)
                # count and cur_sum are automatically cleaned up because we 
                # are returning to the previous execution context with previous arg
                taken[j] = False
            
        return backtrack(0, 0)