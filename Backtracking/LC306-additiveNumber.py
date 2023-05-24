class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        nums = []

        def backtrack(i):
            if i == len(num) and len(nums) >= 3:
                return True
            if i == len(num):
                return False
            
            for j in range(i, len(num)):
                cur_num = num[i:j+1]
                if len(cur_num) > 1 and cur_num[0] == '0':
                    return False
                cur_num = int(cur_num)

                if len(nums) <= 1:
                    nums.append(cur_num)
                    if backtrack(j+1):
                        return True
                    nums.pop()
                else:
                    if nums[-2] + nums[-1] == cur_num:
                        nums.append(cur_num)
                        if backtrack(j+1):
                            return True
                        nums.pop()
            return False
            
        return backtrack(0)
