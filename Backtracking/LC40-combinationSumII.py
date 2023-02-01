class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        combination = []
        
        def backtrack(i, cur_sum):
            if cur_sum == target:
                output.append(combination[:])
                return
            if i == len(candidates) or cur_sum > target:
                return
            
            # Decision to include candidates[i]
            combination.append(candidates[i])
            backtrack(i + 1, cur_sum + candidates[i])
            combination.pop()
            
            # Decision to NOT include candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, cur_sum)
        backtrack(0, 0)
        return output