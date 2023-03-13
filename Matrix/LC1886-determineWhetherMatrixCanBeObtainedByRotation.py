'''
zip function
'''
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4): 
            if mat == target: return True
            mat = [list(x) for x in zip(*mat[::-1])]
        return False 

'''
manual
'''
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        for _ in range(4):
            N = len(mat)
            l, r = 0, N - 1
            t, b = 0, N - 1
            while l <= r:
                for i in range(r - l):
                    # Save top_l
                    top_l = mat[t][l + i]
                    
                    # bot_l -> top_l
                    mat[t][l + i] = mat[b - i][l]
                    
                    # bot_r -> bot_l
                    mat[b - i][l] = mat[b][r - i]
                    
                    # top_r -> bot_l
                    mat[b][r - i] = mat[t + i][r]
                    
                    # top_l -> top_r
                    mat[t + i][r] = top_l
                if mat == target:
                    return True
                l += 1
                r -= 1
                t += 1
                b -= 1
        return False
        
