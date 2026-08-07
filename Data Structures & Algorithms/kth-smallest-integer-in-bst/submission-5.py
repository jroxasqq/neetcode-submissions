# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # an inorder traversal of a BST traverses it in ascending sorted order.
    def inorder(self, root: Optional[TreeNode], result):
        if not root:
            return

        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)

    def kthSmallest(self, root: Optional[TreeNode], k: int, num_visited: int=0, result: int=0) -> int:
        result = []
        self.inorder(root, result)
        return result[k - 1]
