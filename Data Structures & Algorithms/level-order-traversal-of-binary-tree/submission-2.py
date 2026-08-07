# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getLevelOrder(self, root: Optional[TreeNode], level: int, result: List[List[int]]):
        if not root:
            return []
        
        if level >= len(result):
            result.append([])
        result[level].append(root.val)

        self.getLevelOrder(root.left, level + 1, result)
        self.getLevelOrder(root.right, level + 1, result)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.getLevelOrder(root, 0, result)
        return result