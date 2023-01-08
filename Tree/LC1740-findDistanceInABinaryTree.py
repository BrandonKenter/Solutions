# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
BFS
'''
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        adj = defaultdict(list)
        def create_adj(cur):
            if cur is None:
                return
            
            if cur.left:
                adj[cur.val].append(cur.left.val)
                adj[cur.left.val].append(cur.val)
                create_adj(cur.left)
            if cur.right:
                adj[cur.val].append(cur.right.val)
                adj[cur.right.val].append(cur.val)
                create_adj(cur.right)
        create_adj(root)

        dist = 0
        vis = set([p])
        deq = deque([p])
        while deq:
            for i in range(len(deq)):
                cur = deq.popleft()

                if cur == q:
                    return dist
                
                for nei in adj[cur]:
                    if nei not in vis:
                        deq.append(nei)
                        vis.add(nei)
            dist += 1


'''
DFS
'''
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        def create_adj(cur):
            if cur is None:
                return
            
            if cur.left:
                adj[cur.val].append(cur.left.val)
                adj[cur.left.val].append(cur.val)
                create_adj(cur.left)
            if cur.right:
                adj[cur.val].append(cur.right.val)
                adj[cur.right.val].append(cur.val)
                create_adj(cur.right)
        
        def find_dist(cur, cur_dist):
            nonlocal dist
            if cur == q:
                dist = cur_dist
                return True

            cur_dist += 1
            vis.add(cur)

            for nei in adj[cur]:
                if nei not in vis:
                    if find_dist(nei, cur_dist): return True
            return False
                        
        vis = set()
        adj = defaultdict(list)
        create_adj(root)
        dist = 0
        find_dist(p, 0)
        return dist
