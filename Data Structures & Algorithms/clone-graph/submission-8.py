"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from copy import deepcopy
class Solution:
    def cloneGraph(self, node: Optional['Node'], visited: set[tuple[int, int]]=set()) -> Optional['Node']:
        if not node:
            return

        # deep copies assign a different reference than the original node to newNode.
        newNode = deepcopy(node)

        # visited set is so we don't get stuck in loops.
        visited.add(newNode.val)

        # for each neighbor we recursively call this function to get a deep copy of each
        # of the neighbours if they haven't be visited before (again to prevent loops).
        for idx, neighbor in enumerate(newNode.neighbors):
            if neighbor.val not in visited:
                newNode.neighbors[idx] = self.cloneGraph(neighbor, visited)

        return newNode