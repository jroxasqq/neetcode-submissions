# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAncestors(self, root: TreeNode, target: TreeNode):
        if not root:
            return []

        if root.val == target.val:
            return [target]

        leftAncestors = self.getAncestors(root.left, target)
        rightAncestors = self.getAncestors(root.right, target)
        if leftAncestors:
            return [root, *leftAncestors]
        elif rightAncestors:
            return [root, *rightAncestors]

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # keep track of all ancestors starting from the root.

        pAncestors = self.getAncestors(root, p)
        qAncestors = self.getAncestors(root, q)
        
        lca = None
        for i in range(min(len(pAncestors), len(qAncestors))):
            if  pAncestors[i].val != qAncestors[i].val:
                break
            lca = pAncestors[i]
        
        return lca
