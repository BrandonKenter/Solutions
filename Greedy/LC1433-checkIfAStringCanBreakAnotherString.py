class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        if len(s1) == 1: return True
        s1_arr = sorted([ord(c) for c in s1])
        s2_arr = sorted([ord(c) for c in s2])
        
        higher = None
        for i in range(len(s1)):
            if higher == 's1':
                if s1_arr[i] < s2_arr[i]:
                    return False
            elif higher == 's2':
                if s2_arr[i] < s1_arr[i]:
                    return False
            else:
                if s1_arr[i] > s2_arr[i]:
                    higher = 's1'
                elif s2_arr[i] > s1_arr[i]:
                    higher = 's2'
        return True
        