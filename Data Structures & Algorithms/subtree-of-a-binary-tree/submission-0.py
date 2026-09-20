# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.tree = []
        self.subTree = []
        def buildTree(root, tree):
            if not root:
                tree.append(None)
                return
            
            tree.append(root.val)
            left = root.left
            right = root.right
            buildTree(left, tree)
            buildTree(right, tree)
        buildTree(root, self.tree)
        buildTree(subRoot, self.subTree)
        n = len(self.subTree)

        for i in range(len(self.tree) - n + 1):
            if self.tree[i:i+n] == self.subTree:
                return True

        return False