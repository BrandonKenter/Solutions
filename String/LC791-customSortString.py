class Solution:
    def customSortString(self, order: str, s: str) -> str:
        indices = defaultdict(int)
        for i, c in enumerate(order):
            if c not in indices:
                indices[c] = i
        
        # Use array buckets because empty string buckets 
        # with concatenation will be O(N^2) time complexity
        buckets = [[] for i in range(201)]
        for c in s:
            # Put the character in the bucket for its respective index in indices
            # If c is not in the indices map, it defaults to 0
            # This is fine because these chars can be anywhere in the result string
            # So the chars in s that are not in order will be at the beginning of the res string
            i = indices[c] 
            buckets[i].append(c)
        
        res = []
        for c_arr in buckets:
            if c_arr:
                res.append("".join(c_arr))
        return "".join(res)
        