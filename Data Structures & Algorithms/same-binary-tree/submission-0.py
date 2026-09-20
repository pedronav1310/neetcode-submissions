# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pTree=[]
        qTree=[]
        def tree(p, solution):
            if not p:
                solution.append(None)
                return 
        
            solution.append(p.val)
            tree(p.left, solution)
            tree(p.right, solution)
        tree(p, pTree)
        tree(q, qTree)
        print(pTree, qTree)
        return pTree == qTree