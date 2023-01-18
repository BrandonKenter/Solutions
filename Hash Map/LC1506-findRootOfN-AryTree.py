"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

'''
- O(N) time / O(N) space
- Use a hash map to count the indegrees of each node
- For each node in the tree, increment their children's indegree by 1
- Iterate through the original tree list and if the node is not in the map, it's the root
'''
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        indegrees = defaultdict(int)
        for node in tree:
            for child in node.children:
                indegrees[child] += 1
        
        for node in tree:
            if node not in indegrees:
                return node
        

'''
- O(N) time / O(1) space
- Using a sum of all node values in the tree
- Add each node's value to sum, subtract each node's child values from sum
- Resulting node_sum is the value of the root node
- Search for the root node in the original tree list
'''
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        node_sum = 0
        for node in tree:
            if node:
                node_sum += node.val
                for child in node.children:
                    node_sum -= child.val
        for node in tree:
            if node and node.val == node_sum:
                return node