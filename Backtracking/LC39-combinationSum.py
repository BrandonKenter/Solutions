class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        combination = []
        
        def backtrack(i, cur_sum):
            if i == len(candidates) or cur_sum > target:
                return 
            if cur_sum == target:
                out.append(combination[:])
                return
            
            combination.append(candidates[i])
            backtrack(i, cur_sum + candidates[i])
            combination.pop()
            
            backtrack(i + 1, cur_sum)
        backtrack(0, 0)
        return out