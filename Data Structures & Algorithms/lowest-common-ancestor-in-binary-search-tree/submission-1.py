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
        
        # get all ancestors from the root to p and q respectively, including
        # p and q themselves respectively.
        pAncestors = self.getAncestors(root, p)
        qAncestors = self.getAncestors(root, q)
        
        # Lowest Common Ancestor (lca) is simply the last assignment before
        # the pAncestors and qAncestors differ in corresponding ancestor.
        lca = None
        for i in range(min(len(pAncestors), len(qAncestors))):
            if pAncestors[i].val != qAncestors[i].val:
                break
            lca = pAncestors[i]
        
        return lca
