class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        if A == None:
            return A
        path = []
        
        def dfs(cur, cur_path):
            if cur is None:
                return False
                
            cur_path.append(cur.val)
            if cur.val == B:
                path = cur_path[::]
                return True

            if dfs(cur.left, cur_path) or dfs(cur.right, cur_path):
                return True
                
            cur_path.pop()
            return False
        
        dfs(A, [])
        return path