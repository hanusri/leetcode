from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.curr.right = node
                self.curr = node
                inorder(node.right)
        
        ans = self.curr = TreeNode()
        inorder(root)
        return ans.right