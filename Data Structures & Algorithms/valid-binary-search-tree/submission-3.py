# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower=float('-inf'), upper=float('inf')) -> bool:
        if not root:
            return True
        
        if not (lower < root.val < upper):
            return False
        
        # with this pre-order traversal,
        # we recursively call on the left subtree with root value as the
        # strict upper bound to ensure the left subtree only has values
        # strictly less than the current node (root) value. Similarly
        # for the strict lower bound of the right subtree recursive call.
        isLeftSubtreeValid = self.isValidBST(root.left, lower, root.val)
        isRightSubtreeValid = self.isValidBST(root.right, root.val, upper)
         
        return isLeftSubtreeValid and isRightSubtreeValid


