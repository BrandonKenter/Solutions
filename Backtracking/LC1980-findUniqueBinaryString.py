class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_set = set(nums)
        combo = []

        def backtrack():
            if len(combo) == len(nums[0]):
                if "".join(combo) not in nums_set:
                    return "".join(combo)
                else:
                    return None
            
            combo.append("1")
            one = backtrack()
            if one: return one
            combo.pop()

            combo.append("0")
            zero = backtrack()
            if zero: return zero
            combo.pop()
            return None

        return backtrack()
