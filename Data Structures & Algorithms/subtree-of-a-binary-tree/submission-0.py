# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None: 
            return False # either p xor q, so unequal subtree size.

        # both p and q have atlast one node, check they're equal.
        if p.val != q.val:
            return False
            
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        result1 = self.isSubtree(root.left, subRoot)
        result2 = self.isSubtree(root.right, subRoot)
        return result1 or result2 or self.isSameTree(root, subRoot)
