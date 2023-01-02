class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)

        def dfs(cur, parent):
            if cur is None:
                return
            
            if cur and parent:
                adj[cur].append(parent)
                adj[parent].append(cur)
            dfs(cur.left, cur)
            dfs(cur.right, cur)


        def get_dist_k_nodes():
            q = deque([target])
            vis = set([target])
            level = 0

            while q:
                level_nodes = []
                for i in range(len(q)):
                    cur = q.popleft()
                    level_nodes.append(cur.val)
                    for nei in adj[cur]:
                        if nei not in vis:
                            q.append(nei)
                            vis.add(nei)
                if level == k:
                    return level_nodes
                level += 1
            return []
        
        dfs(root, None)
        kth_level = get_dist_k_nodes()
        return kth_level