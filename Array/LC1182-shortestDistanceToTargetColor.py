class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        pre, post = [[-1, -1, -1] for i in range(len(colors))], [[-1, -1, -1] for i in range(len(colors))]
        pre_map, post_map = {}, {}
        for i in range(len(colors)):
            color = colors[i]
            pre_map[color] = i
            pre[i][0] = pre_map[1] if 1 in pre_map else float('inf')
            pre[i][1] = pre_map[2] if 2 in pre_map else float('inf')
            pre[i][2] = pre_map[3] if 3 in pre_map else float('inf')
        
        for i in range(len(colors) - 1, -1, -1):
            color = colors[i]
            post_map[color] = i
            post[i][0] = post_map[1] if 1 in post_map else float('inf')
            post[i][1] = post_map[2] if 2 in post_map else float('inf')
            post[i][2] = post_map[3] if 3 in post_map else float('inf')

        res = []
        for q in queries:
            i, color = q[0], q[1]
            pre_arr = pre[i]
            post_arr = post[i]
            res.append(min(abs(pre_arr[color-1] - i), abs(post_arr[color-1] - i)) if pre_arr[color-1] != float('inf') or post_arr[color-1] != float('inf') else -1)
        return res
        